from typing import Any
import logging
import yaml
from pyspark.sql import SparkSession
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat

from databricks.labs.dqx.checks_storage import is_table_location
from databricks.labs.dqx.config import (
    InputConfig,
    ProfilerConfig,
    BaseChecksStorageConfig,
    InstallationChecksStorageConfig,
)
from databricks.labs.dqx.engine import DQEngine
from databricks.labs.dqx.io import read_input_data
from databricks.labs.dqx.profiler.generator import DQGenerator
from databricks.labs.dqx.profiler.profiler import DQProfiler
from databricks.labs.blueprint.installation import Installation

from databricks.labs.dqx.utils import safe_strip_file_from_path

logger = logging.getLogger(__name__)


class ProfilerRunner:
    """Runs the DQX profiler on the input data and saves the generated checks and profile summary stats."""

    def __init__(
        self,
        ws: WorkspaceClient,
        spark: SparkSession,
        dq_engine: DQEngine,
        installation: Installation,
        profiler: DQProfiler,
        generator: DQGenerator,
    ):
        self.ws = ws
        self.spark = spark
        self.dq_engine = dq_engine
        self.installation = installation
        self.profiler = profiler
        self.generator = generator

    def run(
        self,
        run_config_name: str,
        input_config: InputConfig,
        profiler_config: ProfilerConfig,
        product: str,
        install_folder: str,
    ) -> None:
        """
        Run the DQX profiler for the given run configuration and save the generated checks and profile summary stats.

        Args:
            run_config_name: Name of the run configuration (used in storage config).
            input_config: Input data configuration.
            profiler_config: Profiler configuration.
            product: Product name for the installation (used in storage config).
            install_folder: Installation folder path (used in storage config).

        Returns:
            A tuple containing the generated checks and profile summary statistics.
        """
        df = read_input_data(self.spark, input_config)
        summary_stats, profiles = self.profiler.profile(
            df,
            options={
                "sample_fraction": profiler_config.sample_fraction,
                "sample_seed": profiler_config.sample_seed,
                "limit": profiler_config.limit,
                "filter": profiler_config.filter,
            },
        )
        checks = self.generator.generate_dq_rules(profiles)  # use default criticality level "error"
        logger.info(f"Using options: \n{profiler_config}")
        logger.info(f"Generated checks: \n{checks}")
        logger.info(f"Generated summary statistics: \n{summary_stats}")

        storage_config = InstallationChecksStorageConfig(
            run_config_name=run_config_name,
            assume_user=True,
            product_name=product,
            install_folder=install_folder,
        )
        self.save(checks, summary_stats, storage_config, profiler_config.summary_stats_file)

    def run_for_patterns(
        self,
        patterns: list[str],
        exclude_patterns: list[str],
        profiler_config: ProfilerConfig,
        checks_location: str,
        install_folder: str,
        product: str,
        max_parallelism: int,
    ) -> None:
        """
        Run the DQX profiler for the given table patterns and save the generated checks and profile summary stats.

        Args:
            patterns: List of table patterns to profile (e.g. ["catalog.schema.table*"]).
            exclude_patterns: List of table patterns to exclude from profiling (e.g. ["*output", "*quarantine"]).
            profiler_config: Profiler configuration.
            checks_location: Delta table to save the generated checks, otherwise an absolute directory.
            install_folder: Installation folder path.
            product: Product name for the installation.
            max_parallelism: Maximum number of parallel threads to use for profiling.
        """
        options = [
            {
                "table": "*",  # Matches all tables
                "options": {
                    "sample_fraction": profiler_config.sample_fraction,
                    "sample_seed": profiler_config.sample_seed,
                    "limit": profiler_config.limit,
                },
            }
        ]
        logger.info(f"Using options: \n{options}")

        # Include tables matching the patterns, but skip existing output and quarantine tables.
        results = self.profiler.profile_tables_for_patterns(
            patterns=patterns, exclude_patterns=exclude_patterns, options=options, max_parallelism=max_parallelism
        )

        for table, (summary_stats, profiles) in results.items():
            checks = self.generator.generate_dq_rules(profiles)  # use default criticality level "error"
            logger.info(f"Generated checks: \n{checks}")
            logger.info(f"Generated summary statistics: \n{summary_stats}")

            storage_config = InstallationChecksStorageConfig(
                location=(
                    checks_location
                    if is_table_location(checks_location)
                    else f"{safe_strip_file_from_path(checks_location)}/{table}.yml"
                ),
                overwrite_location=True,
                product_name=product,
                install_folder=install_folder,
                run_config_name=table,
            )
            self.save(checks, summary_stats, storage_config, profiler_config.summary_stats_file)

    def save(
        self,
        checks: list[dict],
        summary_stats: dict[str, Any],
        storage_config: BaseChecksStorageConfig,
        profile_summary_stats_file: str,
    ) -> None:
        """
        Save the generated checks and profile summary statistics to the specified files.

        Args:
            checks: The generated checks.
            summary_stats: The profile summary statistics.
            storage_config: Configuration for where to save the checks.
            profile_summary_stats_file: The file to save the profile summary statistics to.
        """
        self.dq_engine.save_checks(checks, storage_config)
        self._save_summary_stats(profile_summary_stats_file, summary_stats)

    def _save_summary_stats(self, profile_summary_stats_file: str, summary_stats: dict[str, Any]) -> None:
        install_folder = self.installation.install_folder()
        summary_stats_file = f"{install_folder}/{profile_summary_stats_file}"

        logger.info(f"Uploading profile summary stats to {summary_stats_file}")
        content = yaml.safe_dump(summary_stats).encode("utf-8")
        self.ws.workspace.upload(summary_stats_file, content, format=ImportFormat.AUTO, overwrite=True)
