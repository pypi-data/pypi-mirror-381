"""
Comparative analysis functions for immune repertoire data.

Provides functions for comparing sequences across multiple repertoires,
including common sequence identification, differential abundance testing,
clonal relatedness metrics, and longitudinal clone tracking.
"""

import polars as pl
import pandas as pd
from typing import Union, Optional, List, Dict
import numpy as np


def common_seqs(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_ids: Optional[List[str]] = None,
    by_column: str = "junction_aa",
    min_repertoires: int = 2
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Find sequences shared across multiple repertoires.

    Identifies sequences that appear in two or more repertoires and returns
    their frequencies across all repertoires where they appear.

    Args:
        data: Input DataFrame with AIRR-formatted sequences. Must contain
            'repertoire_id' column and the column specified in `by_column`.
        repertoire_ids: List of repertoire IDs to compare. If None, uses all
            repertoires in the data (default: None)
        by_column: Column name containing sequences to compare
            (default: "junction_aa")
        min_repertoires: Minimum number of repertoires a sequence must appear
            in to be included (default: 2)

    Returns:
        DataFrame with common sequences and their frequencies across repertoires.
        Contains columns: sequence column, repertoire_id, duplicate_count,
        duplicate_frequency, and n_repertoires (count of repertoires sharing
        this sequence).

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Find sequences common to 2+ samples
        >>> common = ls.common_seqs(data)
        >>> print(f"Found {len(common)} common sequence occurrences")

        >>> # Find sequences in specific repertoires
        >>> common = ls.common_seqs(
        ...     data,
        ...     repertoire_ids=["S1", "S2", "S3"]
        ... )

        >>> # Find highly shared sequences (3+ repertoires)
        >>> highly_shared = ls.common_seqs(data, min_repertoires=3)

    See Also:
        - clonal_relatedness(): Calculate similarity between repertoires
        - differential_abundance(): Test for differential sequence abundance
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Validate column exists
    if by_column not in data.columns:
        raise ValueError(f"Column '{by_column}' not found in data")

    if "repertoire_id" not in data.columns:
        raise ValueError("Column 'repertoire_id' not found in data")

    # Filter for specified repertoires if provided
    if repertoire_ids is not None:
        if is_polars:
            filtered = data.filter(pl.col("repertoire_id").is_in(repertoire_ids))
        else:
            filtered = data[data["repertoire_id"].isin(repertoire_ids)].copy()
    else:
        filtered = data

    # Count number of repertoires each sequence appears in
    if is_polars:
        # Count unique repertoires per sequence
        seq_counts = (
            filtered
            .group_by(by_column)
            .agg([
                pl.col("repertoire_id").n_unique().alias("n_repertoires")
            ])
        )

        # Filter for sequences in min_repertoires or more
        common_seqs_list = (
            seq_counts
            .filter(pl.col("n_repertoires") >= min_repertoires)
            .select(by_column)
        )

        # Get all records for common sequences
        result = (
            filtered
            .join(common_seqs_list, on=by_column, how="inner")
        )

        # Add n_repertoires column
        result = result.join(seq_counts, on=by_column, how="left")

        # Sort by n_repertoires (descending) and sequence
        result = result.sort(
            ["n_repertoires", by_column, "repertoire_id"],
            descending=[True, False, False]
        )

    else:
        # Count unique repertoires per sequence
        seq_counts = (
            filtered
            .groupby(by_column)["repertoire_id"]
            .nunique()
            .reset_index()
            .rename(columns={"repertoire_id": "n_repertoires"})
        )

        # Filter for sequences in min_repertoires or more
        common_seqs_list = seq_counts[
            seq_counts["n_repertoires"] >= min_repertoires
        ][by_column]

        # Get all records for common sequences
        result = filtered[filtered[by_column].isin(common_seqs_list)].copy()

        # Add n_repertoires column
        result = result.merge(seq_counts, on=by_column, how="left")

        # Sort by n_repertoires (descending) and sequence
        result = result.sort_values(
            ["n_repertoires", by_column, "repertoire_id"],
            ascending=[False, True, True]
        )

    return result


def differential_abundance(
    data: Union[pl.DataFrame, pd.DataFrame],
    group1: List[str],
    group2: List[str],
    by_column: str = "junction_aa",
    min_count: int = 5,
    method: str = "fisher"
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Test for differential abundance of sequences between two groups.

    Performs statistical testing (Fisher's exact test or Chi-square) to identify
    sequences with significantly different abundances between two groups of
    repertoires.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        group1: List of repertoire IDs in first group
        group2: List of repertoire IDs in second group
        by_column: Column containing sequences to compare (default: "junction_aa")
        min_count: Minimum total count across both groups for testing
            (default: 5)
        method: Statistical test method: "fisher" or "chi-square"
            (default: "fisher")

    Returns:
        DataFrame with sequences and test statistics including:
        - sequence column (junction_aa or junction)
        - count_group1, count_group2: Total counts in each group
        - freq_group1, freq_group2: Frequencies in each group
        - p_value: Statistical significance
        - log2_fold_change: log2(freq_group2 / freq_group1)
        - significant: Boolean indicating p < 0.05

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Compare two groups of samples
        >>> diff = ls.differential_abundance(
        ...     data,
        ...     group1=["Patient1_Pre", "Patient2_Pre"],
        ...     group2=["Patient1_Post", "Patient2_Post"]
        ... )

        >>> # Filter for significant sequences
        >>> sig = diff.filter(pl.col("significant")) if isinstance(diff, pl.DataFrame) else diff[diff["significant"]]
        >>> print(f"Found {len(sig)} differentially abundant sequences")

    Notes:
        - Fisher's exact test recommended for small counts
        - Chi-square test faster for large datasets
        - P-values are not corrected for multiple testing

    See Also:
        - common_seqs(): Find shared sequences
        - clonal_relatedness(): Measure repertoire similarity
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Validate inputs
    if by_column not in data.columns:
        raise ValueError(f"Column '{by_column}' not found in data")

    if "repertoire_id" not in data.columns or "duplicate_count" not in data.columns:
        raise ValueError("Data must contain 'repertoire_id' and 'duplicate_count' columns")

    if method not in ["fisher", "chi-square"]:
        raise ValueError("method must be 'fisher' or 'chi-square'")

    # Filter for specified groups
    all_repertoires = group1 + group2
    if is_polars:
        filtered = data.filter(pl.col("repertoire_id").is_in(all_repertoires))
    else:
        filtered = data[data["repertoire_id"].isin(all_repertoires)].copy()

    # Aggregate counts by sequence and group
    if is_polars:
        # Add group label
        filtered = filtered.with_columns(
            pl.when(pl.col("repertoire_id").is_in(group1))
            .then(pl.lit("group1"))
            .otherwise(pl.lit("group2"))
            .alias("group")
        )

        # Aggregate by sequence and group
        seq_counts = (
            filtered
            .group_by([by_column, "group"])
            .agg([
                pl.col("duplicate_count").sum().alias("count")
            ])
        )

        # Pivot to wide format
        seq_wide = (
            seq_counts
            .pivot(values="count", index=by_column, columns="group")
            .fill_null(0)
        )

        # Calculate totals for each group
        total_group1 = filtered.filter(pl.col("group") == "group1")["duplicate_count"].sum()
        total_group2 = filtered.filter(pl.col("group") == "group2")["duplicate_count"].sum()

        # Filter by minimum count
        seq_wide = seq_wide.filter(
            (pl.col("group1") + pl.col("group2")) >= min_count
        )

    else:
        # Add group label
        filtered["group"] = filtered["repertoire_id"].apply(
            lambda x: "group1" if x in group1 else "group2"
        )

        # Aggregate by sequence and group
        seq_counts = (
            filtered
            .groupby([by_column, "group"])["duplicate_count"]
            .sum()
            .reset_index()
            .rename(columns={"duplicate_count": "count"})
        )

        # Pivot to wide format
        seq_wide = seq_counts.pivot(
            index=by_column,
            columns="group",
            values="count"
        ).fillna(0).reset_index()

        # Calculate totals for each group
        total_group1 = filtered[filtered["group"] == "group1"]["duplicate_count"].sum()
        total_group2 = filtered[filtered["group"] == "group2"]["duplicate_count"].sum()

        # Filter by minimum count
        seq_wide = seq_wide[
            (seq_wide["group1"] + seq_wide["group2"]) >= min_count
        ].copy()

    # Perform statistical test
    if method == "fisher":
        from scipy.stats import fisher_exact

        def fisher_test(row):
            # Create contingency table
            a = int(row["group1"])  # sequence in group1
            b = int(row["group2"])  # sequence in group2
            c = int(total_group1 - a)  # other sequences in group1
            d = int(total_group2 - b)  # other sequences in group2

            # Fisher's exact test
            _, p_value = fisher_exact([[a, b], [c, d]])
            return p_value

        if is_polars:
            # Convert to pandas for scipy, then back
            seq_wide_pd = seq_wide.to_pandas()
            seq_wide_pd["p_value"] = seq_wide_pd.apply(fisher_test, axis=1)
            seq_wide = pl.from_pandas(seq_wide_pd)
        else:
            seq_wide["p_value"] = seq_wide.apply(fisher_test, axis=1)

    else:  # chi-square
        from scipy.stats import chi2_contingency

        def chi_square_test(row):
            a = int(row["group1"])
            b = int(row["group2"])
            c = int(total_group1 - a)
            d = int(total_group2 - b)

            _, p_value, _, _ = chi2_contingency([[a, b], [c, d]])
            return p_value

        if is_polars:
            seq_wide_pd = seq_wide.to_pandas()
            seq_wide_pd["p_value"] = seq_wide_pd.apply(chi_square_test, axis=1)
            seq_wide = pl.from_pandas(seq_wide_pd)
        else:
            seq_wide["p_value"] = seq_wide.apply(chi_square_test, axis=1)

    # Calculate frequencies and fold change
    if is_polars:
        result = seq_wide.with_columns([
            (pl.col("group1") / total_group1).alias("freq_group1"),
            (pl.col("group2") / total_group2).alias("freq_group2"),
        ])

        # Calculate log2 fold change (with pseudocount to avoid division by zero)
        result = result.with_columns([
            (
                (pl.col("freq_group2") + 1e-10).log() / np.log(2) -
                (pl.col("freq_group1") + 1e-10).log() / np.log(2)
            ).alias("log2_fold_change"),
            (pl.col("p_value") < 0.05).alias("significant")
        ])

        # Rename count columns
        result = result.rename({"group1": "count_group1", "group2": "count_group2"})

        # Sort by p-value
        result = result.sort("p_value")

    else:
        result = seq_wide.copy()
        result["freq_group1"] = result["group1"] / total_group1
        result["freq_group2"] = result["group2"] / total_group2

        # Calculate log2 fold change
        result["log2_fold_change"] = (
            np.log2(result["freq_group2"] + 1e-10) -
            np.log2(result["freq_group1"] + 1e-10)
        )

        result["significant"] = result["p_value"] < 0.05

        # Rename count columns
        result = result.rename(columns={"group1": "count_group1", "group2": "count_group2"})

        # Sort by p-value
        result = result.sort_values("p_value")

    return result


def clonal_relatedness(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_ids: Optional[List[str]] = None,
    by_column: str = "junction_aa",
    method: str = "morisita"
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Calculate pairwise similarity between repertoires.

    Computes similarity metrics between all pairs of repertoires to measure
    clonal relatedness. Uses Morisita-Horn index by default, which accounts
    for both presence/absence and relative abundance of sequences.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        repertoire_ids: List of repertoire IDs to compare. If None, uses all
            repertoires (default: None)
        by_column: Column containing sequences to compare (default: "junction_aa")
        method: Similarity metric to use:
            - "morisita": Morisita-Horn index (default, recommended)
            - "jaccard": Jaccard index (presence/absence only)
            - "cosine": Cosine similarity

    Returns:
        DataFrame with pairwise similarity scores. Contains columns:
        - repertoire1, repertoire2: Pair of repertoire IDs
        - similarity: Similarity score (0-1, where 1 = identical)
        - n_shared: Number of shared sequences
        - n_total: Total unique sequences across both repertoires

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Calculate Morisita-Horn index for all pairs
        >>> similarity = ls.clonal_relatedness(data)
        >>> print(similarity)

        >>> # Compare specific samples
        >>> similarity = ls.clonal_relatedness(
        ...     data,
        ...     repertoire_ids=["S1", "S2", "S3"]
        ... )

        >>> # Use Jaccard index instead
        >>> jaccard = ls.clonal_relatedness(data, method="jaccard")

    Notes:
        - Morisita-Horn index: Recommended for abundance-weighted similarity
        - Jaccard index: Simple overlap coefficient (0-1)
        - Cosine similarity: Angle between frequency vectors
        - All metrics return values between 0 (no similarity) and 1 (identical)

    References:
        Morisita M. (1959) Measuring of the dispersion and analysis of
        distribution patterns. Memoires of the Faculty of Science,
        Kyushu University, Series E. Biology, 2, 215-235.

    See Also:
        - common_seqs(): Find shared sequences
        - differential_abundance(): Test for differential abundance
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Validate inputs
    if by_column not in data.columns:
        raise ValueError(f"Column '{by_column}' not found in data")

    if "repertoire_id" not in data.columns or "duplicate_frequency" not in data.columns:
        raise ValueError("Data must contain 'repertoire_id' and 'duplicate_frequency' columns")

    if method not in ["morisita", "jaccard", "cosine"]:
        raise ValueError("method must be 'morisita', 'jaccard', or 'cosine'")

    # Filter for specified repertoires
    if repertoire_ids is not None:
        if is_polars:
            filtered = data.filter(pl.col("repertoire_id").is_in(repertoire_ids))
        else:
            filtered = data[data["repertoire_id"].isin(repertoire_ids)].copy()
    else:
        filtered = data

    # Get list of unique repertoires
    if is_polars:
        repertoire_list = filtered["repertoire_id"].unique().sort().to_list()
    else:
        repertoire_list = sorted(filtered["repertoire_id"].unique())

    # Create frequency matrix (sequences × repertoires)
    # Need to aggregate in case of duplicates
    if is_polars:
        # Aggregate by sequence and repertoire first
        freq_data = (
            filtered
            .group_by([by_column, "repertoire_id"])
            .agg(pl.col("duplicate_frequency").sum())
        )

        freq_matrix = (
            freq_data
            .pivot(
                values="duplicate_frequency",
                index=by_column,
                columns="repertoire_id"
            )
            .fill_null(0)
        )
    else:
        # Aggregate by sequence and repertoire first
        freq_data = (
            filtered
            [[by_column, "repertoire_id", "duplicate_frequency"]]
            .groupby([by_column, "repertoire_id"])["duplicate_frequency"]
            .sum()
            .reset_index()
        )

        freq_matrix = (
            freq_data
            .pivot(
                index=by_column,
                columns="repertoire_id",
                values="duplicate_frequency"
            )
            .fillna(0)
        )

    # Calculate pairwise similarities
    results = []

    for i, rep1 in enumerate(repertoire_list):
        for rep2 in repertoire_list[i+1:]:
            if is_polars:
                freq1 = freq_matrix[rep1].to_numpy()
                freq2 = freq_matrix[rep2].to_numpy()
            else:
                freq1 = freq_matrix[rep1].values
                freq2 = freq_matrix[rep2].values

            # Count shared sequences
            n_shared = int(np.sum((freq1 > 0) & (freq2 > 0)))
            n_total = int(np.sum((freq1 > 0) | (freq2 > 0)))

            # Calculate similarity based on method
            if method == "morisita":
                # Morisita-Horn index
                numerator = 2 * np.sum(freq1 * freq2)
                denominator = (np.sum(freq1**2) + np.sum(freq2**2))

                if denominator == 0:
                    similarity = 0.0
                else:
                    similarity = numerator / denominator

            elif method == "jaccard":
                # Jaccard index
                if n_total == 0:
                    similarity = 0.0
                else:
                    similarity = n_shared / n_total

            else:  # cosine
                # Cosine similarity
                numerator = np.sum(freq1 * freq2)
                denominator = np.sqrt(np.sum(freq1**2)) * np.sqrt(np.sum(freq2**2))

                if denominator == 0:
                    similarity = 0.0
                else:
                    similarity = numerator / denominator

            results.append({
                "repertoire1": rep1,
                "repertoire2": rep2,
                "similarity": similarity,
                "n_shared": n_shared,
                "n_total": n_total
            })

    # Convert results to DataFrame
    if is_polars:
        result = pl.DataFrame(results)
        result = result.sort(["similarity"], descending=True)
    else:
        result = pd.DataFrame(results)
        result = result.sort_values("similarity", ascending=False)

    return result


def clone_track(
    data: Union[pl.DataFrame, pd.DataFrame],
    by_column: str = "junction_aa",
    include_frequency: bool = True
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Track clones across multiple repertoires/time points.

    Creates a matrix showing the presence and frequency of each unique sequence
    across all repertoires. This is essential for longitudinal analysis and
    tracking clonal dynamics over time or across conditions.

    Args:
        data: Input DataFrame with AIRR-formatted sequences. Must contain
            'repertoire_id' and the column specified in `by_column`.
        by_column: Column containing sequences to track (default: "junction_aa")
        include_frequency: If True, returns frequencies; if False, returns
            presence/absence (1/0) (default: True)

    Returns:
        DataFrame in wide format with sequences as rows and repertoires as columns.
        - First column: sequence (junction_aa or junction)
        - Remaining columns: one per repertoire
        - Values: frequencies (if include_frequency=True) or binary presence (0/1)

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Track clones with frequencies
        >>> tracking = ls.clone_track(data)
        >>> print(tracking.head())

        >>> # Track presence/absence only
        >>> presence = ls.clone_track(data, include_frequency=False)

        >>> # Filter for sequences seen in multiple samples
        >>> # Count non-zero values per row
        >>> if isinstance(tracking, pl.DataFrame):
        ...     tracking = tracking.with_columns(
        ...         pl.sum_horizontal(pl.all().exclude(by_column) > 0).alias("n_samples")
        ...     )
        ...     shared = tracking.filter(pl.col("n_samples") > 1)

    Notes:
        - Missing sequences in a repertoire are represented as 0
        - This function is memory-intensive for large datasets
        - Output is in wide format (sequences × repertoires matrix)

    See Also:
        - common_seqs(): Find sequences present in multiple repertoires
        - clonal_relatedness(): Calculate repertoire similarity
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Validate inputs
    if by_column not in data.columns:
        raise ValueError(f"Column '{by_column}' not found in data")

    if "repertoire_id" not in data.columns:
        raise ValueError("Column 'repertoire_id' not found in data")

    # Determine value column
    if include_frequency:
        if "duplicate_frequency" not in data.columns:
            raise ValueError("Column 'duplicate_frequency' required when include_frequency=True")
        value_col = "duplicate_frequency"
    else:
        # Create binary presence column
        value_col = "presence"
        if is_polars:
            data = data.with_columns(pl.lit(1).alias(value_col))
        else:
            data = data.copy()
            data[value_col] = 1

    # Create pivot table
    if is_polars:
        # Select only needed columns
        pivot_data = data.select([by_column, "repertoire_id", value_col])

        # Pivot to wide format
        result = (
            pivot_data
            .pivot(
                values=value_col,
                index=by_column,
                columns="repertoire_id"
            )
            .fill_null(0)
        )

        # Sort by sequence
        result = result.sort(by_column)

    else:
        # Select only needed columns
        pivot_data = data[[by_column, "repertoire_id", value_col]]

        # Pivot to wide format
        result = (
            pivot_data
            .pivot(
                index=by_column,
                columns="repertoire_id",
                values=value_col
            )
            .fillna(0)
            .reset_index()
        )

        # Sort by sequence
        result = result.sort_values(by_column)

    return result


def searchSeq(
    data: Union[pl.DataFrame, pd.DataFrame],
    sequence: str,
    by_column: str = "junction_aa",
    exact: bool = True
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Search for specific sequences or patterns in the data.

    Finds all occurrences of a sequence (exact match) or sequences containing
    a pattern (substring match) across all repertoires.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        sequence: Sequence string to search for
        by_column: Column to search in (default: "junction_aa")
        exact: If True, exact match; if False, substring match (default: True)

    Returns:
        DataFrame containing all matching sequences with their frequencies
        and repertoire information.

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Find exact sequence
        >>> matches = ls.searchSeq(data, "CASSLKPNTEAFF")
        >>> print(f"Found in {matches['repertoire_id'].n_unique()} repertoires")

        >>> # Find sequences containing motif
        >>> motif_matches = ls.searchSeq(data, "LKPN", exact=False)
        >>> print(f"Found {len(motif_matches)} sequences with LKPN motif")

    See Also:
        - remove_seq(): Remove specific sequences
        - common_seqs(): Find shared sequences
    """
    is_polars = isinstance(data, pl.DataFrame)

    if by_column not in data.columns:
        raise ValueError(f"Column '{by_column}' not found in data")

    # Search for sequence
    if is_polars:
        if exact:
            result = data.filter(pl.col(by_column) == sequence)
        else:
            result = data.filter(pl.col(by_column).str.contains(sequence))
    else:
        if exact:
            result = data[data[by_column] == sequence].copy()
        else:
            result = data[data[by_column].str.contains(sequence, na=False)].copy()

    return result


def mergeSeqs(
    data: Union[pl.DataFrame, pd.DataFrame],
    merge_column: str = "repertoire_id",
    new_name: str = "merged",
    repertoire_ids: Optional[List[str]] = None
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Merge multiple repertoires into a single combined repertoire.

    Combines sequences from multiple repertoires, aggregating counts and
    recalculating frequencies. Useful for creating grouped/pooled samples
    or combining technical replicates.

    Args:
        data: Input DataFrame with AIRR-formatted sequences
        merge_column: Column to use for grouping (default: "repertoire_id")
        new_name: Name for the merged repertoire (default: "merged")
        repertoire_ids: List of repertoire IDs to merge. If None, merges all
            repertoires (default: None)

    Returns:
        DataFrame with merged repertoire. Sequences are aggregated by junction_aa,
        counts are summed, and frequencies are recalculated.

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")

        >>> # Merge all repertoires
        >>> merged_all = ls.mergeSeqs(data, new_name="combined")

        >>> # Merge specific samples (e.g., technical replicates)
        >>> merged = ls.mergeSeqs(
        ...     data,
        ...     repertoire_ids=["Sample1_rep1", "Sample1_rep2"],
        ...     new_name="Sample1_merged"
        ... )

        >>> # Merge by treatment group
        >>> treatment_group = data[data["treatment"] == "drug_A"]
        >>> merged_treatment = ls.mergeSeqs(
        ...     treatment_group,
        ...     new_name="drug_A_pooled"
        ... )

    Notes:
        - Duplicate counts are summed across merged repertoires
        - Frequencies are recalculated after merging
        - Metadata from first occurrence is kept

    See Also:
        - productive_seq(): Aggregate sequences within repertoires
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Filter for specific repertoires if provided
    if repertoire_ids is not None:
        if is_polars:
            filtered = data.filter(pl.col(merge_column).is_in(repertoire_ids))
        else:
            filtered = data[data[merge_column].isin(repertoire_ids)].copy()
    else:
        filtered = data

    # Aggregate by junction_aa (or could make this configurable)
    by_column = "junction_aa" if "junction_aa" in filtered.columns else "junction"

    if is_polars:
        # Group by sequence and aggregate
        merged = (
            filtered
            .group_by(by_column)
            .agg([
                pl.col("duplicate_count").sum().alias("duplicate_count"),
                pl.first("v_call").alias("v_call"),
                pl.first("d_call").alias("d_call"),
                pl.first("j_call").alias("j_call"),
                pl.first("junction_length").alias("junction_length"),
                pl.first("sequence_id").alias("sequence_id"),
            ])
        )

        # Add new repertoire_id and recalculate frequency
        merged = merged.with_columns([
            pl.lit(new_name).alias("repertoire_id"),
            (pl.col("duplicate_count") / pl.col("duplicate_count").sum())
            .alias("duplicate_frequency")
        ])

        # Sort by frequency
        merged = merged.sort("duplicate_frequency", descending=True)

    else:
        # Group by sequence and aggregate
        agg_dict = {
            "duplicate_count": "sum",
            "v_call": "first",
            "d_call": "first",
            "j_call": "first",
            "junction_length": "first",
            "sequence_id": "first"
        }

        merged = (
            filtered
            .groupby(by_column, as_index=False)
            .agg(agg_dict)
        )

        # Add new repertoire_id and recalculate frequency
        merged["repertoire_id"] = new_name
        merged["duplicate_frequency"] = (
            merged["duplicate_count"] / merged["duplicate_count"].sum()
        )

        # Sort by frequency
        merged = merged.sort_values("duplicate_frequency", ascending=False)

    return merged
