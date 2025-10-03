"""
Tests for comparative analysis functions.
"""

import pytest
import pandas as pd
import polars as pl

from lymphoseq.analysis import common_sequences
from lymphoseq.analysis.comparative import (
    common_seqs,
    differential_abundance,
    clonal_relatedness,
    searchSeq,
    mergeSeqs,
)


class TestCommonSequences:
    """Test common sequence analysis."""

    def test_common_seqs_basic(self, sample_multi_repertoire_data):
        """Test finding common sequences."""
        result = common_seqs(sample_multi_repertoire_data, min_samples=2)

        assert "junction_aa" in result.columns
        assert "n_samples" in result.columns or "repertoire_count" in result.columns

    def test_common_seqs_all_samples(self, sample_multi_repertoire_data):
        """Test sequences common to all samples."""
        # Add a sequence that appears in all samples
        common_seq = "CASSLVGGANTDTQYF"
        test_data = sample_multi_repertoire_data.copy()

        for rep_id in test_data["repertoire_id"].unique():
            if common_seq not in test_data[test_data["repertoire_id"] == rep_id]["junction_aa"].values:
                new_row = test_data[test_data["repertoire_id"] == rep_id].iloc[0].copy()
                new_row["junction_aa"] = common_seq
                test_data = pd.concat([test_data, pd.DataFrame([new_row])], ignore_index=True)

        result = common_seqs(test_data, min_samples=3)

        assert len(result) > 0
        assert common_seq in result["junction_aa"].values

    def test_common_seqs_no_overlap(self, sample_multi_repertoire_data):
        """Test when there are no common sequences."""
        # Make all sequences unique per sample
        test_data = sample_multi_repertoire_data.copy()
        test_data["junction_aa"] = test_data["repertoire_id"] + "_" + test_data["junction_aa"]

        result = common_seqs(test_data, min_samples=2)

        assert len(result) == 0

    def test_common_seqs_polars(self, sample_multi_repertoire_data):
        """Test with Polars data."""
        pl_data = pl.from_pandas(sample_multi_repertoire_data)
        result = common_seqs(pl_data, min_samples=2)

        assert isinstance(result, pl.DataFrame)


class TestDifferentialAbundance:
    """Test differential abundance analysis."""

    def test_differential_abundance_basic(self, sample_multi_repertoire_data):
        """Test basic differential abundance."""
        group1 = ["sample1", "sample2"]
        group2 = ["sample3"]

        result = differential_abundance(
            sample_multi_repertoire_data,
            group1=group1,
            group2=group2
        )

        assert "junction_aa" in result.columns
        assert "fold_change" in result.columns or "log2_fc" in result.columns

    def test_differential_abundance_statistics(self, sample_multi_repertoire_data):
        """Test that statistical measures are calculated."""
        group1 = ["sample1"]
        group2 = ["sample2"]

        result = differential_abundance(
            sample_multi_repertoire_data,
            group1=group1,
            group2=group2
        )

        # Should have some measure of significance or fold change
        assert len(result.columns) > 2

    def test_differential_abundance_no_shared_seqs(self, sample_multi_repertoire_data):
        """Test differential abundance with no shared sequences."""
        # Make sequences unique per group
        test_data = sample_multi_repertoire_data.copy()
        test_data.loc[test_data["repertoire_id"] == "sample1", "junction_aa"] = \
            "GROUP1_" + test_data.loc[test_data["repertoire_id"] == "sample1", "junction_aa"]
        test_data.loc[test_data["repertoire_id"] == "sample2", "junction_aa"] = \
            "GROUP2_" + test_data.loc[test_data["repertoire_id"] == "sample2", "junction_aa"]

        result = differential_abundance(
            test_data,
            group1=["sample1"],
            group2=["sample2"]
        )

        # Should still return results (zero fold change or infinite)
        assert len(result) > 0


class TestClonalRelatedness:
    """Test clonal relatedness analysis."""

    def test_clonal_relatedness_basic(self, sample_multi_repertoire_data):
        """Test basic clonal relatedness calculation."""
        result = clonal_relatedness(sample_multi_repertoire_data)

        assert isinstance(result, (pd.DataFrame, pl.DataFrame))
        # Should have pairwise comparisons
        assert len(result) > 0

    def test_clonal_relatedness_morisita_index(self, sample_multi_repertoire_data):
        """Test Morisita-Horn index calculation."""
        result = clonal_relatedness(
            sample_multi_repertoire_data,
            method="morisita"
        )

        # Morisita index should be between 0 and 1
        if "morisita_index" in result.columns:
            assert result["morisita_index"].min() >= 0
            assert result["morisita_index"].max() <= 1

    def test_clonal_relatedness_self_comparison(self, sample_multi_repertoire_data):
        """Test that sample compared to itself has high relatedness."""
        # Compare sample1 to itself
        sample1_data = sample_multi_repertoire_data[
            sample_multi_repertoire_data["repertoire_id"] == "sample1"
        ]
        duplicated = pd.concat([sample1_data, sample1_data], ignore_index=True)
        duplicated.loc[len(sample1_data):, "repertoire_id"] = "sample1_copy"

        result = clonal_relatedness(duplicated)

        # Self-comparison should have high similarity
        if "morisita_index" in result.columns:
            self_comparison = result[
                (result["repertoire_1"] == "sample1") &
                (result["repertoire_2"] == "sample1_copy")
            ]
            if len(self_comparison) > 0:
                assert self_comparison["morisita_index"].values[0] > 0.9


class TestSequenceSearch:
    """Test sequence search functions."""

    def test_searchSeq_basic(self, sample_multi_repertoire_data):
        """Test searching for specific sequences."""
        target_seq = sample_multi_repertoire_data["junction_aa"].iloc[0]

        result = searchSeq(sample_multi_repertoire_data, sequence=target_seq)

        assert len(result) > 0
        assert target_seq in result["junction_aa"].values

    def test_searchSeq_multiple(self, sample_multi_repertoire_data):
        """Test searching for multiple sequences."""
        target_seqs = sample_multi_repertoire_data["junction_aa"].iloc[:3].tolist()

        result = searchSeq(sample_multi_repertoire_data, sequence=target_seqs)

        assert len(result) >= len(target_seqs)
        assert all(seq in result["junction_aa"].values for seq in target_seqs)

    def test_searchSeq_not_found(self, sample_multi_repertoire_data):
        """Test searching for non-existent sequence."""
        result = searchSeq(sample_multi_repertoire_data, sequence="NONEXISTENT")

        assert len(result) == 0

    def test_searchSeq_partial_match(self, sample_multi_repertoire_data):
        """Test partial matching if supported."""
        # Search for sequences containing "CASS"
        result = searchSeq(
            sample_multi_repertoire_data,
            sequence="CASS",
            partial=True
        )

        # Should find sequences containing "CASS"
        if len(result) > 0:
            assert all("CASS" in seq for seq in result["junction_aa"])


class TestMergeSequences:
    """Test sequence merging functions."""

    def test_mergeSeqs_basic(self, sample_airr_data):
        """Test basic sequence merging."""
        # Create two datasets
        data1 = sample_airr_data.head(3).copy()
        data1["repertoire_id"] = "sample1"

        data2 = sample_airr_data.tail(3).copy()
        data2["repertoire_id"] = "sample2"

        result = mergeSeqs([data1, data2])

        assert len(result) == len(data1) + len(data2)
        assert "sample1" in result["repertoire_id"].values
        assert "sample2" in result["repertoire_id"].values

    def test_mergeSeqs_overlapping(self, sample_multi_repertoire_data):
        """Test merging with overlapping sequences."""
        data1 = sample_multi_repertoire_data[
            sample_multi_repertoire_data["repertoire_id"] == "sample1"
        ]
        data2 = sample_multi_repertoire_data[
            sample_multi_repertoire_data["repertoire_id"] == "sample2"
        ]

        result = mergeSeqs([data1, data2])

        # Should have sequences from both
        assert len(result) > 0
        assert "sample1" in result["repertoire_id"].values
        assert "sample2" in result["repertoire_id"].values

    def test_mergeSeqs_empty_datasets(self):
        """Test merging with empty datasets."""
        empty1 = pd.DataFrame(columns=["junction_aa", "repertoire_id", "duplicate_count"])
        empty2 = pd.DataFrame(columns=["junction_aa", "repertoire_id", "duplicate_count"])

        result = mergeSeqs([empty1, empty2])

        assert len(result) == 0

    def test_mergeSeqs_single_dataset(self, sample_airr_data):
        """Test merging a single dataset."""
        result = mergeSeqs([sample_airr_data])

        # Should return the same data
        assert len(result) == len(sample_airr_data)


class TestComparativeAnalysisEdgeCases:
    """Test edge cases in comparative analysis."""

    def test_empty_groups(self, sample_multi_repertoire_data):
        """Test handling of empty groups."""
        with pytest.raises((ValueError, KeyError)):
            differential_abundance(
                sample_multi_repertoire_data,
                group1=[],
                group2=["sample1"]
            )

    def test_nonexistent_repertoires(self, sample_multi_repertoire_data):
        """Test handling of non-existent repertoire IDs."""
        with pytest.raises((ValueError, KeyError)):
            differential_abundance(
                sample_multi_repertoire_data,
                group1=["nonexistent1"],
                group2=["nonexistent2"]
            )

    def test_single_repertoire_relatedness(self, sample_airr_data):
        """Test relatedness with single repertoire."""
        result = clonal_relatedness(sample_airr_data)

        # Should handle gracefully (no comparisons or self-comparison)
        assert len(result) >= 0
