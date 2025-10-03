"""
Gene usage analysis functions for immune repertoire data.

Provides functions for analyzing V, D, and J gene usage patterns
in TCR and BCR repertoires.
"""

import polars as pl
import pandas as pd
from typing import Union, Optional, List, Literal
import numpy as np


def gene_freq(
    data: Union[pl.DataFrame, pd.DataFrame],
    gene: Literal["v", "d", "j"] = "v",
    repertoire_ids: Optional[List[str]] = None,
    top_n: Optional[int] = None,
    normalize: bool = True
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Calculate V, D, or J gene usage frequencies.

    Computes the frequency of each V, D, or J gene across repertoires.
    Results can be used for repertoire characterization and comparison
    of gene usage patterns.

    Args:
        data: Input DataFrame with AIRR-formatted sequences. Must contain
            v_call, d_call, or j_call columns.
        gene: Gene segment to analyze: "v", "d", or "j" (default: "v")
        repertoire_ids: List of repertoire IDs to analyze. If None, uses all
            repertoires (default: None)
        top_n: Return only the top N most frequent genes. If None, returns
            all genes (default: None)
        normalize: If True, returns frequencies (0-1); if False, returns
            raw counts (default: True)

    Returns:
        DataFrame with gene usage statistics. Contains columns:
        - gene_name: Gene identifier (e.g., TRBV1-1)
        - repertoire_id: Repertoire identifier
        - count: Number of sequences using this gene
        - frequency: Proportion of sequences (if normalize=True)

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Calculate V gene usage
        >>> v_usage = ls.gene_freq(data, gene="v")
        >>> print(v_usage.head())

        >>> # Get top 10 J genes
        >>> j_top10 = ls.gene_freq(data, gene="j", top_n=10)

        >>> # Compare D gene usage in specific samples
        >>> d_usage = ls.gene_freq(
        ...     data,
        ...     gene="d",
        ...     repertoire_ids=["S1", "S2", "S3"]
        ... )

        >>> # Get raw counts instead of frequencies
        >>> v_counts = ls.gene_freq(data, gene="v", normalize=False)

    Notes:
        - Gene calls may contain allele information (e.g., TRBV1-1*01)
        - Alleles are typically grouped by removing the *01 suffix
        - Missing or unassigned genes are excluded from calculations

    See Also:
        - top_seqs(): Get most abundant sequences
        - clonal_relatedness(): Compare repertoire similarity
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Determine gene column
    gene_col_map = {
        "v": "v_call",
        "d": "d_call",
        "j": "j_call"
    }

    if gene not in gene_col_map:
        raise ValueError(f"gene must be 'v', 'd', or 'j', got '{gene}'")

    gene_col = gene_col_map[gene]

    # Validate column exists
    if gene_col not in data.columns:
        raise ValueError(f"Column '{gene_col}' not found in data")

    if "repertoire_id" not in data.columns:
        raise ValueError("Column 'repertoire_id' not found in data")

    # Filter for specified repertoires
    if repertoire_ids is not None:
        if is_polars:
            filtered = data.filter(pl.col("repertoire_id").is_in(repertoire_ids))
        else:
            filtered = data[data["repertoire_id"].isin(repertoire_ids)].copy()
    else:
        filtered = data

    # Remove null/missing gene calls
    if is_polars:
        filtered = filtered.filter(pl.col(gene_col).is_not_null())
        filtered = filtered.filter(pl.col(gene_col) != "")
    else:
        filtered = filtered[filtered[gene_col].notna()].copy()
        filtered = filtered[filtered[gene_col] != ""].copy()

    # Clean gene names (remove allele information like *01)
    if is_polars:
        filtered = filtered.with_columns(
            pl.col(gene_col).str.split("*").list.first().alias("gene_name")
        )
    else:
        filtered["gene_name"] = filtered[gene_col].str.split("*").str[0]

    # Calculate frequencies
    if is_polars:
        # Count occurrences by gene and repertoire
        result = (
            filtered
            .group_by(["gene_name", "repertoire_id"])
            .agg([
                pl.count().alias("count")
            ])
        )

        if normalize:
            # Calculate frequency within each repertoire
            result = result.with_columns(
                (pl.col("count") / pl.col("count").sum().over("repertoire_id"))
                .alias("frequency")
            )

        # Sort by frequency/count within each repertoire
        sort_col = "frequency" if normalize else "count"
        result = result.sort(
            ["repertoire_id", sort_col],
            descending=[False, True]
        )

    else:
        # Count occurrences by gene and repertoire
        result = (
            filtered
            .groupby(["gene_name", "repertoire_id"])
            .size()
            .reset_index(name="count")
        )

        if normalize:
            # Calculate frequency within each repertoire
            result["frequency"] = (
                result.groupby("repertoire_id")["count"]
                .transform(lambda x: x / x.sum())
            )

        # Sort by frequency/count within each repertoire
        sort_col = "frequency" if normalize else "count"
        result = result.sort_values(
            ["repertoire_id", sort_col],
            ascending=[True, False]
        )

    # Filter for top N genes if requested
    if top_n is not None:
        if is_polars:
            sort_col = "frequency" if normalize else "count"
            result = (
                result
                .sort(sort_col, descending=True)
                .group_by("repertoire_id", maintain_order=True)
                .head(top_n)
            )
        else:
            sort_col = "frequency" if normalize else "count"
            result = (
                result
                .sort_values(sort_col, ascending=False)
                .groupby("repertoire_id", as_index=False, sort=False)
                .head(top_n)
            )

    return result


def gene_pair_freq(
    data: Union[pl.DataFrame, pd.DataFrame],
    gene_pair: Literal["vj", "vd", "dj"] = "vj",
    repertoire_ids: Optional[List[str]] = None,
    top_n: Optional[int] = None,
    normalize: bool = True
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Calculate V-J, V-D, or D-J gene pair usage frequencies.

    Analyzes the co-occurrence of gene pairs to understand recombination
    patterns and biases in repertoires.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        gene_pair: Gene pair to analyze: "vj", "vd", or "dj" (default: "vj")
        repertoire_ids: List of repertoire IDs to analyze. If None, uses all
            repertoires (default: None)
        top_n: Return only the top N most frequent pairs. If None, returns
            all pairs (default: None)
        normalize: If True, returns frequencies; if False, returns counts
            (default: True)

    Returns:
        DataFrame with gene pair usage statistics. Contains columns:
        - gene1: First gene in pair (e.g., V gene)
        - gene2: Second gene in pair (e.g., J gene)
        - repertoire_id: Repertoire identifier
        - count: Number of sequences with this pair
        - frequency: Proportion of sequences (if normalize=True)

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Calculate V-J pairing
        >>> vj_pairs = ls.gene_pair_freq(data, gene_pair="vj")
        >>> print(vj_pairs.head())

        >>> # Get top 20 V-J pairs
        >>> vj_top20 = ls.gene_pair_freq(data, gene_pair="vj", top_n=20)

    See Also:
        - gene_freq(): Single gene usage analysis
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Determine gene columns
    pair_col_map = {
        "vj": ("v_call", "j_call"),
        "vd": ("v_call", "d_call"),
        "dj": ("d_call", "j_call")
    }

    if gene_pair not in pair_col_map:
        raise ValueError(f"gene_pair must be 'vj', 'vd', or 'dj', got '{gene_pair}'")

    gene1_col, gene2_col = pair_col_map[gene_pair]

    # Validate columns exist
    for col in [gene1_col, gene2_col]:
        if col not in data.columns:
            raise ValueError(f"Column '{col}' not found in data")

    if "repertoire_id" not in data.columns:
        raise ValueError("Column 'repertoire_id' not found in data")

    # Filter for specified repertoires
    if repertoire_ids is not None:
        if is_polars:
            filtered = data.filter(pl.col("repertoire_id").is_in(repertoire_ids))
        else:
            filtered = data[data["repertoire_id"].isin(repertoire_ids)].copy()
    else:
        filtered = data

    # Remove null/missing gene calls
    if is_polars:
        filtered = filtered.filter(
            pl.col(gene1_col).is_not_null() & pl.col(gene2_col).is_not_null()
        )
        filtered = filtered.filter(
            (pl.col(gene1_col) != "") & (pl.col(gene2_col) != "")
        )
    else:
        filtered = filtered[
            filtered[gene1_col].notna() & filtered[gene2_col].notna()
        ].copy()
        filtered = filtered[
            (filtered[gene1_col] != "") & (filtered[gene2_col] != "")
        ].copy()

    # Clean gene names (remove allele information)
    if is_polars:
        filtered = filtered.with_columns([
            pl.col(gene1_col).str.split("*").list.first().alias("gene1"),
            pl.col(gene2_col).str.split("*").list.first().alias("gene2")
        ])
    else:
        filtered["gene1"] = filtered[gene1_col].str.split("*").str[0]
        filtered["gene2"] = filtered[gene2_col].str.split("*").str[0]

    # Calculate frequencies
    if is_polars:
        # Count occurrences by gene pair and repertoire
        result = (
            filtered
            .group_by(["gene1", "gene2", "repertoire_id"])
            .agg([
                pl.count().alias("count")
            ])
        )

        if normalize:
            # Calculate frequency within each repertoire
            result = result.with_columns(
                (pl.col("count") / pl.col("count").sum().over("repertoire_id"))
                .alias("frequency")
            )

        # Sort by frequency/count within each repertoire
        sort_col = "frequency" if normalize else "count"
        result = result.sort(
            ["repertoire_id", sort_col],
            descending=[False, True]
        )

    else:
        # Count occurrences by gene pair and repertoire
        result = (
            filtered
            .groupby(["gene1", "gene2", "repertoire_id"])
            .size()
            .reset_index(name="count")
        )

        if normalize:
            # Calculate frequency within each repertoire
            result["frequency"] = (
                result.groupby("repertoire_id")["count"]
                .transform(lambda x: x / x.sum())
            )

        # Sort by frequency/count within each repertoire
        sort_col = "frequency" if normalize else "count"
        result = result.sort_values(
            ["repertoire_id", sort_col],
            ascending=[True, False]
        )

    # Filter for top N pairs if requested
    if top_n is not None:
        if is_polars:
            sort_col = "frequency" if normalize else "count"
            result = (
                result
                .sort(sort_col, descending=True)
                .group_by("repertoire_id", maintain_order=True)
                .head(top_n)
            )
        else:
            sort_col = "frequency" if normalize else "count"
            result = (
                result
                .sort_values(sort_col, ascending=False)
                .groupby("repertoire_id", as_index=False, sort=False)
                .head(top_n)
            )

    return result
