"""
Tests for sequence filtering and chain merging functions.
"""

import pytest
import pandas as pd
import polars as pl

from lymphoseq.sequence import (
    top_seqs,
    productive_seq,
    unique_seqs,
    remove_seq,
    merge_chains,
    split_chains,
)


class TestSequenceFiltering:
    """Test sequence filtering functions."""

    def test_top_seqs_pandas(self, sample_airr_data):
        """Test top_seqs with pandas data."""
        result = top_seqs(sample_airr_data, top=3)

        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3
        assert result["duplicate_count"].iloc[0] >= result["duplicate_count"].iloc[1]

    def test_top_seqs_polars(self, polars_airr_data):
        """Test top_seqs with polars data."""
        result = top_seqs(polars_airr_data, top=3)

        assert isinstance(result, pl.DataFrame)
        assert len(result) == 3

    def test_top_seqs_by_repertoire(self, sample_multi_repertoire_data):
        """Test top_seqs per repertoire."""
        result = top_seqs(sample_multi_repertoire_data, top=10)

        # Should have at most 10 sequences per repertoire
        for rep_id in result["repertoire_id"].unique():
            rep_seqs = result[result["repertoire_id"] == rep_id]
            assert len(rep_seqs) <= 10

    def test_productive_seq(self, sample_airr_data):
        """Test filtering for productive sequences."""
        # Add some non-productive sequences
        test_data = sample_airr_data.copy()
        test_data.loc[3, "productive"] = False
        test_data.loc[4, "productive"] = False

        result = productive_seq(test_data)

        assert len(result) == 3
        # Check productive column exists and all values are True
        assert "productive" in result.columns
        assert all(result["productive"] == True)

    def test_unique_seqs(self, sample_multi_repertoire_data):
        """Test unique sequence extraction."""
        # Add duplicate sequences
        test_data = pd.concat([
            sample_multi_repertoire_data,
            sample_multi_repertoire_data.head(10)
        ], ignore_index=True)

        result = unique_seqs(test_data)

        # Check that duplicates are removed
        assert len(result) < len(test_data)
        assert result["junction_aa"].nunique() == len(result)

    def test_remove_seq(self, sample_airr_data):
        """Test sequence removal."""
        seqs_to_remove = ["CASSLVGGANTDTQYF", "CASSLEGANTDTQYF"]

        result = remove_seq(sample_airr_data, seqs_to_remove)

        assert len(result) == 3  # 5 - 2 = 3
        assert not any(result["junction_aa"].isin(seqs_to_remove))

    def test_remove_seq_multiple_repertoires(self, sample_multi_repertoire_data):
        """Test sequence removal across multiple repertoires."""
        # Find a sequence that appears in the data
        seq_to_remove = sample_multi_repertoire_data["junction_aa"].iloc[0]

        result = remove_seq(sample_multi_repertoire_data, [seq_to_remove])

        # Sequence should be removed from all repertoires
        assert seq_to_remove not in result["junction_aa"].values


class TestChainMerging:
    """Test chain merging functions for 10X data."""

    def test_merge_chains_basic(self, sample_10x_data):
        """Test basic chain merging."""
        result = merge_chains(sample_10x_data)

        assert "junction_aa" in result.columns
        assert ":" in result["junction_aa"].iloc[0]
        assert "duplicate_count" in result.columns
        assert "productive" in result.columns

    def test_merge_chains_polars(self, sample_10x_data):
        """Test chain merging with Polars data."""
        pl_data = pl.from_pandas(sample_10x_data)
        result = merge_chains(pl_data)

        assert isinstance(result, pl.DataFrame)
        assert "junction_aa" in result.columns

    def test_merge_chains_custom_separator(self, sample_10x_data):
        """Test merging with custom separator."""
        result = merge_chains(sample_10x_data, separator=";")

        assert ";" in result["junction_aa"].iloc[0]
        assert ":" not in result["junction_aa"].iloc[0]

    def test_merge_chains_keep_columns(self, sample_10x_data):
        """Test keeping original chain columns."""
        result = merge_chains(sample_10x_data, keep_chain_columns=True)

        assert "tra_junction_aa" in result.columns
        assert "trb_junction_aa" in result.columns
        assert "tra_v_call" in result.columns
        assert "trb_v_call" in result.columns

    def test_merge_chains_no_aggregate(self, sample_10x_data):
        """Test merging without aggregation."""
        result = merge_chains(sample_10x_data, aggregate=False)

        assert len(result) == len(sample_10x_data)
        assert "cell_id" in result.columns

    def test_merge_chains_with_duplicates(self, sample_10x_data):
        """Test aggregation with duplicate sequences."""
        # Duplicate the first two rows
        duplicated = pd.concat([sample_10x_data, sample_10x_data.head(2)], ignore_index=True)

        result = merge_chains(duplicated, aggregate=True)

        # Should have fewer rows due to aggregation
        assert len(result) < len(duplicated)

        # Check that duplicate counts are correct
        assert result["duplicate_count"].max() > 1

    def test_merge_chains_creates_valid_format(self, sample_10x_data):
        """Test that merged data is compatible with analysis functions."""
        from lymphoseq.analysis import clonality

        merged = merge_chains(sample_10x_data)

        # Should be able to calculate clonality
        result = clonality(merged)
        assert len(result) > 0

    def test_split_chains(self, sample_10x_data):
        """Test splitting merged chains."""
        merged = merge_chains(sample_10x_data)
        split = split_chains(merged)

        assert "tra_junction_aa" in split.columns
        assert "trb_junction_aa" in split.columns

        # Check that splitting recovers original sequences
        original_tra = sample_10x_data["tra_junction_aa"].iloc[0]
        split_tra = split["tra_junction_aa"].iloc[0] if isinstance(split, pd.DataFrame) else split["tra_junction_aa"][0]

        # Should match (order might differ due to aggregation)
        assert original_tra in split["tra_junction_aa"].values if isinstance(split, pd.DataFrame) else original_tra in split["tra_junction_aa"].to_list()

    def test_split_chains_polars(self, sample_10x_data):
        """Test splitting with Polars data."""
        pl_data = pl.from_pandas(sample_10x_data)
        merged = merge_chains(pl_data)
        split = split_chains(merged)

        assert isinstance(split, pl.DataFrame)
        assert "tra_junction_aa" in split.columns

    def test_merge_chains_missing_columns(self):
        """Test error handling for missing required columns."""
        invalid_data = pd.DataFrame({
            "cell_id": ["cell1", "cell2"],
            "repertoire_id": ["sample1", "sample1"],
            "junction_aa": ["CASSLVG", "CASSLEG"],  # Wrong column name
        })

        with pytest.raises(ValueError):
            merge_chains(invalid_data)

    def test_merge_chains_empty_data(self):
        """Test handling of empty data."""
        empty_data = pd.DataFrame(columns=[
            "tra_junction_aa", "trb_junction_aa", "repertoire_id"
        ])

        with pytest.raises(ValueError):
            merge_chains(empty_data)


class TestSequenceFilteringEdgeCases:
    """Test edge cases in sequence filtering."""

    def test_top_seqs_more_than_available(self, sample_airr_data):
        """Test requesting more sequences than available."""
        result = top_seqs(sample_airr_data, top=100)

        # Should return all available sequences
        assert len(result) == len(sample_airr_data)

    def test_top_seqs_zero(self, sample_airr_data):
        """Test requesting zero sequences."""
        result = top_seqs(sample_airr_data, top=0)

        assert len(result) == 0

    def test_productive_seq_all_productive(self, sample_airr_data):
        """Test filtering when all sequences are productive."""
        result = productive_seq(sample_airr_data)

        assert len(result) == len(sample_airr_data)

    def test_productive_seq_none_productive(self, sample_airr_data):
        """Test filtering when no sequences are productive."""
        test_data = sample_airr_data.copy()
        test_data["productive"] = False

        result = productive_seq(test_data)

        assert len(result) == 0

    def test_remove_seq_empty_list(self, sample_airr_data):
        """Test removing empty list of sequences."""
        result = remove_seq(sample_airr_data, [])

        # Should return unchanged data
        assert len(result) == len(sample_airr_data)

    def test_remove_seq_nonexistent(self, sample_airr_data):
        """Test removing sequences that don't exist."""
        result = remove_seq(sample_airr_data, ["NONEXISTENT", "ALSONONEXISTENT"])

        # Should return unchanged data
        assert len(result) == len(sample_airr_data)
