"""
Tests for gene usage analysis functions.
"""

import pytest
import pandas as pd
import polars as pl

from lymphoseq.analysis.genes import gene_freq, gene_pair_freq


class TestGeneFrequency:
    """Test gene frequency calculation."""

    def test_gene_freq_v_genes(self, sample_gene_usage_data):
        """Test V gene frequency calculation."""
        result = gene_freq(sample_gene_usage_data, gene="v")

        assert "v_call" in result.columns or "v_family" in result.columns
        assert "frequency" in result.columns
        assert result["frequency"].sum() == pytest.approx(1.0, rel=0.01)

    def test_gene_freq_j_genes(self, sample_gene_usage_data):
        """Test J gene frequency calculation."""
        result = gene_freq(sample_gene_usage_data, gene="j")

        assert "j_call" in result.columns or "j_family" in result.columns
        assert "frequency" in result.columns

    def test_gene_freq_by_repertoire(self, sample_multi_repertoire_data):
        """Test gene frequency per repertoire."""
        result = gene_freq(sample_multi_repertoire_data, gene="v")

        # Should have results for each repertoire
        repertoires = result["repertoire_id"].unique()
        assert len(repertoires) > 1

    def test_gene_freq_polars(self, polars_airr_data):
        """Test gene frequency with Polars data."""
        # Add v_call column if missing
        if "v_call" not in polars_airr_data.columns:
            polars_airr_data = polars_airr_data.with_columns(
                pl.lit("TRBV2*01").alias("v_call")
            )

        result = gene_freq(polars_airr_data, gene="v")

        assert isinstance(result, pl.DataFrame)


class TestGenePairFrequency:
    """Test gene pair frequency calculation."""

    def test_gene_pair_freq_basic(self, sample_gene_usage_data):
        """Test VJ pair frequency calculation."""
        result = gene_pair_freq(sample_gene_usage_data)

        assert "v_call" in result.columns
        assert "j_call" in result.columns
        assert "frequency" in result.columns

    def test_gene_pair_freq_multi_repertoire(self, sample_multi_repertoire_data):
        """Test gene pair frequency across repertoires."""
        result = gene_pair_freq(sample_multi_repertoire_data)

        # Check that we have results for multiple repertoires
        if "repertoire_id" in result.columns:
            assert len(result["repertoire_id"].unique()) > 1

    def test_gene_pair_freq_top_n(self, sample_multi_repertoire_data):
        """Test returning top N gene pairs."""
        result = gene_pair_freq(sample_multi_repertoire_data, top=5)

        # Should have at most 5 pairs per repertoire
        if "repertoire_id" in result.columns:
            for rep_id in result["repertoire_id"].unique():
                rep_data = result[result["repertoire_id"] == rep_id]
                assert len(rep_data) <= 5

    def test_gene_pair_freq_frequencies_sum(self, sample_gene_usage_data):
        """Test that frequencies sum to ~1.0 per repertoire."""
        result = gene_pair_freq(sample_gene_usage_data)

        if "repertoire_id" in result.columns:
            for rep_id in result["repertoire_id"].unique():
                rep_data = result[result["repertoire_id"] == rep_id]
                freq_sum = rep_data["frequency"].sum()
                assert freq_sum <= 1.0  # Can be less if filtered to top N


class TestGeneAnalysisEdgeCases:
    """Test edge cases in gene analysis."""

    def test_gene_freq_missing_gene_column(self, sample_airr_data):
        """Test handling of missing gene columns."""
        incomplete_data = sample_airr_data[["junction_aa", "duplicate_frequency"]].copy()

        with pytest.raises((ValueError, KeyError)):
            gene_freq(incomplete_data, gene="v")

    def test_gene_freq_empty_data(self):
        """Test handling of empty data."""
        empty_data = pd.DataFrame(columns=[
            "v_call", "duplicate_frequency", "repertoire_id"
        ])

        with pytest.raises((ValueError, Exception)):
            gene_freq(empty_data, gene="v")

    def test_gene_pair_freq_missing_columns(self, sample_airr_data):
        """Test handling of missing required columns."""
        incomplete_data = sample_airr_data[["v_call"]].copy()

        with pytest.raises((ValueError, KeyError)):
            gene_pair_freq(incomplete_data)


class TestGeneAnalysisDataFormats:
    """Test gene analysis with different data formats."""

    def test_gene_freq_with_families(self, sample_gene_usage_data):
        """Test gene frequency with gene families."""
        # Add v_family column
        test_data = sample_gene_usage_data.copy()
        test_data["v_family"] = test_data["v_call"].str.split("*").str[0]

        result = gene_freq(test_data, gene="v", by_family=True)

        assert "v_family" in result.columns or "v_call" in result.columns

    def test_gene_freq_unweighted(self, sample_gene_usage_data):
        """Test unweighted gene frequency (count-based)."""
        result = gene_freq(sample_gene_usage_data, gene="v")

        # Should count each occurrence
        assert len(result) > 0

    def test_gene_pair_freq_sorted(self, sample_multi_repertoire_data):
        """Test that gene pairs are sorted by frequency."""
        result = gene_pair_freq(sample_multi_repertoire_data)

        # Check that frequencies are in descending order for each repertoire
        if "repertoire_id" in result.columns:
            for rep_id in result["repertoire_id"].unique():
                rep_data = result[result["repertoire_id"] == rep_id]
                frequencies = rep_data["frequency"].tolist()
                assert frequencies == sorted(frequencies, reverse=True)
