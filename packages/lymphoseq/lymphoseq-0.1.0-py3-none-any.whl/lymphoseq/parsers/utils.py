"""
Utility functions for AIRR-seq data parsing and standardization.

Adapted from quest/parsers patterns for LymphoSeq compatibility.
"""

import re
import pandas as pd
import polars as pl
from typing import Dict, List, Union, Optional, Any
from pathlib import Path


# AIRR standard column mappings
AIRR_STANDARD_COLUMNS = {
    "sequence_id": "sequence_id",
    "sequence": "sequence",
    "sequence_aa": "sequence_aa",
    "productive": "productive",
    "locus": "locus",
    "v_call": "v_call",
    "d_call": "d_call",
    "j_call": "j_call",
    "c_call": "c_call",
    "junction": "junction",
    "junction_aa": "junction_aa",
    "junction_length": "junction_length",
    "duplicate_count": "duplicate_count",
    "duplicate_frequency": "duplicate_frequency",
    "repertoire_id": "repertoire_id",
}

# Common column name mappings from different platforms
COLUMN_MAPPINGS = {
    "immunoseq": {
        "nucleotide": "sequence",
        "aminoAcid": "junction_aa",
        "count (templates/reads)": "duplicate_count",
        "frequencyCount (%)": "duplicate_frequency",
        "cdr3Length": "junction_length",
        "vGeneName": "v_call",
        "dGeneName": "d_call",
        "jGeneName": "j_call",
        "vFamilyName": "v_family",
        "dFamilyName": "d_family",
        "jFamilyName": "j_family",
        "sequenceStatus": "productive",
        "cloneResolved": "productive",
        "frame_type": "vj_in_frame",
    },
    "bgi": {
        # BGI column names with special characters
        "nucleotide(CDR3 in lowercase)": "junction",
        "aminoAcid(CDR3 in lowercase)": "junction_aa",
        "cloneCount": "duplicate_count",
        "clonefrequency (%)": "duplicate_frequency",
        "CDR3Length": "junction_length",
        "vGene": "v_call",
        "dGene": "d_call",
        "jGene": "j_call",
        "vDeletion": "v_deletion",
        "d5Deletion": "d5_deletion",
        "d3Deletion": "d3_deletion",
        "jDeletion": "j_deletion",
        "vdInsertion": "vd_insertion",
        "djInsertion": "dj_insertion",
        "vjInsertion": "vj_insertion",
        "fuction": "productive",  # Note: BGI has typo "fuction" instead of "function"
    },
    "mixcr": {
        "aaSeqCDR3": "junction_aa",
        "nSeqCDR3": "junction",
        "allVHitsWithScore": "v_call",
        "allDHitsWithScore": "d_call",
        "allJHitsWithScore": "j_call",
        "cloneCount": "duplicate_count",
        "cloneFraction": "duplicate_frequency",
    },
    "tenx": {
        "cdr3": "junction_aa",
        "cdr3_nt": "junction",
        "v_gene": "v_call",
        "d_gene": "d_call",
        "j_gene": "j_call",
        "reads": "duplicate_count",
        "umis": "duplicate_count",
        "raw_clonotype_id": "clone_id",
        "barcode": "cell_id",
    }
}


def standardize_airr_data(
    data: Union[pd.DataFrame, pl.DataFrame],
    platform: str = "auto",
    repertoire_id: Optional[str] = None
) -> Union[pd.DataFrame, pl.DataFrame]:
    """
    Standardize data to AIRR format.

    Args:
        data: Input data frame
        platform: Platform type for column mapping
        repertoire_id: Repertoire identifier to add

    Returns:
        Standardized data frame
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Convert to pandas for processing if needed
    if is_polars:
        df = data.to_pandas()
    else:
        df = data.copy()

    # Auto-detect platform if not specified
    if platform == "auto":
        platform = detect_platform(df.columns.tolist())

    # Apply column mappings
    if platform in COLUMN_MAPPINGS:
        column_mapping = COLUMN_MAPPINGS[platform]
        df = df.rename(columns=column_mapping)

    # Platform-specific transformations
    if platform == "bgi":
        # BGI uses percentages, convert to fractions (0-1)
        if "duplicate_frequency" in df.columns:
            df["duplicate_frequency"] = df["duplicate_frequency"] / 100.0

    # Add standard columns with defaults
    for col in AIRR_STANDARD_COLUMNS.values():
        if col not in df.columns:
            if col == "productive":
                df[col] = True  # Default to productive
            elif col == "repertoire_id" and repertoire_id:
                df[col] = repertoire_id
            else:
                df[col] = ""

    # Standardize productive column
    if "productive" in df.columns:
        df["productive"] = standardize_productive_column(df["productive"])

    # Clean and validate data
    df = clean_gene_calls(df)
    df = validate_sequences(df)

    # Reorder columns to standard order
    available_cols = [col for col in AIRR_STANDARD_COLUMNS.values() if col in df.columns]
    other_cols = [col for col in df.columns if col not in available_cols]
    df = df[available_cols + other_cols]

    return pl.from_pandas(df) if is_polars else df


def detect_platform(columns: List[str]) -> str:
    """
    Auto-detect the platform based on column names.

    Args:
        columns: List of column names

    Returns:
        Detected platform name
    """
    columns_lower = [col.lower() for col in columns]

    # Check for platform-specific column patterns
    # Check BGI first (before immunoseq) since both have "nucleotide" but BGI has parentheses
    if any("nucleotide(cdr3" in col or "aminoacid(cdr3" in col for col in columns_lower):
        return "bgi"
    elif any("aminoacid" in col or ("nucleotide" in col and "count (templates" in " ".join(columns_lower)) for col in columns_lower):
        return "immunoseq"
    elif any("aaseqcdr3" in col or "nseqcdr3" in col for col in columns_lower):
        return "mixcr"
    elif any("barcode" in col or "contig_id" in col for col in columns_lower):
        return "tenx"
    else:
        return "generic"


def standardize_productive_column(series: Union[pd.Series, pl.Series]) -> Union[pd.Series, pl.Series]:
    """
    Standardize productive column to boolean values.

    Args:
        series: Series containing productive status

    Returns:
        Boolean series
    """
    if isinstance(series, pl.Series):
        return series.map_elements(lambda x: _convert_productive_value(x))
    else:
        return series.apply(_convert_productive_value)


def _convert_productive_value(value: Any) -> bool:
    """Convert various productive value formats to boolean."""
    if pd.isna(value) or value == "":
        return False

    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        value = value.lower().strip()
        # BGI format: "in-frame" is productive, "out-of-frame" is not
        if value.startswith("in-frame") or value.startswith("in"):
            return True
        elif value.startswith("out-of-frame") or value.startswith("out"):
            return False
        # Standard formats
        elif value in ["true", "yes", "productive", "1"]:
            return True
        elif value in ["false", "no", "unproductive", "0", "stop"]:
            return False

    if isinstance(value, (int, float)):
        return bool(value)

    return False


def clean_gene_calls(df: Union[pd.DataFrame, pl.DataFrame]) -> Union[pd.DataFrame, pl.DataFrame]:
    """
    Clean and standardize gene call annotations.

    Args:
        df: Data frame with gene call columns

    Returns:
        Data frame with cleaned gene calls
    """
    gene_columns = ["v_call", "d_call", "j_call", "c_call"]

    for col in gene_columns:
        if col in df.columns:
            if isinstance(df, pl.DataFrame):
                df = df.with_columns(
                    pl.col(col).map_elements(lambda x: clean_single_gene_call(x)).alias(col)
                )
            else:
                df[col] = df[col].apply(clean_single_gene_call)

    return df


def clean_single_gene_call(gene_call: Any) -> str:
    """
    Clean a single gene call annotation.

    Args:
        gene_call: Gene call string or value

    Returns:
        Cleaned gene call string
    """
    if pd.isna(gene_call) or gene_call == "":
        return ""

    gene_call = str(gene_call).strip()

    # Remove common prefixes and clean up
    gene_call = re.sub(r"^(TCRBV|TCRBD|TCRBJ|TRAV|TRAJ|IGHV|IGHD|IGHJ|IGH|TRB|TRA)", "", gene_call)

    # Extract the main gene name (first part before any additional annotations)
    if "," in gene_call:
        gene_call = gene_call.split(",")[0]
    if ";" in gene_call:
        gene_call = gene_call.split(";")[0]
    if "(" in gene_call:
        gene_call = gene_call.split("(")[0]

    return gene_call.strip()


def validate_sequences(df: Union[pd.DataFrame, pl.DataFrame]) -> Union[pd.DataFrame, pl.DataFrame]:
    """
    Validate and clean sequence data.

    Args:
        df: Data frame with sequence columns

    Returns:
        Data frame with validated sequences
    """
    # Validate junction_aa sequences (amino acid)
    if "junction_aa" in df.columns:
        if isinstance(df, pl.DataFrame):
            df = df.with_columns(
                pl.col("junction_aa").map_elements(lambda x: validate_aa_sequence(x)).alias("junction_aa")
            )
        else:
            df["junction_aa"] = df["junction_aa"].apply(validate_aa_sequence)

    # Validate junction sequences (nucleotide)
    if "junction" in df.columns:
        if isinstance(df, pl.DataFrame):
            df = df.with_columns(
                pl.col("junction").map_elements(lambda x: validate_nt_sequence(x)).alias("junction")
            )
        else:
            df["junction"] = df["junction"].apply(validate_nt_sequence)

    return df


def validate_aa_sequence(seq: Any) -> str:
    """
    Validate amino acid sequence.

    Args:
        seq: Sequence to validate

    Returns:
        Cleaned sequence or empty string if invalid
    """
    if pd.isna(seq) or seq == "":
        return ""

    seq = str(seq).upper().strip()

    # Remove non-amino acid characters
    valid_aa = re.sub(r"[^ACDEFGHIKLMNPQRSTVWY*]", "", seq)

    return valid_aa


def validate_nt_sequence(seq: Any) -> str:
    """
    Validate nucleotide sequence.

    Args:
        seq: Sequence to validate

    Returns:
        Cleaned sequence or empty string if invalid
    """
    if pd.isna(seq) or seq == "":
        return ""

    seq = str(seq).upper().strip()

    # Remove non-nucleotide characters
    valid_nt = re.sub(r"[^ATCGN]", "", seq)

    return valid_nt


def validate_airr_schema(df: Union[pd.DataFrame, pl.DataFrame]) -> Dict[str, Any]:
    """
    Validate data against AIRR schema requirements.

    Args:
        df: Data frame to validate

    Returns:
        Validation report dictionary
    """
    report = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "statistics": {}
    }

    # Check required columns
    required_columns = ["sequence_id", "productive", "locus", "v_call", "j_call"]
    missing_required = [col for col in required_columns if col not in df.columns]

    if missing_required:
        report["valid"] = False
        report["errors"].append(f"Missing required columns: {missing_required}")

    # Check data quality
    if isinstance(df, pl.DataFrame):
        total_rows = df.height
        empty_sequences = df.filter(pl.col("junction_aa") == "").height if "junction_aa" in df.columns else 0
    else:
        total_rows = len(df)
        empty_sequences = (df["junction_aa"] == "").sum() if "junction_aa" in df.columns else 0

    if empty_sequences > 0:
        report["warnings"].append(f"{empty_sequences} rows have empty junction_aa sequences")

    # Statistics
    report["statistics"] = {
        "total_rows": total_rows,
        "empty_sequences": empty_sequences,
        "columns": len(df.columns) if isinstance(df, pd.DataFrame) else len(df.columns),
    }

    return report


def get_memory_usage(df: Union[pd.DataFrame, pl.DataFrame]) -> float:
    """
    Get memory usage of data frame in GB.

    Args:
        df: Data frame to analyze

    Returns:
        Memory usage in GB
    """
    if isinstance(df, pl.DataFrame):
        return df.estimated_size("gb")
    else:
        return df.memory_usage(deep=True).sum() / (1024**3)