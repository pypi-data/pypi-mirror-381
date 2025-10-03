"""
Parser for 10X Genomics VDJ sequencing data.

Handles TSV files from 10X Genomics VDJ analysis with
cell barcode grouping and chain pairing functionality.
"""

import json
from pathlib import Path
from typing import Union, List, Optional, Dict, Any
import pandas as pd
import polars as pl
from itertools import product

from .base_parser import BaseParser, ParserConfig
from .utils_enhanced import standardize_airr_data


class TenXParser(BaseParser):
    """
    Parser for 10X Genomics VDJ sequencing files.

    Handles the specific format used by 10X Genomics Cell Ranger
    VDJ analysis pipeline, including cell barcode grouping and
    alpha/beta chain pairing.
    """

    def __init__(self, config: Optional[ParserConfig] = None):
        """Initialize 10X parser."""
        super().__init__(config)
        self.platform = "tenx"
        self.supported_extensions.extend([".json", ".json.gz"])

    def parse_file(self, file_path: Path) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Parse a single 10X VDJ file.

        Args:
            file_path: Path to the 10X file (TSV or JSON)

        Returns:
            Parsed data frame
        """
        repertoire_id = self.extract_repertoire_id(file_path)

        if file_path.suffix.lower() in [".json", ".gz"]:
            data = self._parse_json_file(file_path)
        else:
            data = self._parse_tsv_file(file_path)

        # Add repertoire_id
        if isinstance(data, pl.DataFrame):
            data = data.with_columns(pl.lit(repertoire_id).alias("repertoire_id"))
        else:
            data["repertoire_id"] = repertoire_id

        return data

    def _parse_tsv_file(self, file_path: Path) -> Union[pd.DataFrame, pl.DataFrame]:
        """Parse 10X TSV file format."""
        delimiter = self.detect_delimiter(file_path)

        try:
            if self.config.return_type == "polars":
                data = pl.read_csv(
                    file_path,
                    separator=delimiter,
                    null_values=["", "NA", "N/A", "None"],
                    try_parse_dates=False,
                    ignore_errors=True
                )
            else:
                data = pd.read_csv(
                    file_path,
                    sep=delimiter,
                    na_values=["", "NA", "N/A", "None"],
                    low_memory=False,
                    dtype=str
                )
        except Exception as e:
            raise ValueError(f"Failed to parse TSV file {file_path}: {str(e)}")

        return data

    def _parse_json_file(self, file_path: Path) -> Union[pd.DataFrame, pl.DataFrame]:
        """Parse 10X JSON file format (e.g., all_contig_annotations.json)."""
        try:
            with open(file_path, 'r') as f:
                data_list = [json.loads(line) for line in f]

            if self.config.return_type == "polars":
                data = pl.DataFrame(data_list)
            else:
                data = pd.DataFrame(data_list)

        except Exception as e:
            raise ValueError(f"Failed to parse JSON file {file_path}: {str(e)}")

        return data

    def standardize_columns(
        self,
        data: Union[pd.DataFrame, pl.DataFrame]
    ) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Standardize 10X columns to AIRR format.

        Args:
            data: Raw 10X data

        Returns:
            Data with standardized column names
        """
        repertoire_id = None
        if isinstance(data, pl.DataFrame):
            if "repertoire_id" in data.columns:
                repertoire_id = data["repertoire_id"][0]
        else:
            if "repertoire_id" in data.columns:
                repertoire_id = data["repertoire_id"].iloc[0]

        # Apply enhanced AIRR standardization
        standardized = self.standardize_to_airr(data, platform="tenx", repertoire_id=repertoire_id)

        # Apply 10X-specific processing if needed
        if self._has_barcode_data(standardized):
            standardized = self._process_barcode_groups(standardized)

        return standardized

    def _has_barcode_data(self, data: Union[pd.DataFrame, pl.DataFrame]) -> bool:
        """Check if data contains cell barcode information."""
        barcode_cols = ["barcode", "cell_id", "clonotype_id"]
        if isinstance(data, pl.DataFrame):
            return any(col in data.columns for col in barcode_cols)
        else:
            return any(col in data.columns for col in barcode_cols)

    def _process_barcode_groups(
        self,
        data: Union[pd.DataFrame, pl.DataFrame]
    ) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Process cell barcode groups to pair alpha and beta chains.

        Args:
            data: Standardized 10X data with barcodes

        Returns:
            Data with paired chains
        """
        if isinstance(data, pl.DataFrame):
            return self._process_barcode_groups_polars(data)
        else:
            return self._process_barcode_groups_pandas(data)

    def _process_barcode_groups_pandas(self, data: pd.DataFrame) -> pd.DataFrame:
        """Process barcode groups using pandas."""
        if "barcode" not in data.columns and "cell_id" not in data.columns:
            return data

        barcode_col = "barcode" if "barcode" in data.columns else "cell_id"
        chain_col = "chain" if "chain" in data.columns else "locus"

        if chain_col not in data.columns:
            return data

        formatted_contigs = []

        for barcode, group in data.groupby(barcode_col):
            # Get TRA and TRB sequences
            tra_seqs = group[group[chain_col].str.contains("TRA|TCR_Alpha", na=False)]
            trb_seqs = group[group[chain_col].str.contains("TRB|TCR_Beta", na=False)]

            # Create all combinations of alpha and beta chains
            if not tra_seqs.empty and not trb_seqs.empty:
                for idx, (tra_idx, tra_row) in enumerate(tra_seqs.iterrows(), 1):
                    for jdx, (trb_idx, trb_row) in enumerate(trb_seqs.iterrows(), 1):
                        combined_row = self._format_combined_tcell(
                            barcode, f"{idx}_{jdx}", tra_row, trb_row
                        )
                        formatted_contigs.append(combined_row)
            elif not tra_seqs.empty:
                for idx, (tra_idx, tra_row) in enumerate(tra_seqs.iterrows(), 1):
                    combined_row = self._format_combined_tcell(
                        barcode, idx, tra_row, None
                    )
                    formatted_contigs.append(combined_row)
            elif not trb_seqs.empty:
                for idx, (trb_idx, trb_row) in enumerate(trb_seqs.iterrows(), 1):
                    combined_row = self._format_combined_tcell(
                        barcode, idx, None, trb_row
                    )
                    formatted_contigs.append(combined_row)

        if formatted_contigs:
            return pd.DataFrame(formatted_contigs)
        else:
            return data

    def _process_barcode_groups_polars(self, data: pl.DataFrame) -> pl.DataFrame:
        """Process barcode groups using polars."""
        # For now, convert to pandas for complex grouping operations
        pandas_data = data.to_pandas()
        processed = self._process_barcode_groups_pandas(pandas_data)
        return pl.from_pandas(processed)

    def _format_combined_tcell(
        self,
        barcode: str,
        index: Union[str, int],
        tra_row: Optional[pd.Series],
        trb_row: Optional[pd.Series]
    ) -> Dict[str, Any]:
        """
        Format combined T-cell data from alpha and beta chains.

        Args:
            barcode: Cell barcode
            index: Index for this combination
            tra_row: TRA chain data
            trb_row: TRB chain data

        Returns:
            Combined data dictionary
        """
        result = {
            "sequence_id": f"{barcode}_{index}",
            "cell_id": barcode,
            "repertoire_id": tra_row.get("repertoire_id", "") if tra_row is not None else (
                trb_row.get("repertoire_id", "") if trb_row is not None else ""
            )
        }

        # Add TRA information
        if tra_row is not None:
            result.update({
                "tra_junction_aa": tra_row.get("junction_aa", ""),
                "tra_junction": tra_row.get("junction", ""),
                "tra_v_call": tra_row.get("v_call", ""),
                "tra_d_call": tra_row.get("d_call", ""),
                "tra_j_call": tra_row.get("j_call", ""),
            })

        # Add TRB information
        if trb_row is not None:
            result.update({
                "trb_junction_aa": trb_row.get("junction_aa", ""),
                "trb_junction": trb_row.get("junction", ""),
                "trb_v_call": trb_row.get("v_call", ""),
                "trb_d_call": trb_row.get("d_call", ""),
                "trb_j_call": trb_row.get("j_call", ""),
            })

        # Create combined sequence field
        tra_seq = result.get("tra_junction_aa", "")
        trb_seq = result.get("trb_junction_aa", "")
        combined_seq = " ".join([x for x in [tra_seq, trb_seq] if x])
        result["junction_aa"] = combined_seq + ";" if combined_seq else ""

        # Set other standard fields
        result.update({
            "productive": True,  # Assume productive for 10X data
            "locus": "TCR",
            "sequence": "",
            "duplicate_count": 1,
        })

        return result


def read_10x(
    path: Union[str, Path, List[str]],
    recursive: bool = False,
    collapse_chains: bool = True,
    parallel: bool = True,
    threads: Optional[int] = None,
    return_type: str = "polars",
    validate_airr: bool = True,
    enhanced_mappings: bool = True
) -> Union[pd.DataFrame, pl.DataFrame]:
    """
    Read 10X Genomics VDJ sequencing files.

    This function imports files from 10X Genomics Cell Ranger VDJ analysis
    and standardizes them to AIRR format. Can handle both TSV and JSON formats.

    Args:
        path: Path to directory containing files, single file, or list of files
        recursive: Search recursively for files in subdirectories
        collapse_chains: Combine alpha and beta chains for T-cell data
        parallel: Process files in parallel
        threads: Number of threads to use
        return_type: Return format ("polars", "pandas")
        validate_airr: Enable AIRR schema validation
        enhanced_mappings: Use comprehensive column mappings

    Returns:
        Parsed and standardized data frame

    Examples:
        >>> # Read 10X VDJ data directory
        >>> data = read_10x("data/10x_vdj/")

        >>> # Read specific file
        >>> data = read_10x("filtered_contig_annotations.csv")

        >>> # Read without chain collapsing
        >>> data = read_10x("data/", collapse_chains=False)
    """
    # Create parser configuration
    config = ParserConfig(
        parallel=parallel,
        threads=threads,
        return_type=return_type,
        validate_airr=validate_airr,
        enhanced_mappings=enhanced_mappings
    )

    # Initialize parser and process data
    parser = TenXParser(config)
    return parser.parse(path, recursive=recursive)