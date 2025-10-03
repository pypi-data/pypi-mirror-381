"""
Plotting functions for AIRR-seq data visualization.

Provides interactive and publication-ready plots using Plotly and Seaborn.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import polars as pl
import numpy as np
from typing import Union, Optional, List, Dict, Any


def plot_clonality(
    data: Union[pl.DataFrame, pd.DataFrame],
    x_col: str = "repertoire_id",
    y_col: str = "clonality",
    color_col: Optional[str] = None,
    title: str = "Clonality Analysis",
    width: int = 800,
    height: int = 600
) -> go.Figure:
    """
    Create an interactive clonality plot.

    Args:
        data: Data frame with clonality results
        x_col: Column for x-axis (usually repertoire_id)
        y_col: Column for y-axis (clonality values)
        color_col: Optional column for color coding
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/")
        >>> diversity = ls.clonality(data)
        >>> fig = ls.plot_clonality(diversity)
        >>> fig.show()
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Create the plot
    if color_col and color_col in df.columns:
        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            color=color_col,
            title=title,
            labels={
                x_col: "Repertoire",
                y_col: "Clonality",
                color_col: color_col.replace("_", " ").title()
            }
        )
    else:
        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            title=title,
            labels={
                x_col: "Repertoire",
                y_col: "Clonality"
            }
        )

    # Customize layout
    fig.update_layout(
        width=width,
        height=height,
        xaxis_title="Repertoire ID",
        yaxis_title="Clonality",
        showlegend=bool(color_col),
        hovermode="x unified",
        template="plotly_white"
    )

    # Rotate x-axis labels if many repertoires
    if len(df) > 10:
        fig.update_xaxes(tickangle=45)

    return fig


def plot_diversity(
    data: Union[pl.DataFrame, pd.DataFrame],
    metrics: List[str] = ["clonality", "gini_coefficient", "unique_productive_sequences"],
    title: str = "Diversity Metrics Comparison",
    width: int = 1000,
    height: int = 600
) -> go.Figure:
    """
    Create a multi-metric diversity comparison plot.

    Args:
        data: Data frame with diversity results
        metrics: List of metrics to plot
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with subplots

    Examples:
        >>> fig = ls.plot_diversity(diversity_results)
        >>> fig.show()
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Check which metrics are available
    available_metrics = [m for m in metrics if m in df.columns]
    if not available_metrics:
        raise ValueError(f"None of the specified metrics {metrics} found in data")

    # Create subplots
    from plotly.subplots import make_subplots

    n_metrics = len(available_metrics)
    cols = min(3, n_metrics)
    rows = (n_metrics + cols - 1) // cols

    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=available_metrics,
        vertical_spacing=0.1,
        horizontal_spacing=0.1
    )

    # Add plots for each metric
    for i, metric in enumerate(available_metrics):
        row = i // cols + 1
        col = i % cols + 1

        fig.add_trace(
            go.Bar(
                x=df["repertoire_id"],
                y=df[metric],
                name=metric,
                showlegend=False,
                marker_color=px.colors.qualitative.Set1[i % len(px.colors.qualitative.Set1)]
            ),
            row=row,
            col=col
        )

    # Update layout
    fig.update_layout(
        width=width,
        height=height,
        title_text=title,
        template="plotly_white"
    )

    return fig


def plot_common_sequences(
    data: Union[pl.DataFrame, pd.DataFrame],
    top_n: int = 20,
    title: str = "Common Sequences Across Repertoires",
    width: int = 800,
    height: int = 600
) -> go.Figure:
    """
    Plot the most common sequences found across repertoires.

    Args:
        data: Data frame with common sequences
        top_n: Number of top sequences to show
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object

    Examples:
        >>> common = ls.common_sequences(data)
        >>> fig = ls.plot_common_sequences(common)
        >>> fig.show()
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Get top N sequences
    df_top = df.head(top_n).copy()

    # Truncate long sequences for display
    df_top["sequence_display"] = df_top["junction_aa"].apply(
        lambda x: x[:15] + "..." if len(str(x)) > 15 else str(x)
    )

    # Create horizontal bar plot
    fig = go.Figure(data=[
        go.Bar(
            y=df_top["sequence_display"],
            x=df_top["repertoire_count"],
            orientation='h',
            text=df_top["total_count"],
            textposition="outside",
            hovertemplate=(
                "Sequence: %{customdata[0]}<br>"
                "Repertoires: %{x}<br>"
                "Total count: %{text}<br>"
                "<extra></extra>"
            ),
            customdata=df_top[["junction_aa"]]
        )
    ])

    fig.update_layout(
        width=width,
        height=height,
        title=title,
        xaxis_title="Number of Repertoires",
        yaxis_title="CDR3 Sequence",
        template="plotly_white",
        yaxis=dict(autorange="reversed")  # Show most common at top
    )

    return fig


def plot_repertoire_comparison(
    data: Union[pl.DataFrame, pd.DataFrame],
    x_metric: str = "unique_productive_sequences",
    y_metric: str = "clonality",
    color_col: Optional[str] = None,
    size_col: Optional[str] = "total_count",
    title: str = "Repertoire Comparison",
    width: int = 800,
    height: int = 600
) -> go.Figure:
    """
    Create a scatter plot comparing repertoires across two metrics.

    Args:
        data: Data frame with repertoire metrics
        x_metric: Metric for x-axis
        y_metric: Metric for y-axis
        color_col: Optional column for color coding
        size_col: Optional column for bubble size
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object

    Examples:
        >>> fig = ls.plot_repertoire_comparison(
        ...     diversity_results,
        ...     x_metric="unique_productive_sequences",
        ...     y_metric="clonality"
        ... )
        >>> fig.show()
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Check required columns
    required_cols = [x_metric, y_metric]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Create scatter plot
    scatter_kwargs = {
        "data_frame": df,
        "x": x_metric,
        "y": y_metric,
        "hover_name": "repertoire_id" if "repertoire_id" in df.columns else None,
        "title": title,
        "labels": {
            x_metric: x_metric.replace("_", " ").title(),
            y_metric: y_metric.replace("_", " ").title()
        }
    }

    if color_col and color_col in df.columns:
        scatter_kwargs["color"] = color_col

    if size_col and size_col in df.columns:
        scatter_kwargs["size"] = size_col

    fig = px.scatter(**scatter_kwargs)

    # Customize layout
    fig.update_layout(
        width=width,
        height=height,
        template="plotly_white"
    )

    return fig


def plot_rarefaction(
    data: Union[pl.DataFrame, pd.DataFrame],
    color_by: str = "repertoire_id",
    show_ci: bool = True,
    title: str = "Rarefaction Curves",
    width: int = 900,
    height: int = 600
) -> go.Figure:
    """
    Plot rarefaction curves showing diversity vs sampling depth.

    Creates line plots showing how unique sequences increase with sequencing
    depth, with optional confidence intervals. Helps assess sampling
    completeness and compare diversity across samples.

    Args:
        data: DataFrame from rarefaction_curve() function. Must contain:
            'sample_size', 'unique_sequences', 'repertoire_id' columns.
        color_by: Column to color lines by (default: "repertoire_id")
        show_ci: Whether to show confidence intervals (default: True)
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with rarefaction curves

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> rarefaction = ls.rarefaction_curve(data, iterations=100)
        >>> fig = ls.plot_rarefaction(rarefaction)
        >>> fig.show()

        >>> # Customize appearance
        >>> fig = ls.plot_rarefaction(
        ...     rarefaction,
        ...     show_ci=False,
        ...     title="Sample Diversity Rarefaction"
        ... )
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Validate required columns
    required_cols = ["sample_size", "unique_sequences", color_by]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    fig = go.Figure()

    # Get unique groups
    groups = df[color_by].unique()
    colors = px.colors.qualitative.Plotly

    for i, group in enumerate(groups):
        group_data = df[df[color_by] == group].sort_values("sample_size")
        color = colors[i % len(colors)]

        # Main line
        fig.add_trace(go.Scatter(
            x=group_data["sample_size"],
            y=group_data["unique_sequences"],
            mode="lines+markers",
            name=str(group),
            line=dict(color=color, width=2),
            marker=dict(size=6),
            hovertemplate=(
                f"{color_by}: {group}<br>"
                "Sample size: %{x}<br>"
                "Unique sequences: %{y:.1f}<br>"
                "<extra></extra>"
            )
        ))

        # Add confidence interval if available and requested
        if show_ci and "unique_sequences_sd" in df.columns:
            y_upper = group_data["unique_sequences"] + group_data["unique_sequences_sd"]
            y_lower = group_data["unique_sequences"] - group_data["unique_sequences_sd"]

            # Upper bound
            fig.add_trace(go.Scatter(
                x=group_data["sample_size"],
                y=y_upper,
                mode="lines",
                line=dict(width=0),
                showlegend=False,
                hoverinfo="skip"
            ))

            # Lower bound (creates fill)
            fig.add_trace(go.Scatter(
                x=group_data["sample_size"],
                y=y_lower,
                mode="lines",
                line=dict(width=0),
                fillcolor=color.replace("rgb", "rgba").replace(")", ", 0.2)"),
                fill="tonexty",
                showlegend=False,
                hoverinfo="skip"
            ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Sample Size (Number of Reads)",
        yaxis_title="Unique Sequences",
        width=width,
        height=height,
        template="plotly_white",
        hovermode="x unified",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )

    return fig


def plot_gene_usage(
    data: Union[pl.DataFrame, pd.DataFrame],
    top_n: int = 15,
    facet_by: Optional[str] = None,
    title: str = "Gene Usage Frequencies",
    width: int = 900,
    height: int = 600
) -> go.Figure:
    """
    Plot V, D, or J gene usage frequencies.

    Creates horizontal bar plots showing the most frequent genes, optionally
    faceted by repertoire or condition.

    Args:
        data: DataFrame from gene_freq() function. Must contain 'gene_name',
            'frequency', and 'repertoire_id' columns.
        top_n: Number of top genes to show per group (default: 15)
        facet_by: Column to create separate subplots (default: None)
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with gene usage bars

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> v_usage = ls.gene_freq(data, gene="v")
        >>> fig = ls.plot_gene_usage(v_usage, top_n=20)
        >>> fig.show()

        >>> # Facet by repertoire
        >>> fig = ls.plot_gene_usage(v_usage, facet_by="repertoire_id")
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Validate required columns
    required_cols = ["gene_name", "frequency", "repertoire_id"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    if facet_by and facet_by in df.columns:
        # Create faceted plot
        groups = df[facet_by].unique()
        n_groups = len(groups)

        from plotly.subplots import make_subplots

        fig = make_subplots(
            rows=1,
            cols=n_groups,
            subplot_titles=[str(g) for g in groups],
            horizontal_spacing=0.05
        )

        for i, group in enumerate(groups):
            group_data = (
                df[df[facet_by] == group]
                .nlargest(top_n, "frequency")
                .sort_values("frequency")
            )

            fig.add_trace(
                go.Bar(
                    y=group_data["gene_name"],
                    x=group_data["frequency"],
                    orientation="h",
                    name=str(group),
                    showlegend=False,
                    marker_color=px.colors.qualitative.Set2[i % len(px.colors.qualitative.Set2)],
                    hovertemplate=(
                        "Gene: %{y}<br>"
                        "Frequency: %{x:.3f}<br>"
                        "<extra></extra>"
                    )
                ),
                row=1,
                col=i+1
            )

            fig.update_xaxes(title_text="Frequency" if i == 0 else "", row=1, col=i+1)
            fig.update_yaxes(title_text="Gene", row=1, col=i+1)

    else:
        # Single plot
        df_top = df.nlargest(top_n, "frequency").sort_values("frequency")

        fig = go.Figure()
        for rep, col in zip(df_top["repertoire_id"].unique(), px.colors.qualitative.Set2):
            filtered_df = df_top[df_top["repertoire_id"] == rep]
            filtered_df["trace_name"] = rep
            fig.add_trace(
                go.Bar(
                    y=filtered_df["gene_name"],
                    x=filtered_df["frequency"],
                    orientation="h",
                    name=rep,
                    marker_color=col,
                    customdata=filtered_df["trace_name"],
                    hovertemplate=(
                        "Repertoire: %{customdata}<br>"
                        "Gene: %{y}<br>"
                        "Frequency: %{x:.3f}<br>"
                        "<extra></extra>"
                    )
                )
            )
        
        fig.update_xaxes(title_text="Frequency")
        fig.update_yaxes(title_text="Gene")
        fig.update_layout(barmode="stack")

    # Update layout
    fig.update_layout(
        title=title,
        width=width,
        height=height,
        template="plotly_white",
    )

    return fig


def plot_similarity(
    data: Union[pl.DataFrame, pd.DataFrame],
    metric: str = "similarity",
    title: str = "Repertoire Similarity Heatmap",
    width: int = 700,
    height: int = 600,
    colorscale: str = "RdBu"
) -> go.Figure:
    """
    Plot repertoire similarity as a heatmap.

    Creates a heatmap showing pairwise similarity scores between repertoires
    from clonal_relatedness() analysis.

    Args:
        data: DataFrame from clonal_relatedness() function. Must contain
            'repertoire1', 'repertoire2', and similarity metric column.
        metric: Column name containing similarity values (default: "similarity")
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels
        colorscale: Plotly colorscale name (default: "RdBu")

    Returns:
        Plotly figure object with similarity heatmap

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> similarity = ls.clonal_relatedness(data, method="morisita")
        >>> fig = ls.plot_similarity(similarity)
        >>> fig.show()

        >>> # Use different colorscale
        >>> fig = ls.plot_similarity(similarity, colorscale="Viridis")
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Validate required columns
    required_cols = ["repertoire1", "repertoire2", metric]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Get all unique repertoires
    all_repertoires = sorted(set(df["repertoire1"].unique()) | set(df["repertoire2"].unique()))
    n = len(all_repertoires)

    # Create similarity matrix (symmetric with diagonal = 1)
    matrix = np.ones((n, n))

    for _, row in df.iterrows():
        i = all_repertoires.index(row["repertoire1"])
        j = all_repertoires.index(row["repertoire2"])
        matrix[i, j] = row[metric]
        matrix[j, i] = row[metric]  # Symmetric

    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=matrix,
        x=all_repertoires,
        y=all_repertoires,
        colorscale=colorscale,
        text=np.round(matrix, 3),
        texttemplate="%{text}",
        textfont={"size": 10},
        colorbar=dict(title=metric.replace("_", " ").title()),
        hovertemplate=(
            "Repertoire 1: %{y}<br>"
            "Repertoire 2: %{x}<br>"
            f"{metric}: %{{z:.3f}}<br>"
            "<extra></extra>"
        )
    ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Repertoire",
        yaxis_title="Repertoire",
        width=width,
        height=height,
        template="plotly_white",
        xaxis=dict(tickangle=45),
        yaxis=dict(autorange="reversed")
    )

    return fig


def plot_common_seqs(
    data: Union[pl.DataFrame, pd.DataFrame],
    top_n: int = 20,
    color_by: str = "n_repertoires",
    title: str = "Sequences Shared Across Repertoires",
    width: int = 900,
    height: int = 600
) -> go.Figure:
    """
    Plot sequences found in multiple repertoires.

    Creates a horizontal bar plot showing shared sequences colored by the
    number of repertoires they appear in.

    Args:
        data: DataFrame from common_seqs() function. Must contain
            'junction_aa', 'n_repertoires', and frequency information.
        top_n: Number of top sequences to show (default: 20)
        color_by: Column to color bars by (default: "n_repertoires")
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with shared sequence bars

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> common = ls.common_seqs(data, min_repertoires=2)
        >>> fig = ls.plot_common_seqs(common, top_n=30)
        >>> fig.show()
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Aggregate by sequence to get summary stats
    if "junction_aa" in df.columns and "n_repertoires" in df.columns:
        # Group by sequence and get max frequency
        seq_summary = (
            df.groupby("junction_aa")
            .agg({
                "n_repertoires": "first",
                "duplicate_frequency": "mean"
            })
            .reset_index()
            .nlargest(top_n, "n_repertoires")
            .sort_values("duplicate_frequency")
        )
    else:
        raise ValueError("Data must contain 'junction_aa' and 'n_repertoires' columns")

    # Truncate long sequences for display
    seq_summary["seq_display"] = seq_summary["junction_aa"].apply(
        lambda x: x[:20] + "..." if len(str(x)) > 20 else str(x)
    )

    # Create plot
    fig = go.Figure(data=[
        go.Bar(
            y=seq_summary["seq_display"],
            x=seq_summary["duplicate_frequency"],
            orientation="h",
            marker=dict(
                color=seq_summary[color_by],
                colorscale="Viridis",
                colorbar=dict(title="# Repertoires"),
                showscale=True
            ),
            text=seq_summary["n_repertoires"],
            textposition="outside",
            hovertemplate=(
                "Sequence: %{customdata[0]}<br>"
                "Repertoires: %{customdata[1]}<br>"
                "Avg frequency: %{x:.4f}<br>"
                "<extra></extra>"
            ),
            customdata=seq_summary[["junction_aa", "n_repertoires"]]
        )
    ])

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Average Frequency",
        yaxis_title="CDR3 Sequence",
        width=width,
        height=height,
        template="plotly_white",
        showlegend=False
    )

    return fig


def plot_differential(
    data: Union[pl.DataFrame, pd.DataFrame],
    p_threshold: float = 0.05,
    fc_threshold: float = 1.0,
    label_top: int = 10,
    title: str = "Differential Abundance (Volcano Plot)",
    width: int = 900,
    height: int = 700
) -> go.Figure:
    """
    Create a volcano plot for differential abundance analysis.

    Plots log2 fold change vs -log10(p-value) to visualize significantly
    different sequences between groups.

    Args:
        data: DataFrame from differential_abundance() function. Must contain
            'log2_fold_change', 'p_value', and sequence columns.
        p_threshold: P-value threshold for significance (default: 0.05)
        fc_threshold: Absolute log2 fold change threshold (default: 1.0)
        label_top: Number of top significant sequences to label (default: 10)
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with volcano plot

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> diff = ls.differential_abundance(
        ...     data,
        ...     group1=["Pre1", "Pre2"],
        ...     group2=["Post1", "Post2"]
        ... )
        >>> fig = ls.plot_differential(diff, label_top=15)
        >>> fig.show()
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Validate required columns
    required_cols = ["log2_fold_change", "p_value"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Calculate -log10(p-value)
    df["-log10_pvalue"] = -np.log10(df["p_value"])

    # Classify points
    df["significance"] = "Not significant"
    df.loc[
        (df["p_value"] < p_threshold) & (df["log2_fold_change"] > fc_threshold),
        "significance"
    ] = "Up in Group 2"
    df.loc[
        (df["p_value"] < p_threshold) & (df["log2_fold_change"] < -fc_threshold),
        "significance"
    ] = "Up in Group 1"

    # Get sequence column name
    seq_col = None
    for col in ["junction_aa", "junction", "sequence"]:
        if col in df.columns:
            seq_col = col
            break

    # Create color map
    color_map = {
        "Not significant": "lightgray",
        "Up in Group 1": "blue",
        "Up in Group 2": "red"
    }

    fig = go.Figure()

    # Plot each category
    for sig_type in ["Not significant", "Up in Group 1", "Up in Group 2"]:
        subset = df[df["significance"] == sig_type]

        fig.add_trace(go.Scatter(
            x=subset["log2_fold_change"],
            y=subset["-log10_pvalue"],
            mode="markers",
            name=sig_type,
            marker=dict(
                color=color_map[sig_type],
                size=6,
                opacity=0.6 if sig_type == "Not significant" else 0.8
            ),
            hovertemplate=(
                f"{seq_col}: %{{customdata[0]}}<br>" if seq_col else "" +
                "log2 FC: %{x:.2f}<br>"
                "p-value: %{customdata[1]:.2e}<br>"
                "<extra></extra>"
            ),
            customdata=subset[[seq_col, "p_value"]] if seq_col else subset[["p_value"]]
        ))

    # Add threshold lines
    fig.add_hline(y=-np.log10(p_threshold), line_dash="dash", line_color="gray",
                  annotation_text=f"p={p_threshold}")
    fig.add_vline(x=fc_threshold, line_dash="dash", line_color="gray")
    fig.add_vline(x=-fc_threshold, line_dash="dash", line_color="gray")

    # Label top significant sequences
    if seq_col and label_top > 0:
        sig_df = df[df["significance"] != "Not significant"].nlargest(label_top, "-log10_pvalue")

        for _, row in sig_df.iterrows():
            seq_display = str(row[seq_col])[:15] + "..." if len(str(row[seq_col])) > 15 else str(row[seq_col])
            fig.add_annotation(
                x=row["log2_fold_change"],
                y=row["-log10_pvalue"],
                text=seq_display,
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor="black",
                ax=20,
                ay=-20,
                font=dict(size=8)
            )

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="log2 Fold Change",
        yaxis_title="-log10(p-value)",
        width=width,
        height=height,
        template="plotly_white",
        hovermode="closest",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    return fig

def plot_top_seqs(
    data: Union[pl.DataFrame, pd.DataFrame],
    top: int = 10,
    repertoire_ids: Optional[List[str]] = None,
    title: str = "Top Sequence Frequencies",
    width: int = 900,
    height: int = 600
) -> go.Figure:
    """1
    Create stacked bar plot showing cumulative frequency of top sequences.

    Shows the top N most abundant sequences per repertoire as colored bands,
    with all remaining sequences grouped as "Other". Useful for visualizing
    clonal dominance and repertoire diversity at a glance.

    Args:
        data: DataFrame with sequence data. Must contain 'repertoire_id',
            'junction_aa', and 'duplicate_frequency' columns.
        top: Number of top sequences to show individually (default: 10)
        repertoire_ids: Optional list of specific repertoires to plot
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with stacked bar chart

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> # Show top 15 sequences per sample
        >>> fig = ls.plot_top_seqs(data, top=15)
        >>> fig.show()

        >>> # Compare specific samples
        >>> fig = ls.plot_top_seqs(
        ...     data,
        ...     top=10,
        ...     repertoire_ids=["S1", "S2", "S3"]
        ... )

    Notes:
        - Sequences are ranked within each repertoire
        - "Other" category includes all sequences beyond top N
        - Colors cycle through a spectral palette
        - Repertoires ordered by diversity (most diverse first)

    See Also:
        - top_seqs(): Get the top N sequences
        - plot_clonality(): Visualize clonality metrics
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter for specified repertoires
    if repertoire_ids:
        df = df[df["repertoire_id"].isin(repertoire_ids)]

    # Validate required columns
    required_cols = ["repertoire_id", "junction_aa", "duplicate_frequency"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # Get top sequences per repertoire
    top_seqs = []
    for rep in df["repertoire_id"].unique():
        rep_data = df[df["repertoire_id"] == rep].nlargest(top, "duplicate_frequency").copy()
        rep_data["rank"] = range(1, len(rep_data) + 1)
        top_seqs.append(rep_data)

    top_df = pd.concat(top_seqs, ignore_index=True)

    # Calculate "Other" category
    other_freqs = []
    for rep in df["repertoire_id"].unique():
        top_freq = top_df[top_df["repertoire_id"] == rep]["duplicate_frequency"].sum()
        other_freq = 1.0 - top_freq
        other_freqs.append({
            "repertoire_id": rep,
            "junction_aa": "Other sequences",
            "duplicate_frequency": other_freq,
            "rank": top + 1
        })

    other_df = pd.DataFrame(other_freqs)
    plot_df = pd.concat([top_df, other_df], ignore_index=True)
    plot_df["frequency_pct"] = plot_df["duplicate_frequency"] * 100

    # Order repertoires by diversity (other freq descending)
    rep_order = other_df.sort_values("duplicate_frequency", ascending=False)["repertoire_id"].tolist()

    # Create color palette
    colors = px.colors.sample_colorscale("Spectral", np.linspace(0, 1, top + 1))

    fig = go.Figure()

    # Add trace for each rank
    for rank in range(1, top + 2):
        rank_data = plot_df[plot_df["rank"] == rank]
        rank_data = rank_data.set_index("repertoire_id").reindex(rep_order).reset_index()

        label = f"Rank {rank}" if rank <= top else "Other"

        fig.add_trace(go.Bar(
            x=rank_data["repertoire_id"],
            y=rank_data["frequency_pct"],
            name=label,
            marker_color=colors[rank - 1],
            hovertemplate=(
                f"<b>{label}</b><br>"
                "Repertoire: %{x}<br>"
                "Frequency: %{y:.2f}%<br>"
                "<extra></extra>"
            ),
            showlegend=False
        ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Repertoire",
        yaxis_title="Frequency (%)",
        barmode="stack",
        width=width,
        height=height,
        template="plotly_white",
        xaxis=dict(tickangle=45),
        yaxis=dict(range=[0, 100])
    )

    return fig


def plot_lorenz_curve(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_ids: Optional[List[str]] = None,
    title: str = "Lorenz Curve - Clonal Inequality",
    width: int = 800,
    height: int = 600
) -> go.Figure:
    """
    Plot Lorenz curves to visualize clonal inequality.

    The Lorenz curve shows cumulative frequency distribution, helping visualize
    how evenly sequences are distributed. A more diagonal line indicates higher
    diversity, while a curve closer to the bottom-right indicates clonal
    dominance (high inequality).

    Args:
        data: DataFrame with sequence frequencies. Must contain 'repertoire_id'
            and 'duplicate_frequency' columns.
        repertoire_ids: Optional list of specific repertoires to plot
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly figure object with Lorenz curves

    Examples:
        >>> import lymphoseq as ls
        >>> data = ls.read_immunoseq("data/immunoseq/")
        >>> fig = ls.plot_lorenz_curve(data)
        >>> fig.show()

        >>> # Compare specific samples
        >>> fig = ls.plot_lorenz_curve(
        ...     data,
        ...     repertoire_ids=["Pre_treatment", "Post_treatment"]
        ... )

    Notes:
        - Diagonal line represents perfect equality
        - Area between curve and diagonal is the Gini coefficient
        - Steeper curves = more clonal (less diverse)
        - More diagonal = more diverse (even distribution)

    See Also:
        - clonality(): Calculate diversity metrics including Gini
        - plot_clonality(): Visualize clonality scores
    """
    # Convert to pandas if needed
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter for specified repertoires
    if repertoire_ids:
        df = df[df["repertoire_id"].isin(repertoire_ids)]

    # Validate required columns
    required_cols = ["repertoire_id", "duplicate_frequency"]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    fig = go.Figure()

    # Add diagonal line for perfect equality
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode="lines",
        line=dict(color="black", dash="dash", width=1),
        name="Perfect equality",
        hoverinfo="skip"
    ))

    # Calculate and plot Lorenz curve for each repertoire
    colors = px.colors.qualitative.Plotly
    for i, rep in enumerate(df["repertoire_id"].unique()):
        rep_data = df[df["repertoire_id"] == rep].copy()

        # Sort by frequency
        freqs = rep_data["duplicate_frequency"].sort_values().values

        # Calculate cumulative distribution
        cumsum_freqs = np.cumsum(freqs)
        cumsum_freqs = cumsum_freqs / cumsum_freqs[-1]  # Normalize to [0, 1]

        # Proportion of sequences
        n = len(freqs)
        p = np.arange(1, n + 1) / n

        # Prepend (0, 0) for proper Lorenz curve
        L = np.concatenate([[0], cumsum_freqs])
        p = np.concatenate([[0], p])

        # Calculate Gini coefficient (approximation)
        gini = 1 - 2 * np.trapz(L, p)

        fig.add_trace(go.Scatter(
            x=p,
            y=L,
            mode="lines",
            name=f"{rep} (Gini={gini:.3f})",
            line=dict(color=colors[i % len(colors)], width=2),
            hovertemplate=(
                f"Repertoire: {rep}<br>"
                "Sequences (cumulative %): %{x:.2%}<br>"
                "Frequency (cumulative %): %{y:.2%}<br>"
                f"Gini: {gini:.3f}<br>"
                "<extra></extra>"
            )
        ))

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Cumulative Proportion of Sequences",
        yaxis_title="Cumulative Proportion of Reads",
        width=width,
        height=height,
        template="plotly_white",
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[0, 1]),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    return fig


def common_seqs_venn(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_ids: List[str],
    by_column: str = "junction_aa",
    title: Optional[str] = None,
    width: int = 700,
    height: int = 700
) -> go.Figure:
    """
    Create a Venn diagram showing shared sequences between 2-3 repertoires.

    Visualizes the overlap of unique sequences between repertoires, showing
    which sequences are shared and which are unique to each repertoire.

    Args:
        data: DataFrame with sequence data
        repertoire_ids: List of 2-3 repertoire IDs to compare
        by_column: Column to use for comparison (default: junction_aa)
        title: Plot title (auto-generated if None)
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly Figure with Venn diagram

    Raises:
        ValueError: If number of repertoire_ids is not 2 or 3

    Examples:
        >>> # Compare 2 repertoires
        >>> fig = common_seqs_venn(df, ["Sample1", "Sample2"])
        >>> fig.show()

        >>> # Compare 3 repertoires
        >>> fig = common_seqs_venn(df, ["S1", "S2", "S3"], by_column="junction")
    """
    if len(repertoire_ids) < 2 or len(repertoire_ids) > 3:
        raise ValueError("Please provide 2 or 3 repertoire_ids for comparison")

    # Convert to pandas for easier set operations
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter to selected repertoires and get unique sequences
    sets = []
    for rep_id in repertoire_ids:
        rep_seqs = df[df["repertoire_id"] == rep_id][by_column].dropna().unique()
        sets.append(set(rep_seqs))

    # Calculate overlaps
    if len(repertoire_ids) == 2:
        # Two-way Venn
        set1, set2 = sets
        only_1 = len(set1 - set2)
        only_2 = len(set2 - set1)
        both = len(set1 & set2)

        # Create figure with shapes for Venn diagram
        fig = go.Figure()

        # Add circles using shapes
        # Circle 1 (left)
        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=0, y0=0, x1=2, y1=2,
            line=dict(color="#3288bd", width=3),
            fillcolor="rgba(50, 136, 189, 0.3)"
        )

        # Circle 2 (right)
        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=1.5, y0=0, x1=3.5, y1=2,
            line=dict(color="#d53e4f", width=3),
            fillcolor="rgba(213, 62, 79, 0.3)"
        )

        # Add text annotations for counts
        fig.add_annotation(x=0.7, y=1, text=f"{only_1:,}", showarrow=False, font=dict(size=20))
        fig.add_annotation(x=2.8, y=1, text=f"{only_2:,}", showarrow=False, font=dict(size=20))
        fig.add_annotation(x=1.75, y=1, text=f"{both:,}", showarrow=False, font=dict(size=20, color="black"))

        # Add labels
        fig.add_annotation(x=0.7, y=2.3, text=repertoire_ids[0], showarrow=False, font=dict(size=14))
        fig.add_annotation(x=2.8, y=2.3, text=repertoire_ids[1], showarrow=False, font=dict(size=14))

        # Update layout
        fig.update_xaxes(range=[-0.5, 4], showgrid=False, showticklabels=False, zeroline=False)
        fig.update_yaxes(range=[-0.5, 2.8], showgrid=False, showticklabels=False, zeroline=False)

    else:
        # Three-way Venn
        set1, set2, set3 = sets

        # Calculate all regions
        only_1 = len(set1 - set2 - set3)
        only_2 = len(set2 - set1 - set3)
        only_3 = len(set3 - set1 - set2)
        set1_2 = len((set1 & set2) - set3)
        set1_3 = len((set1 & set3) - set2)
        set2_3 = len((set2 & set3) - set1)
        all_three = len(set1 & set2 & set3)

        # Create figure
        fig = go.Figure()

        # Add circles using shapes
        # Circle 1 (top)
        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=0.5, y0=1.5, x1=2.5, y1=3.5,
            line=dict(color="#3288bd", width=3),
            fillcolor="rgba(50, 136, 189, 0.2)"
        )

        # Circle 2 (bottom left)
        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=0, y0=0, x1=2, y1=2,
            line=dict(color="#abdda4", width=3),
            fillcolor="rgba(171, 221, 164, 0.2)"
        )

        # Circle 3 (bottom right)
        fig.add_shape(
            type="circle",
            xref="x", yref="y",
            x0=1.5, y0=0, x1=3.5, y1=2,
            line=dict(color="#d53e4f", width=3),
            fillcolor="rgba(213, 62, 79, 0.2)"
        )

        # Add text annotations for counts
        fig.add_annotation(x=1.5, y=3.0, text=f"{only_1:,}", showarrow=False, font=dict(size=16))
        fig.add_annotation(x=0.5, y=0.6, text=f"{only_2:,}", showarrow=False, font=dict(size=16))
        fig.add_annotation(x=3.0, y=0.6, text=f"{only_3:,}", showarrow=False, font=dict(size=16))
        fig.add_annotation(x=0.9, y=2.0, text=f"{set1_2:,}", showarrow=False, font=dict(size=16))
        fig.add_annotation(x=2.1, y=2.0, text=f"{set1_3:,}", showarrow=False, font=dict(size=16))
        fig.add_annotation(x=1.5, y=0.9, text=f"{set2_3:,}", showarrow=False, font=dict(size=16))
        fig.add_annotation(x=1.5, y=1.5, text=f"{all_three:,}", showarrow=False, font=dict(size=18, color="black"))

        # Add labels
        fig.add_annotation(x=1.5, y=3.8, text=repertoire_ids[0], showarrow=False, font=dict(size=12))
        fig.add_annotation(x=0.5, y=-0.3, text=repertoire_ids[1], showarrow=False, font=dict(size=12))
        fig.add_annotation(x=3.0, y=-0.3, text=repertoire_ids[2], showarrow=False, font=dict(size=12))

        # Update layout
        fig.update_xaxes(range=[-0.5, 4], showgrid=False, showticklabels=False, zeroline=False)
        fig.update_yaxes(range=[-0.8, 4.2], showgrid=False, showticklabels=False, zeroline=False)

    # Common layout settings
    if title is None:
        title = f"Common Sequences - {', '.join(repertoire_ids)}"

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center'),
        width=width,
        height=height,
        plot_bgcolor="white",
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, scaleanchor="x", scaleratio=1),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


def plot_track(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_ids: Optional[List[str]] = None,
    by_column: str = "junction_aa",
    top_n: int = 20,
    min_frequency: float = 0.0001,
    highlight_seqs: Optional[List[str]] = None,
    title: str = "Clone Tracking",
    width: int = 1000,
    height: int = 700,
    min_shared: int = 1
) -> go.Figure:
    """
    Track clones across samples with Sankey diagram.

    Visualizes how specific sequences flow between repertoires, showing
    the persistence and dynamics of TCR clones across samples.

    Args:
        data: DataFrame with sequence data
        repertoire_ids: List of repertoire IDs to track (in order). If None, uses all
        by_column: Column to track (default: junction_aa)
        top_n: Number of top sequences to track per repertoire
        min_frequency: Minimum frequency threshold to include
        highlight_seqs: Optional list of specific sequences to highlight
        title: Plot title
        width: Plot width in pixels
        height: Plot height in pixels
        min_shared: Minimum number of repertoires a sequence must appear in (default: 1)

    Returns:
        Plotly Figure with Sankey diagram

    Examples:
        >>> # Track top clones across time points
        >>> fig = plot_track(df, repertoire_ids=["T0", "T1", "T2"], top_n=15)
        >>> fig.show()

        >>> # Track shared sequences only
        >>> fig = plot_track(
        ...     df,
        ...     repertoire_ids=["Pre", "Post"],
        ...     min_shared=2
        ... )
    """
    # Convert to pandas for easier processing
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter to selected repertoires
    if repertoire_ids is not None:
        df = df[df["repertoire_id"].isin(repertoire_ids)]
    else:
        repertoire_ids = sorted(df["repertoire_id"].unique())

    # Filter by minimum frequency
    df = df[df["duplicate_frequency"] >= min_frequency]

    # Get sequences to track
    if highlight_seqs is not None:
        # Use highlighted sequences
        candidate_sequences = set(highlight_seqs)
    else:
        # Get top N sequences from each repertoire
        candidate_sequences = set()
        for rep_id in repertoire_ids:
            rep_df = df[df["repertoire_id"] == rep_id].nlargest(top_n, "duplicate_frequency")
            candidate_sequences.update(rep_df[by_column].tolist())

    # Filter to sequences that appear in at least min_shared repertoires
    seq_rep_counts = {}
    for seq in candidate_sequences:
        count = df[df[by_column] == seq]["repertoire_id"].nunique()
        seq_rep_counts[seq] = count

    sequences_to_track = {seq for seq, count in seq_rep_counts.items() if count >= min_shared}

    if len(sequences_to_track) == 0:
        raise ValueError(
            f"No sequences found in at least {min_shared} repertoires. "
            f"Try reducing min_shared parameter or increasing top_n."
        )

    # Filter to sequences we're tracking
    df_filtered = df[df[by_column].isin(sequences_to_track)].copy()

    # Sort sequences by total abundance across all samples
    seq_totals = df_filtered.groupby(by_column)["duplicate_frequency"].sum().sort_values(ascending=False)
    sequences = seq_totals.index.tolist()

    return _plot_track_sankey(df_filtered, sequences, repertoire_ids, by_column, title, width, height)


def _plot_track_sankey(
    df_filtered: pd.DataFrame,
    sequences: List[str],
    repertoire_ids: List[str],
    by_column: str,
    title: str,
    width: int,
    height: int
) -> go.Figure:
    """Create Sankey diagram for clone tracking."""

    # Create color map for sequences
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    if len(sequences) <= 10:
        colors = plt.cm.tab10(range(len(sequences)))
    else:
        colors = plt.cm.tab20(range(min(len(sequences), 20)))

    seq_colors = {}
    for i, seq in enumerate(sequences):
        if i < len(colors):
            rgba = colors[i]
            seq_colors[seq] = f'rgba({int(rgba[0]*255)},{int(rgba[1]*255)},{int(rgba[2]*255)},0.8)'
        else:
            seq_colors[seq] = 'rgba(128,128,128,0.5)'

    # Build frequency matrix: sequences x repertoires
    freq_matrix = {}
    for seq in sequences:
        freq_matrix[seq] = {}
        for rep_id in repertoire_ids:
            rep_seq_data = df_filtered[
                (df_filtered[by_column] == seq) &
                (df_filtered["repertoire_id"] == rep_id)
            ]
            freq_matrix[seq][rep_id] = rep_seq_data["duplicate_frequency"].sum() if len(rep_seq_data) > 0 else 0

    # Build nodes and links
    node_labels = []
    node_colors = []
    node_customdata = []
    node_map = {}  # (repertoire, sequence) -> node_index
    node_x = []
    node_y = []

    # Create nodes for each (repertoire, sequence) pair where sequence appears
    node_idx = 0
    repertoire_node_counts = {rep_id: 0 for rep_id in repertoire_ids}

    for rep_idx, rep_id in enumerate(repertoire_ids):
        # Position along x-axis
        x_pos = rep_idx / (len(repertoire_ids) - 1) if len(repertoire_ids) > 1 else 0.5

        # Get sequences present in this repertoire, maintaining global sequence order
        rep_seqs = [seq for seq in sequences if freq_matrix[seq][rep_id] > 0]
        repertoire_node_counts[rep_id] = len(rep_seqs)

        for seq_idx, seq in enumerate(rep_seqs):
            freq = freq_matrix[seq][rep_id]

            # Truncate sequence for display
            seq_display = seq[:20] + "..." if len(seq) > 20 else seq
            node_label = f"{seq_display}"

            node_labels.append(node_label)
            node_colors.append(seq_colors.get(seq, 'rgba(128,128,128,0.5)'))
            node_customdata.append({
                'sequence': seq,
                'repertoire': rep_id,
                'frequency': freq
            })
            node_map[(rep_id, seq)] = node_idx
            node_x.append(x_pos)

            # Space nodes vertically evenly within each repertoire column
            if len(rep_seqs) > 1:
                y_pos = seq_idx / (len(rep_seqs) - 1)
            else:
                y_pos = 0.5
            node_y.append(y_pos)
            node_idx += 1

    # Create links between all repertoires for the same sequence
    # Links flow left-to-right connecting each occurrence of a sequence
    sources = []
    targets = []
    values = []
    link_colors = []
    link_labels = []

    # For each sequence, create links between all repertoires it appears in
    for seq in sequences:
        # Get all repertoires where this sequence appears (in order)
        seq_reps = [rep_id for rep_id in repertoire_ids if freq_matrix[seq][rep_id] > 0]

        # Create links between consecutive appearances of this sequence
        for i in range(len(seq_reps) - 1):
            rep1 = seq_reps[i]
            rep2 = seq_reps[i + 1]

            freq1 = freq_matrix[seq][rep1]
            freq2 = freq_matrix[seq][rep2]

            if (rep1, seq) in node_map and (rep2, seq) in node_map:
                source_node = node_map[(rep1, seq)]
                target_node = node_map[(rep2, seq)]
                sources.append(source_node)
                targets.append(target_node)
                # Use geometric mean of frequencies for better visual representation
                # Multiply by scaling factor for visibility
                values.append(np.sqrt(freq1 * freq2) * 1000)
                link_colors.append(seq_colors.get(seq, 'rgba(128,128,128,0.3)'))
                link_labels.append(f"{seq[:30]}<br>{rep1}: {freq1:.4f}<br>{rep2}: {freq2:.4f}")

    # Check if we have any links to display
    if len(sources) == 0:
        raise ValueError(
            f"No sequences found in multiple samples. All {len(sequences)} sequences appear in only one sample. "
            f"Try: (1) setting min_shared=1 to show all sequences, or (2) increasing top_n to find more shared sequences."
        )

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        arrangement='snap',
        node=dict(
            pad=20,
            thickness=25,
            line=dict(color="white", width=2),
            label=node_labels,
            color=node_colors,
            x=node_x,
            y=node_y,
            customdata=[f"<b>{cd['sequence'][:30]}</b><br>Sample: {cd['repertoire']}<br>Freq: {cd['frequency']:.4f}"
                       for cd in node_customdata],
            hovertemplate='%{customdata}<extra></extra>'
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            color=link_colors,
            customdata=link_labels,
            hovertemplate='<b>%{customdata}</b><extra></extra>'
        )
    )])

    # Add repertoire labels as annotations
    for i, rep_id in enumerate(repertoire_ids):
        fig.add_annotation(
            x=i / (len(repertoire_ids) - 1) if len(repertoire_ids) > 1 else 0.5,
            y=1.08,
            text=f"<b>{rep_id}</b>",
            showarrow=False,
            font=dict(size=16, color='black'),
            xref="paper",
            yref="paper"
        )

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=18)),
        font=dict(size=11),
        width=width,
        height=height,
        margin=dict(l=20, r=20, t=100, b=40),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )

    return fig


def plot_track_singular(
    data: Union[pl.DataFrame, pd.DataFrame],
    sequence: str,
    repertoire_ids: Optional[List[str]] = None,
    by_column: str = "junction_aa",
    title: Optional[str] = None,
    width: int = 800,
    height: int = 500
) -> go.Figure:
    """
    Track a single clone across multiple samples.

    Creates a line plot showing how a specific sequence's frequency changes
    across repertoires (e.g., over time or across conditions).

    Args:
        data: DataFrame with sequence data
        sequence: Specific sequence to track
        repertoire_ids: List of repertoire IDs in order (if None, uses all)
        by_column: Column to match (default: junction_aa)
        title: Plot title (auto-generated if None)
        width: Plot width in pixels
        height: Plot height in pixels

    Returns:
        Plotly Figure with line plot

    Examples:
        >>> # Track a sequence over time points
        >>> fig = plot_track_singular(
        ...     df,
        ...     sequence="CASSLAPGATNEKLFF",
        ...     repertoire_ids=["T0", "T1", "T2", "T3"]
        ... )
        >>> fig.show()
    """
    # Convert to pandas
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter to sequence
    df_seq = df[df[by_column] == sequence].copy()

    if len(df_seq) == 0:
        raise ValueError(f"Sequence '{sequence}' not found in data")

    # Get repertoire order
    if repertoire_ids is None:
        repertoire_ids = sorted(df_seq["repertoire_id"].unique())
    
    # Get frequency for each repertoire
    frequencies = []
    for rep_id in repertoire_ids:
        rep_data = df_seq[df_seq["repertoire_id"] == rep_id]
        if len(rep_data) > 0:
            freq = rep_data["duplicate_frequency"].sum()
        else:
            freq = 0
        frequencies.append(freq)
    
    sequences = df_seq["junction_aa"].unique()
    sequences = sorted(sequences)
    if len(sequences) <= 10:
        colors = plt.cm.tab10(range(len(sequences)))
    else:
        colors = plt.cm.tab20(range(min(len(sequences), 20)))
    
    # Create line plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=repertoire_ids,
        y=frequencies,
        mode='lines+markers',
        line=dict(color='#3288bd', width=3),
        marker=dict(size=10, color='#3288bd'),
        color=colors,
        name=sequence[:20] + "..." if len(sequence) > 20 else sequence
    ))

    # Add title
    if title is None:
        title = f"Clone Tracking: {sequence[:30]}{'...' if len(sequence) > 30 else ''}"

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center'),
        xaxis_title="Repertoire",
        yaxis_title="Frequency",
        width=width,
        height=height,
        template="plotly_white",
        hovermode='x unified'
    )

    # Format y-axis as percentage
    fig.update_yaxes(tickformat=".2%")

    return fig
