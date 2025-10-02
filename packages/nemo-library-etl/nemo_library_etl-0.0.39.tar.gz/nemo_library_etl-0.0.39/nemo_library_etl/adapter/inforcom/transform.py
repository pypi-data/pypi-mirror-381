"""
InforCOM ETL Transform Module.

This module handles the transformation phase of the InforCOM ETL pipeline.
It processes the extracted data, applies business rules, data cleaning, and formatting
to prepare the data for loading into the target system.

The transformation process typically includes:
1. Data validation and quality checks
2. Data type conversions and formatting
3. Business rule application
4. Data enrichment and calculated fields
5. Data structure normalization
6. Comprehensive logging throughout the process

Classes:
    InforCOMTransform: Main class handling InforCOM data transformation.
"""

from prefect import get_run_logger
from nemo_library_etl.adapter._utils.db_handler import ETLDuckDBHandler
from nemo_library_etl.adapter.inforcom.config_models import PipelineInforCOM
from nemo_library_etl.adapter._utils.enums import ETLAdapter, ETLStep
from nemo_library_etl.adapter._utils.file_handler import ETLFileHandler
from nemo_library import NemoLibrary
import pandas as pd


class InforCOMTransform:
    """
    Handles transformation of extracted InforCOM data.

    This class manages the transformation phase of the InforCOM ETL pipeline,
    providing methods to process, clean, and format the extracted data for loading
    into the target system.

    The transformer:
    - Uses NemoLibrary for core functionality and configuration
    - Integrates with Prefect logging for pipeline visibility
    - Applies business rules and data validation
    - Handles data type conversions and formatting
    - Provides data enrichment and calculated fields
    - Ensures data quality and consistency

    Attributes:
        nl (NemoLibrary): Core Nemo library instance for system integration.
        config: Configuration object from the Nemo library.
        logger: Prefect logger for pipeline execution tracking.
        cfg (PipelineInforCOM): Pipeline configuration with transformation settings.
    """

    def __init__(self, cfg: PipelineInforCOM):
        """
        Initialize the InforCOMTransform instance.

        Sets up the transformer with the necessary library instances, configuration,
        and logging capabilities for the transformation process.

        Args:
            cfg (PipelineInforCOM): Pipeline configuration object containing
                                                          transformation settings and rules.
        """
        self.nl = NemoLibrary()
        self.config = self.nl.config
        self.logger = get_run_logger()
        self.cfg = cfg
        self.db = None

        super().__init__()

    def transform(self) -> None:
        """
        Execute the main transformation process for InforCOM data.

        This method orchestrates the complete transformation process by:
        1. Loading extracted data from the previous ETL phase
        2. Applying data validation and quality checks
        3. Performing data type conversions and formatting
        4. Applying business rules and logic
        5. Creating calculated fields and data enrichment
        6. Ensuring data consistency and integrity
        7. Preparing data for the loading phase

        The method provides detailed logging for monitoring and debugging purposes
        and handles errors gracefully to ensure pipeline stability.

        Note:
            The actual transformation logic needs to be implemented based on
            the specific InforCOM system requirements and business rules.
        """
        self.logger.info("Transforming all InforCOM objects")

        with ETLDuckDBHandler(threads=8) as self.db:
            
            # load all extracted data into duckdb
            self.load_local_database()
            
            # do transformation on database level here
            
            # dump all transformed data back to jsonl
            fh = ETLFileHandler()
            for table, model in self.cfg.extract.tables.items():
                if model.active is False:
                    self.logger.info(f"Skipping inactive table: {table}")
                    continue

                self.logger.info(f"Dumping transformed table: {table}")

                out_path, total = self.db.export_table(
                    table_name=str(table),
                    fh=fh,
                    adapter=ETLAdapter.INFORCOM,
                    step=ETLStep.TRANSFORM,
                    entity=table,
                    filename=None,            # let FileHandler derive filename from entity
                    substep=None,
                    gzip_enabled=True,        # produce .jsonl.gz
                    order_by=None,            # deterministic output
                    chunk_rows=100_000,
                )
                self.logger.info(f"Export complete: {out_path} ({total} rows)")

    def load_local_database(self) -> None:
        self.logger.info("Loading all InforCOM objects into local database")

        for table, model in self.cfg.extract.tables.items():
            if model.active is False:
                self.logger.info(f"Skipping inactive table: {table}")
                continue

            self.logger.info(f"Loading table: {table}")

            # Example: enforce types for a few known columns (optional)
            cast_map = getattr(model, "duckdb_casts", None)  # e.g., {"id": "BIGINT", "created_at": "TIMESTAMP"}

            self.db.ingest_jsonl(
                adapter=ETLAdapter.INFORCOM,
                step=ETLStep.EXTRACT,
                entity=table,
                ignore_nonexistent=True,
                create_mode="replace",       # or "append"
                table_name=str(table),       # keep your original table name
                add_metadata=True,           # adds _source_path & _ingested_at
                cast_map=cast_map,
            )
            