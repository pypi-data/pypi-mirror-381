"""
Tests for analysis modules.
"""

import pytest
import pandas as pd
import polars as pl
import numpy as np

from lymphoseq.analysis import clonality, diversity_metrics, common_sequences
from lymphoseq.analysis.statistics import (
    gini_coefficient, shannon_entropy, simpson_index,
    inverse_simpson_index, hill_numbers
)


class TestStatistics:
    """Test statistical functions."""

    def test_gini_coefficient(self):
        """Test Gini coefficient calculation."""
        # Perfect equality
        equal_values = [1, 1, 1, 1]
        assert gini_coefficient(equal_values) == pytest.approx(0.0, abs=1e-6)

        # Maximum inequality
        unequal_values = [1, 0, 0, 0]
        gini = gini_coefficient(unequal_values)
        assert gini > 0.5

        # Empty array
        assert gini_coefficient([]) == 0.0

    def test_shannon_entropy(self):
        """Test Shannon entropy calculation."""
        # Perfect equality (maximum entropy for 4 items)
        equal_probs = [0.25, 0.25, 0.25, 0.25]
        entropy = shannon_entropy(equal_probs)
        assert entropy == pytest.approx(2.0, abs=1e-6)

        # Maximum inequality (minimum entropy)
        unequal_probs = [1.0, 0.0, 0.0, 0.0]
        entropy = shannon_entropy(unequal_probs)
        assert entropy == pytest.approx(0.0, abs=1e-6)

        # Empty array
        assert shannon_entropy([]) == 0.0

    def test_simpson_index(self):
        """Test Simpson's index calculation."""
        # Equal probabilities
        equal_probs = [0.25, 0.25, 0.25, 0.25]
        simpson = simpson_index(equal_probs)
        assert simpson == pytest.approx(0.25, abs=1e-6)

        # Maximum dominance
        unequal_probs = [1.0, 0.0, 0.0, 0.0]
        simpson = simpson_index(unequal_probs)
        assert simpson == pytest.approx(1.0, abs=1e-6)

    def test_hill_numbers(self):
        """Test Hill numbers calculation."""
        frequencies = [0.5, 0.3, 0.2]

        # q=0: Species richness
        hill_0 = hill_numbers(frequencies, q=0)
        assert hill_0 == 3.0

        # q=1: Shannon diversity
        hill_1 = hill_numbers(frequencies, q=1)
        assert hill_1 > 0

        # q=2: Simpson diversity
        hill_2 = hill_numbers(frequencies, q=2)
        assert hill_2 > 0


class TestDiversityAnalysis:
    """Test diversity analysis functions."""

    def create_test_data(self):
        """Create test AIRR data."""
        return pd.DataFrame({
            "repertoire_id": ["sample1"] * 5 + ["sample2"] * 5,
            "junction_aa": ["CASSLVG", "CASSLEG", "CASSLVG", "CASSQPG", "CASSDTG"] * 2,
            "duplicate_count": [100, 50, 30, 20, 10, 80, 40, 25, 15, 5],
            "productive": [True] * 10,
            "v_call": ["TRBV2*01"] * 10,
            "j_call": ["TRBJ2-3*01"] * 10
        })

    def test_clonality_basic(self):
        """Test basic clonality calculation."""
        data = self.create_test_data()
        results = clonality(data, rarefy=False)

        assert isinstance(results, pd.DataFrame)
        assert len(results) == 2  # Two repertoires
        assert "clonality" in results.columns
        assert "gini_coefficient" in results.columns
        assert "unique_productive_sequences" in results.columns

    def test_clonality_polars(self):
        """Test clonality with Polars data."""
        data = self.create_test_data()
        pl_data = pl.from_pandas(data)

        results = clonality(pl_data, rarefy=False)

        assert isinstance(results, pl.DataFrame)
        assert len(results) == 2

    def test_diversity_metrics(self):
        """Test diversity metrics calculation."""
        data = self.create_test_data()
        results = diversity_metrics(data)

        assert isinstance(results, pd.DataFrame)
        assert "repertoire_id" in results.columns
        assert all(col in results.columns for col in [
            "total_sequences", "unique_productive_sequences",
            "clonality", "gini_coefficient"
        ])

    def test_common_sequences(self):
        """Test common sequences identification."""
        data = self.create_test_data()
        common = common_sequences(data, min_samples=2)

        assert isinstance(common, pd.DataFrame)
        assert "junction_aa" in common.columns
        assert "repertoire_count" in common.columns

        # Check that CASSLVG appears in both samples
        casslvg_row = common[common["junction_aa"] == "CASSLVG"]
        assert len(casslvg_row) == 1
        assert casslvg_row.iloc[0]["repertoire_count"] == 2

    def test_empty_data_handling(self):
        """Test handling of empty data."""
        empty_data = pd.DataFrame(columns=[
            "repertoire_id", "junction_aa", "duplicate_count", "productive"
        ])

        with pytest.raises(ValueError):
            clonality(empty_data)

    def test_missing_columns_error(self):
        """Test error handling for missing required columns."""
        incomplete_data = pd.DataFrame({
            "repertoire_id": ["sample1"],
            "junction_aa": ["CASSLVG"]
            # Missing duplicate_count and productive
        })

        with pytest.raises(ValueError):
            clonality(incomplete_data)

    def test_rarefaction_analysis(self):
        """Test rarefaction analysis (simplified)."""
        data = self.create_test_data()

        # Add more sequences to make rarefaction meaningful
        expanded_data = pd.concat([data] * 10, ignore_index=True)

        results = clonality(expanded_data, rarefy=True, min_count=20, iterations=5)

        assert isinstance(results, pd.DataFrame)
        assert len(results) == 2
        assert "clonality" in results.columns


class TestAnalysisIntegration:
    """Test integration between analysis components."""

    def test_full_analysis_pipeline(self):
        """Test complete analysis pipeline."""
        # Create more realistic test data
        np.random.seed(42)
        n_sequences = 1000

        data = pd.DataFrame({
            "repertoire_id": np.random.choice(["patient1", "patient2", "control1"], n_sequences),
            "junction_aa": [f"CASS{np.random.choice(['L', 'S', 'T', 'A'])}{i:03d}YF"
                           for i in range(n_sequences)],
            "duplicate_count": np.random.exponential(10, n_sequences).astype(int) + 1,
            "productive": True,
            "v_call": np.random.choice(["TRBV2*01", "TRBV3*01", "TRBV5*01"], n_sequences),
            "j_call": np.random.choice(["TRBJ2-1*01", "TRBJ2-3*01"], n_sequences)
        })

        # Run diversity analysis
        diversity_results = diversity_metrics(data)
        assert len(diversity_results) == 3  # Three repertoires

        # Find common sequences
        common_seqs = common_sequences(data, min_samples=2)
        assert len(common_seqs) >= 0  # Some sequences might be common

        # Check that all expected columns are present
        expected_diversity_cols = [
            "repertoire_id", "total_sequences", "unique_productive_sequences",
            "total_count", "clonality", "gini_coefficient"
        ]
        assert all(col in diversity_results.columns for col in expected_diversity_cols)