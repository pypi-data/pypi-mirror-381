"""
Parser for Adaptive Biotechnologies ImmunoSEQ data.

Handles TSV files exported from ImmunoSEQ analyzer with
platform-specific column mappings and optimizations.
"""

import os
from pathlib import Path
from typing import Union, List, Optional
import pandas as pd
import polars as pl

from .base_parser import BaseParser, ParserConfig
from .utils_enhanced import standardize_airr_data


class ImmunoSeqParser(BaseParser):
    """
    Parser for Adaptive ImmunoSEQ TSV files.

    Handles the specific column format and naming conventions
    used by Adaptive Biotechnologies ImmunoSEQ platform.
    """

    def __init__(self, config: Optional[ParserConfig] = None):
        """Initialize ImmunoSeq parser."""
        super().__init__(config)
        # Use auto-detection to support both ImmunoSEQ and BGI formats
        self.platform = "auto"

    def parse_file(self, file_path: Path) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Parse a single ImmunoSEQ TSV file with optimized lazy loading.

        Args:
            file_path: Path to the TSV file

        Returns:
            Parsed data frame
        """
        delimiter = self.detect_delimiter(file_path)
        repertoire_id = self.extract_repertoire_id(file_path)

        try:
            # Use polars for efficient lazy loading with streaming
            # Note: streaming_mode only works in sequential processing (not parallel)
            if self.config.return_type == "polars" and self.config.streaming_mode and not self.config.parallel:
                # Lazy loading with scan_csv for large files (sequential only)
                # We need to read as strings to match non-streaming behavior
                # Since scan_csv doesn't support infer_schema_length=0, we use read_csv with streaming collect
                data = pl.read_csv(
                    file_path,
                    separator=delimiter,
                    null_values=["", "NA", "N/A"],
                    try_parse_dates=False,
                    low_memory=True,
                    ignore_errors=True,
                    infer_schema_length=0  # Read all as strings for consistency
                ).with_columns(
                    pl.lit(repertoire_id).alias("repertoire_id")
                )

            elif self.config.return_type == "polars":
                # Direct polars read for smaller files
                # Read all as strings first to avoid type conflicts during concat
                data = pl.read_csv(
                    file_path,
                    separator=delimiter,
                    null_values=["", "NA", "N/A"],
                    try_parse_dates=False,
                    low_memory=True,
                    ignore_errors=True,
                    infer_schema_length=0  # Read all as strings
                ).with_columns(
                    pl.lit(repertoire_id).alias("repertoire_id")
                )

            else:
                # Pandas fallback
                data = pd.read_csv(
                    file_path,
                    sep=delimiter,
                    na_values=["", "NA", "N/A"],
                    low_memory=False,
                    dtype=str
                )

                # Handle duplicate column names
                if data.columns.duplicated().any():
                    data.columns = pd.io.common.dedup_names(data.columns, is_potential_multiindex=False)

                data["repertoire_id"] = repertoire_id

        except Exception as e:
            raise ValueError(f"Failed to parse {file_path}: {str(e)}")

        return data

    def standardize_columns(
        self,
        data: Union[pd.DataFrame, pl.DataFrame]
    ) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Standardize ImmunoSEQ columns to AIRR format.

        Note: This method is kept for compatibility but the enhanced
        standardization is now handled in the base class.

        Args:
            data: Raw ImmunoSEQ data

        Returns:
            Data with standardized column names
        """
        # Extract repertoire_id if present
        repertoire_id = None
        if isinstance(data, pl.DataFrame):
            if "repertoire_id" in data.columns:
                repertoire_id = data["repertoire_id"][0]
        else:
            if "repertoire_id" in data.columns:
                repertoire_id = data["repertoire_id"].iloc[0]

        # Use enhanced standardization with auto-detection
        # This allows the parser to handle both ImmunoSEQ and BGI files
        return self.standardize_to_airr(data, platform="auto", repertoire_id=repertoire_id)

    def _detect_immunoseq_version(self, data: Union[pd.DataFrame, pl.DataFrame]) -> str:
        """
        Detect ImmunoSEQ file version based on column names.

        Args:
            data: Parsed data frame

        Returns:
            Version identifier
        """
        columns = data.columns if isinstance(data, pd.DataFrame) else data.columns

        # Check for version-specific columns
        if "aminoAcid" in columns:
            return "v2"
        elif "junction_aa" in columns:
            return "v3"
        else:
            return "unknown"


def read_immunoseq(
    path: Union[str, Path, List[str]],
    recursive: bool = False,
    parallel: bool = True,
    threads: Optional[int] = None,
    chunk_size: Optional[int] = None,
    max_memory_gb: float = 8.0,
    streaming_mode: bool = False,
    temp_dir: Optional[Union[str, Path]] = None,
    progress_detail: str = "basic",
    return_type: str = "polars",
    use_arrow: Union[str, bool] = "auto",
    validate_airr: bool = True,
    enhanced_mappings: bool = True,
    verbose: bool = False
) -> Union[pd.DataFrame, pl.DataFrame, pl.LazyFrame]:
    """
    Read Adaptive ImmunoSEQ files.

    This function imports tab-separated value (.tsv) files exported by the
    Adaptive Biotechnologies ImmunoSEQ analyzer and standardizes them to
    AIRR format.

    Args:
        path: Path to directory containing TSV files, single file, or list of files
        recursive: Search recursively for files in subdirectories
        parallel: Process files in parallel
        threads: Number of threads to use (default: auto-detect)
        chunk_size: Number of files to process in each chunk for memory efficiency
        max_memory_gb: Maximum memory to use in GB
        streaming_mode: Process extremely large files in streaming chunks.
            **IMPORTANT**: When True, returns a Polars LazyFrame instead of DataFrame
            to avoid loading the entire dataset into memory. Use .collect() to
            materialize, or work with lazy operations.
        temp_dir: Temporary directory for cache files (default: system temp)
        progress_detail: Level of progress reporting ("none", "basic", "detailed")
        return_type: Return format ("polars", "pandas")
        use_arrow: Use Apache Arrow for large datasets ("auto", "always", "never")
        validate_airr: Enable AIRR schema validation
        enhanced_mappings: Use comprehensive column mappings
        verbose: Show detailed progress messages (default: False)

    Returns:
        - DataFrame (polars or pandas) if streaming_mode=False
        - LazyFrame (polars) if streaming_mode=True (use .collect() to load)

    Examples:
        >>> # Read all TSV files in a directory
        >>> data = read_immunoseq("data/immunoseq/")

        >>> # Read specific files
        >>> data = read_immunoseq(["sample1.tsv", "sample2.tsv"])

        >>> # Read with custom settings
        >>> data = read_immunoseq(
        ...     "data/",
        ...     parallel=True,
        ...     threads=4,
        ...     return_type="pandas"
        ... )

        >>> # For very large datasets (100+ GB), use streaming mode
        >>> # This returns a LazyFrame to avoid loading into memory
        >>> lazy_data = read_immunoseq(
        ...     "data/large_dataset/",
        ...     streaming_mode=True,
        ...     chunk_size=3,
        ...     parallel=False,
        ...     verbose=False
        ... )
        >>> # Work with lazy operations - only loads what you need
        >>> result = lazy_data.filter(pl.col("duplicate_count") > 10).collect()
        >>> # Or collect specific columns only
        >>> counts = lazy_data.select(["repertoire_id", "duplicate_count"]).collect()

        >>> # The Arrow file is saved in temp directory and shown in output
        >>> # You can also scan it directly later:
        >>> lazy_data = pl.scan_ipc("/tmp/lymphoseq_output_abc12345.arrow")
    """
    # Create parser configuration
    config = ParserConfig(
        parallel=parallel,
        threads=threads,
        chunk_size=chunk_size,
        max_memory_gb=max_memory_gb,
        streaming_mode=streaming_mode,
        temp_dir=temp_dir,
        progress_detail=progress_detail,
        return_type=return_type,
        use_arrow=use_arrow,
        validate_airr=validate_airr,
        enhanced_mappings=enhanced_mappings,
        verbose=verbose
    )

    # Initialize parser and process data
    parser = ImmunoSeqParser(config)
    return parser.parse(path, recursive=recursive)