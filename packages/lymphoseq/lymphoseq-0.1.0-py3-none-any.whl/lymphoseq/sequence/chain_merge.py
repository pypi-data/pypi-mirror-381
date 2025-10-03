"""
Functions for merging paired alpha and beta chains from 10X Genomics data.

Provides functionality to combine TRA and TRB chains from single-cell data
into merged sequences that can be used with bulk analysis functions.
"""

from typing import Union, Optional, Literal
import pandas as pd
import polars as pl


def merge_chains(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_id: Optional[str] = None,
    separator: str = ":",
    keep_chain_columns: bool = False,
    aggregate: bool = True,
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Merge alpha and beta chains from 10X data into combined sequences.

    This function takes 10X single-cell data with separate TRA and TRB chain
    information and creates merged junction and junction_aa sequences that can
    be used with bulk repertoire analysis functions.

    The function looks for columns like tra_junction_aa, trb_junction_aa,
    tra_junction, trb_junction and combines them into junction_aa and junction
    columns that are compatible with the rest of the package functions.

    Args:
        data: DataFrame containing 10X data with separate TRA and TRB columns.
              Expected columns include: tra_junction_aa, trb_junction_aa,
              tra_junction, trb_junction, and optionally tra_v_call, trb_v_call, etc.
        repertoire_id: Optional repertoire ID to filter. If None, processes all repertoires.
        separator: String to use for joining alpha and beta sequences (default: ":")
        keep_chain_columns: If True, keep the original tra_* and trb_* columns
        aggregate: If True, aggregate identical merged sequences and count them

    Returns:
        DataFrame with merged junction and junction_aa columns, compatible
        with bulk analysis functions like clonality(), diversity_metrics(), etc.

    Examples:
        >>> # Read 10X data
        >>> data_10x = read_10x("path/to/10x_data/")
        >>>
        >>> # Merge chains for bulk-style analysis
        >>> merged = merge_chains(data_10x)
        >>>
        >>> # Now use with any bulk analysis function
        >>> clonality_scores = clonality(merged)
        >>> diversity = diversity_metrics(merged)
        >>>
        >>> # Keep original chain columns
        >>> merged_full = merge_chains(data_10x, keep_chain_columns=True)
        >>>
        >>> # Custom separator
        >>> merged_custom = merge_chains(data_10x, separator=";")
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Check for empty data
    if (is_polars and len(data) == 0) or (not is_polars and data.empty):
        raise ValueError("Cannot merge chains: input data is empty")

    # Filter by repertoire_id if specified
    if repertoire_id is not None:
        if is_polars:
            data = data.filter(pl.col("repertoire_id") == repertoire_id)
        else:
            data = data[data["repertoire_id"] == repertoire_id].copy()

    # Check if this is 10X data with chain columns
    required_cols = ["tra_junction_aa", "trb_junction_aa"]
    if is_polars:
        has_chain_cols = all(col in data.columns for col in required_cols)
    else:
        has_chain_cols = all(col in data.columns for col in required_cols)

    if not has_chain_cols:
        raise ValueError(
            "Data does not appear to contain 10X chain columns. "
            f"Expected columns: {required_cols}. "
            f"Found columns: {data.columns[:10].to_list() if is_polars else list(data.columns[:10])}"
        )

    if is_polars:
        result = _merge_chains_polars(data, separator, keep_chain_columns, aggregate)
    else:
        result = _merge_chains_pandas(data, separator, keep_chain_columns, aggregate)

    return result


def _merge_chains_polars(
    data: pl.DataFrame,
    separator: str,
    keep_chain_columns: bool,
    aggregate: bool
) -> pl.DataFrame:
    """Merge chains using Polars operations."""

    # Create merged junction_aa and junction columns
    new_columns = [
        # Merge amino acid sequences
        pl.concat_str([
            pl.col("tra_junction_aa").fill_null(""),
            pl.col("trb_junction_aa").fill_null("")
        ], separator=separator).alias("junction_aa"),

        # Merge nucleotide sequences if available
        (
            pl.concat_str([
                pl.col("tra_junction").fill_null(""),
                pl.col("trb_junction").fill_null("")
            ], separator=separator)
            if "tra_junction" in data.columns and "trb_junction" in data.columns
            else pl.lit("")
        ).alias("junction"),

        # Create combined V gene calls
        (
            pl.concat_str([
                pl.col("tra_v_call").fill_null(""),
                pl.col("trb_v_call").fill_null("")
            ], separator=separator)
            if "tra_v_call" in data.columns and "trb_v_call" in data.columns
            else pl.lit("")
        ).alias("v_call"),

        # Create combined J gene calls
        (
            pl.concat_str([
                pl.col("tra_j_call").fill_null(""),
                pl.col("trb_j_call").fill_null("")
            ], separator=separator)
            if "tra_j_call" in data.columns and "trb_j_call" in data.columns
            else pl.lit("")
        ).alias("j_call"),
    ]

    # Add productive column if not present
    if "productive" not in data.columns:
        new_columns.append(pl.lit(True).alias("productive"))

    result = data.with_columns(new_columns)

    # Remove rows where both chains are empty
    result = result.filter(
        (pl.col("junction_aa") != separator) &
        (pl.col("junction_aa") != "") &
        (pl.col("junction_aa").is_not_null())
    )

    # Calculate junction lengths
    result = result.with_columns([
        pl.col("junction_aa").str.len_chars().alias("junction_aa_length"),
        (
            pl.col("junction").str.len_chars()
            if "junction" in result.columns
            else pl.lit(0)
        ).alias("junction_length")
    ])

    # Remove chain-specific columns if requested (before aggregation)
    chain_cols_to_keep = []
    if not keep_chain_columns:
        chain_cols = [col for col in result.columns if col.startswith(("tra_", "trb_"))]
        result = result.drop(chain_cols)
    else:
        chain_cols_to_keep = [col for col in result.columns if col.startswith(("tra_", "trb_"))]

    if aggregate:
        # Group by merged sequences and aggregate
        group_cols = ["junction_aa", "repertoire_id"]
        if "junction" in result.columns:
            group_cols.append("junction")

        agg_exprs = [
            pl.len().alias("duplicate_count"),
            pl.col("v_call").first(),
            pl.col("j_call").first(),
            pl.col("junction_aa_length").first(),
            pl.col("junction_length").first(),
        ]

        # Keep productive column if present
        if "productive" in result.columns:
            agg_exprs.append(pl.col("productive").first())

        # Keep chain columns if requested
        if keep_chain_columns:
            for col in chain_cols_to_keep:
                agg_exprs.append(pl.col(col).first())

        result = result.group_by(group_cols).agg(agg_exprs)

        # Calculate frequency
        total = result.select(pl.col("duplicate_count").sum()).item()
        result = result.with_columns(
            (pl.col("duplicate_count") / total).alias("duplicate_frequency")
        )
    else:
        # Add duplicate_count and frequency columns if not present
        if "duplicate_count" not in result.columns:
            result = result.with_columns(pl.lit(1).alias("duplicate_count"))

        if "duplicate_frequency" not in result.columns:
            total = len(result)
            result = result.with_columns(
                (pl.lit(1.0) / total).alias("duplicate_frequency")
            )

    return result


def _merge_chains_pandas(
    data: pd.DataFrame,
    separator: str,
    keep_chain_columns: bool,
    aggregate: bool
) -> pd.DataFrame:
    """Merge chains using Pandas operations."""

    result = data.copy()

    # Create merged junction_aa column
    result["junction_aa"] = (
        result["tra_junction_aa"].fillna("") + separator +
        result["trb_junction_aa"].fillna("")
    )

    # Create merged junction column if available
    if "tra_junction" in result.columns and "trb_junction" in result.columns:
        result["junction"] = (
            result["tra_junction"].fillna("") + separator +
            result["trb_junction"].fillna("")
        )
    else:
        result["junction"] = ""

    # Create combined V gene calls if available
    if "tra_v_call" in result.columns and "trb_v_call" in result.columns:
        result["v_call"] = (
            result["tra_v_call"].fillna("") + separator +
            result["trb_v_call"].fillna("")
        )
    else:
        result["v_call"] = ""

    # Create combined J gene calls if available
    if "tra_j_call" in result.columns and "trb_j_call" in result.columns:
        result["j_call"] = (
            result["tra_j_call"].fillna("") + separator +
            result["trb_j_call"].fillna("")
        )
    else:
        result["j_call"] = ""

    # Add productive column if not present
    if "productive" not in result.columns:
        result["productive"] = True

    # Remove rows where both chains are empty
    result = result[
        (result["junction_aa"] != separator) &
        (result["junction_aa"] != "") &
        (result["junction_aa"].notna())
    ].copy()

    # Calculate junction lengths
    result["junction_aa_length"] = result["junction_aa"].str.len()
    result["junction_length"] = result["junction"].str.len()

    # Identify chain columns to keep if requested
    chain_cols_to_keep = []
    if keep_chain_columns:
        chain_cols_to_keep = [col for col in result.columns if col.startswith(("tra_", "trb_"))]
    else:
        # Remove chain-specific columns if not keeping them
        chain_cols = [col for col in result.columns if col.startswith(("tra_", "trb_"))]
        result = result.drop(columns=chain_cols, errors="ignore")

    if aggregate:
        # Group by merged sequences and aggregate
        group_cols = ["junction_aa", "repertoire_id"]
        if "junction" in result.columns and result["junction"].notna().any():
            group_cols.append("junction")

        agg_dict = {
            "duplicate_count": ("junction_aa", "size"),
            "v_call": ("v_call", "first"),
            "j_call": ("j_call", "first"),
            "junction_aa_length": ("junction_aa_length", "first"),
            "junction_length": ("junction_length", "first"),
        }

        # Keep productive column if present
        if "productive" in result.columns:
            agg_dict["productive"] = ("productive", "first")

        # Keep chain columns if requested
        if keep_chain_columns:
            for col in chain_cols_to_keep:
                agg_dict[col] = (col, "first")

        result = result.groupby(group_cols, as_index=False).agg(**agg_dict)

        # Calculate frequency
        total = result["duplicate_count"].sum()
        result["duplicate_frequency"] = result["duplicate_count"] / total
    else:
        # Add duplicate_count and frequency columns if not present
        if "duplicate_count" not in result.columns:
            result["duplicate_count"] = 1

        if "duplicate_frequency" not in result.columns:
            total = len(result)
            result["duplicate_frequency"] = 1.0 / total

    return result


def split_chains(
    data: Union[pl.DataFrame, pd.DataFrame],
    separator: str = ":",
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Split merged junction sequences back into separate alpha and beta chains.

    This is the reverse operation of merge_chains(), taking merged sequences
    and splitting them back into tra_junction_aa and trb_junction_aa columns.

    Args:
        data: DataFrame with merged junction_aa column
        separator: String that was used to join sequences (default: ":")

    Returns:
        DataFrame with separated tra_junction_aa and trb_junction_aa columns

    Examples:
        >>> # Merge chains
        >>> merged = merge_chains(data_10x)
        >>>
        >>> # Split them back
        >>> split = split_chains(merged)
        >>>
        >>> # Check the split columns
        >>> print(split[["tra_junction_aa", "trb_junction_aa"]].head())
    """
    is_polars = isinstance(data, pl.DataFrame)

    if "junction_aa" not in data.columns:
        raise ValueError("Data must contain 'junction_aa' column")

    if is_polars:
        result = data.with_columns([
            pl.col("junction_aa").str.split(separator).list.get(0).alias("tra_junction_aa"),
            pl.col("junction_aa").str.split(separator).list.get(1).alias("trb_junction_aa"),
        ])

        # Also split junction if it exists
        if "junction" in data.columns:
            result = result.with_columns([
                pl.col("junction").str.split(separator).list.get(0).alias("tra_junction"),
                pl.col("junction").str.split(separator).list.get(1).alias("trb_junction"),
            ])

        # Split v_call and j_call if they exist
        if "v_call" in data.columns and separator in data["v_call"][0]:
            result = result.with_columns([
                pl.col("v_call").str.split(separator).list.get(0).alias("tra_v_call"),
                pl.col("v_call").str.split(separator).list.get(1).alias("trb_v_call"),
            ])

        if "j_call" in data.columns and separator in data["j_call"][0]:
            result = result.with_columns([
                pl.col("j_call").str.split(separator).list.get(0).alias("tra_j_call"),
                pl.col("j_call").str.split(separator).list.get(1).alias("trb_j_call"),
            ])
    else:
        result = data.copy()
        split_aa = result["junction_aa"].str.split(separator, expand=True)
        result["tra_junction_aa"] = split_aa[0] if len(split_aa.columns) > 0 else ""
        result["trb_junction_aa"] = split_aa[1] if len(split_aa.columns) > 1 else ""

        # Also split junction if it exists
        if "junction" in result.columns:
            split_nt = result["junction"].str.split(separator, expand=True)
            result["tra_junction"] = split_nt[0] if len(split_nt.columns) > 0 else ""
            result["trb_junction"] = split_nt[1] if len(split_nt.columns) > 1 else ""

        # Split v_call and j_call if they exist
        if "v_call" in result.columns and separator in str(result["v_call"].iloc[0]):
            split_v = result["v_call"].str.split(separator, expand=True)
            result["tra_v_call"] = split_v[0] if len(split_v.columns) > 0 else ""
            result["trb_v_call"] = split_v[1] if len(split_v.columns) > 1 else ""

        if "j_call" in result.columns and separator in str(result["j_call"].iloc[0]):
            split_j = result["j_call"].str.split(separator, expand=True)
            result["tra_j_call"] = split_j[0] if len(split_j.columns) > 0 else ""
            result["trb_j_call"] = split_j[1] if len(split_j.columns) > 1 else ""

    return result
