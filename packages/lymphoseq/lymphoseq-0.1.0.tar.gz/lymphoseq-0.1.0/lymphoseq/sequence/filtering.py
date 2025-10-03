"""
Sequence filtering functions for immune repertoire analysis.

Provides functions to filter, select, and manipulate sequences from
AIRR-formatted data, matching the functionality of R LymphoSeq2.
"""

import polars as pl
import pandas as pd
from typing import Union, Optional, List


def top_seqs(
    data: Union[pl.DataFrame, pd.DataFrame],
    top: int = 1,
    group_by: str = "repertoire_id",
    order_by: str = "duplicate_frequency"
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Select top N sequences from each repertoire by frequency.

    Creates a DataFrame containing the top productive sequences from each
    repertoire, ordered by their frequencies.

    Args:
        data: Input DataFrame with AIRR-formatted sequences. Must contain
            columns specified in `group_by` and `order_by` parameters.
        top: Number of top sequences to select from each repertoire (default: 1)
        group_by: Column name to group by (default: "repertoire_id")
        order_by: Column name to order by (default: "duplicate_frequency")

    Returns:
        DataFrame containing top N sequences from each repertoire, maintaining
        the same type (Polars or Pandas) as the input.

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> # Get top 10 sequences from each repertoire
        >>> top_10 = ls.top_seqs(data, top=10)
        >>> print(f"Selected {len(top_10)} sequences")

        >>> # Get most abundant clone from each sample
        >>> top_clone = ls.top_seqs(data, top=1)
        >>> print(top_clone[["repertoire_id", "junction_aa", "duplicate_frequency"]])

    See Also:
        - productive_seq(): Filter for productive sequences
        - unique_seqs(): Get unique sequences
    """
    is_polars = isinstance(data, pl.DataFrame)

    if is_polars:
        result = (
            data
            .sort(order_by, descending=True)
            .group_by(group_by, maintain_order=True)
            .head(top)
        )
    else:
        result = (
            data
            .sort_values(order_by, ascending=False)
            .groupby(group_by, as_index=False, sort=False)
            .head(top)
        )

    return result


def productive_seq(
    data: Union[pl.DataFrame, pd.DataFrame],
    aggregate: str = "junction_aa",
    productive_only: bool = True
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Filter productive sequences and optionally aggregate by amino acid or nucleotide.

    Filters the data for productive sequences (no stop codons, in-frame) and
    aggregates counts by the specified sequence column. This is typically used
    to prepare data for diversity analysis and visualization.

    Args:
        data: Input DataFrame with AIRR-formatted sequences. Must contain
            'productive' column and the column specified in `aggregate` parameter.
        aggregate: Column to aggregate by. Options:
            - "junction_aa": CDR3 amino acid sequences (default)
            - "junction": CDR3 nucleotide sequences
            - None: No aggregation, just filter productive sequences
        productive_only: Whether to filter for productive sequences only
            (default: True). If False, returns all sequences.

    Returns:
        DataFrame with filtered and aggregated sequences, maintaining the
        same type (Polars or Pandas) as the input.

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Get productive amino acid sequences (most common use case)
        >>> amino_table = ls.productive_seq(data, aggregate="junction_aa")
        >>> print(f"Unique amino acid sequences: {len(amino_table)}")

        >>> # Get productive nucleotide sequences
        >>> nucl_table = ls.productive_seq(data, aggregate="junction")

        >>> # Just filter productive, no aggregation
        >>> productive = ls.productive_seq(data, aggregate=None)

    Notes:
        - Aggregation sums duplicate_count and recalculates duplicate_frequency
        - When aggregating, the first occurrence's metadata is kept
        - Productive sequences are those where productive=True (no stop codons, in-frame)

    See Also:
        - top_seqs(): Get top sequences by frequency
        - unique_seqs(): Get unique sequences without aggregation
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Filter for productive sequences if requested
    if productive_only:
        if is_polars:
            filtered = data.filter(pl.col("productive") == True)
        else:
            filtered = data[data["productive"] == True].copy()
    else:
        filtered = data

    # If no aggregation requested, return filtered data
    if aggregate is None:
        return filtered

    # Validate aggregate column exists
    if aggregate not in filtered.columns:
        raise ValueError(f"Column '{aggregate}' not found in data")

    # Aggregate by specified column
    if is_polars:
        result = (
            filtered
            .group_by([aggregate, "repertoire_id"])
            .agg([
                pl.col("duplicate_count").sum().alias("duplicate_count"),
                pl.first("v_call").alias("v_call"),
                pl.first("j_call").alias("j_call"),
                pl.first("d_call").alias("d_call"),
                pl.first("junction_length").alias("junction_length"),
                pl.first("sequence_id").alias("sequence_id"),
            ])
        )

        # Recalculate frequency within each repertoire
        result = (
            result
            .with_columns([
                (pl.col("duplicate_count") /
                 pl.col("duplicate_count").sum().over("repertoire_id"))
                .alias("duplicate_frequency")
            ])
            .sort(["repertoire_id", "duplicate_frequency"], descending=[False, True])
        )
    else:
        # Group and aggregate
        agg_dict = {
            "duplicate_count": "sum",
        }

        # Only add columns that exist
        optional_cols = ["v_call", "j_call", "d_call", "junction_length", "sequence_id", "junction", "productive"]
        for col in optional_cols:
            if col in filtered.columns:
                agg_dict[col] = "first"

        result = (
            filtered
            .groupby([aggregate, "repertoire_id"], as_index=False)
            .agg(agg_dict)
        )

        # Recalculate frequency within each repertoire
        result["duplicate_frequency"] = (
            result.groupby("repertoire_id")["duplicate_count"]
            .transform(lambda x: x / x.sum())
        )

        result = result.sort_values(
            ["repertoire_id", "duplicate_frequency"],
            ascending=[True, False]
        )

    return result


def unique_seqs(
    data: Union[pl.DataFrame, pd.DataFrame],
    by_column: str = "junction_aa",
    keep: str = "first"
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Get unique sequences based on specified column.

    Returns unique sequences based on the specified column, keeping either
    the first or last occurrence of duplicates.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        by_column: Column name to determine uniqueness (default: "junction_aa")
        keep: Which occurrence to keep for duplicates:
            - "first": Keep first occurrence (default)
            - "last": Keep last occurrence

    Returns:
        DataFrame with unique sequences, maintaining the same type
        (Polars or Pandas) as the input.

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Get unique amino acid sequences
        >>> unique_aa = ls.unique_seqs(data, by_column="junction_aa")
        >>> print(f"Unique sequences: {len(unique_aa)}")

        >>> # Get unique nucleotide sequences
        >>> unique_nt = ls.unique_seqs(data, by_column="junction")

    Notes:
        - This function does not aggregate counts like productive_seq()
        - Use productive_seq() with aggregate parameter for count aggregation

    See Also:
        - productive_seq(): Filter and aggregate sequences
        - top_seqs(): Get top sequences by frequency
    """
    is_polars = isinstance(data, pl.DataFrame)

    if by_column not in data.columns:
        raise ValueError(f"Column '{by_column}' not found in data")

    if is_polars:
        if keep == "first":
            result = data.unique(subset=[by_column], keep="first", maintain_order=True)
        else:
            result = data.unique(subset=[by_column], keep="last", maintain_order=True)
    else:
        result = data.drop_duplicates(subset=[by_column], keep=keep)

    return result


def remove_seq(
    data: Union[pl.DataFrame, pd.DataFrame],
    sequences: Union[str, List[str]],
    column: str = "junction_aa",
    invert: bool = False
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Remove (or keep only) specific sequences from the data.

    Removes sequences matching the specified criteria, or keeps only those
    sequences if invert=True.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        sequences: Single sequence or list of sequences to remove/keep
        column: Column name containing sequences to match (default: "junction_aa")
        invert: If True, keep only matching sequences instead of removing them
            (default: False)

    Returns:
        DataFrame with sequences removed (or kept if invert=True), maintaining
        the same type (Polars or Pandas) as the input.

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Remove a specific sequence
        >>> filtered = ls.remove_seq(data, sequences="CASSLKPNTEAFF")

        >>> # Remove multiple sequences
        >>> to_remove = ["CASSLKPNTEAFF", "CASSXXXXTEAFF"]
        >>> filtered = ls.remove_seq(data, sequences=to_remove)

        >>> # Keep only specific sequences
        >>> keep_these = ["CASSLKPNTEAFF", "CASSXXXXTEAFF"]
        >>> subset = ls.remove_seq(data, sequences=keep_these, invert=True)

    Notes:
        - Case-sensitive matching
        - Uses exact string matching

    See Also:
        - productive_seq(): Filter productive sequences
        - top_seqs(): Select top sequences
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Ensure sequences is a list
    if isinstance(sequences, str):
        sequences = [sequences]

    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in data")

    # Filter data
    if is_polars:
        if invert:
            # Keep only matching sequences
            result = data.filter(pl.col(column).is_in(sequences))
        else:
            # Remove matching sequences
            result = data.filter(~pl.col(column).is_in(sequences))
    else:
        if invert:
            # Keep only matching sequences
            result = data[data[column].isin(sequences)].copy()
        else:
            # Remove matching sequences
            result = data[~data[column].isin(sequences)].copy()

    return result
