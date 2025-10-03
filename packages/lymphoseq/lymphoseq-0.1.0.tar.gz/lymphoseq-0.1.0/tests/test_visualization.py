"""
Tests for visualization functions.
"""

import pytest
import pandas as pd
import polars as pl
import plotly.graph_objects as go

from lymphoseq.visualization import (
    plot_clonality,
    plot_diversity,
    plot_rarefaction,
    plot_gene_usage,
    plot_top_seqs,
    plot_lorenz_curve,
    common_seqs_venn,
    plot_track,
)


@pytest.mark.visualization
class TestBasicPlots:
    """Test basic plotting functions."""

    def test_plot_clonality(self, sample_multi_repertoire_data):
        """Test clonality plotting."""
        fig = plot_clonality(sample_multi_repertoire_data)

        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0

    def test_plot_diversity(self, sample_multi_repertoire_data):
        """Test diversity plotting."""
        fig = plot_diversity(sample_multi_repertoire_data)

        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0

    def test_plot_top_seqs(self, sample_airr_data):
        """Test top sequences plotting."""
        fig = plot_top_seqs(sample_airr_data, top=5)

        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0

    def test_plot_lorenz_curve(self, sample_airr_data):
        """Test Lorenz curve plotting."""
        fig = plot_lorenz_curve(sample_airr_data)

        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0

    def test_plot_gene_usage(self, sample_gene_usage_data):
        """Test gene usage plotting."""
        fig = plot_gene_usage(sample_gene_usage_data)

        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0


@pytest.mark.visualization
class TestAdvancedPlots:
    """Test advanced plotting functions."""

    def test_common_seqs_venn_two_samples(self, sample_multi_repertoire_data):
        """Test Venn diagram for 2 samples."""
        fig = common_seqs_venn(
            sample_multi_repertoire_data,
            repertoire_ids=["sample1", "sample2"]
        )

        assert isinstance(fig, go.Figure)

    def test_common_seqs_venn_three_samples(self, sample_multi_repertoire_data):
        """Test Venn diagram for 3 samples."""
        fig = common_seqs_venn(
            sample_multi_repertoire_data,
            repertoire_ids=["sample1", "sample2", "sample3"]
        )

        assert isinstance(fig, go.Figure)

    def test_plot_track(self, sample_multi_repertoire_data):
        """Test clone tracking plot."""
        # Ensure we have common sequences across samples
        common_seq = sample_multi_repertoire_data["junction_aa"].iloc[0]

        # Make sure it appears in multiple samples
        test_data = sample_multi_repertoire_data.copy()
        for i, rep_id in enumerate(["sample1", "sample2", "sample3"]):
            if rep_id not in test_data[test_data["junction_aa"] == common_seq]["repertoire_id"].values:
                new_row = test_data[test_data["repertoire_id"] == rep_id].iloc[0].copy()
                new_row["junction_aa"] = common_seq
                test_data = pd.concat([test_data, pd.DataFrame([new_row])], ignore_index=True)

        fig = plot_track(test_data, sequences=[common_seq])

        assert isinstance(fig, go.Figure)

    def test_plot_rarefaction(self, sample_multi_repertoire_data):
        """Test rarefaction curve plotting."""
        fig = plot_rarefaction(sample_multi_repertoire_data)

        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0


@pytest.mark.visualization
class TestPlotCustomization:
    """Test plot customization options."""

    def test_plot_with_custom_title(self, sample_airr_data):
        """Test custom title."""
        fig = plot_top_seqs(sample_airr_data, title="Custom Title")

        assert "Custom Title" in fig.layout.title.text

    def test_plot_with_custom_dimensions(self, sample_airr_data):
        """Test custom width and height."""
        fig = plot_top_seqs(sample_airr_data, width=800, height=600)

        assert fig.layout.width == 800
        assert fig.layout.height == 600

    def test_plot_clonality_with_options(self, sample_multi_repertoire_data):
        """Test clonality plot with various options."""
        fig = plot_clonality(
            sample_multi_repertoire_data,
            title="Custom Clonality",
            width=900,
            height=700
        )

        assert isinstance(fig, go.Figure)
        assert fig.layout.width == 900


@pytest.mark.visualization
class TestPlotErrorHandling:
    """Test error handling in plotting functions."""

    def test_empty_data(self):
        """Test plotting with empty data."""
        empty_data = pd.DataFrame(columns=[
            "repertoire_id", "junction_aa", "duplicate_count"
        ])

        with pytest.raises((ValueError, Exception)):
            plot_clonality(empty_data)

    def test_missing_columns(self, sample_airr_data):
        """Test plotting with missing required columns."""
        incomplete_data = sample_airr_data[["junction_aa", "duplicate_count"]].copy()

        with pytest.raises((ValueError, KeyError)):
            plot_clonality(incomplete_data)

    def test_venn_too_many_samples(self, sample_multi_repertoire_data):
        """Test Venn diagram with too many samples."""
        # Venn diagrams only support 2-3 samples
        with pytest.raises((ValueError, NotImplementedError)):
            common_seqs_venn(
                sample_multi_repertoire_data,
                repertoire_ids=["sample1", "sample2", "sample3", "sample4"]
            )


@pytest.mark.visualization
class TestPlotTypes:
    """Test different plot types and backends."""

    def test_plot_returns_figure_object(self, sample_airr_data):
        """Test that plots return proper figure objects."""
        fig = plot_top_seqs(sample_airr_data)

        # Should be a Plotly figure
        assert hasattr(fig, 'data')
        assert hasattr(fig, 'layout')
        assert hasattr(fig, 'show')

    def test_plot_with_polars_data(self, polars_airr_data):
        """Test plotting with Polars data."""
        fig = plot_top_seqs(polars_airr_data)

        assert isinstance(fig, go.Figure)

    def test_multiple_plots_same_data(self, sample_multi_repertoire_data):
        """Test creating multiple plots from same data."""
        fig1 = plot_clonality(sample_multi_repertoire_data)
        fig2 = plot_diversity(sample_multi_repertoire_data)
        fig3 = plot_top_seqs(sample_multi_repertoire_data)

        assert all(isinstance(fig, go.Figure) for fig in [fig1, fig2, fig3])
        assert fig1 is not fig2
        assert fig2 is not fig3
