"""
LymphoSeq: Python toolkit for analyzing high-throughput T and B cell receptor sequencing data.

This package provides tools for importing, manipulating, and visualizing
Adaptive Immune Receptor Repertoire Sequencing (AIRR-seq) data.
"""

__version__ = "0.1.0"
__author__ = "Shashidhar Ravishankar"
__email__ = "sravisha@fredhutch.org"

from .parsers import read_immunoseq, read_10x, read_mixcr
from .analysis import clonality, diversity_metrics, common_sequences, rarefaction_curve
from .analysis.comparative import (
    common_seqs,
    differential_abundance,
    clonal_relatedness,
    clone_track,
    searchSeq,
    mergeSeqs,
)
from .analysis.genes import gene_freq, gene_pair_freq
from .visualization import (
    plot_clonality,
    plot_diversity,
    plot_rarefaction,
    plot_gene_usage,
    plot_similarity,
    plot_common_seqs,
    plot_differential,
    plot_top_seqs,
    plot_track,
    plot_lorenz_curve,
    common_seqs_venn,
)
from .sequence import top_seqs, productive_seq, unique_seqs, remove_seq, merge_chains, split_chains
from .database import search_db, search_published, get_vdjdb_stats

__all__ = [
    # Parsers
    "read_immunoseq",
    "read_10x",
    "read_mixcr",
    # Analysis
    "clonality",
    "diversity_metrics",
    "common_sequences",
    "rarefaction_curve",
    # Comparative analysis
    "common_seqs",
    "differential_abundance",
    "clonal_relatedness",
    "clone_track",
    "searchSeq",
    "mergeSeqs",
    # Gene usage
    "gene_freq",
    "gene_pair_freq",
    # Visualization
    "plot_clonality",
    "plot_diversity",
    "plot_rarefaction",
    "plot_gene_usage",
    "plot_similarity",
    "plot_common_seqs",
    "plot_differential",
    "plot_top_seqs",
    "plot_lorenz_curve",
    "common_seqs_venn",
    # Sequence filtering
    "top_seqs",
    "productive_seq",
    "unique_seqs",
    "remove_seq",
    # Chain merging (10X)
    "merge_chains",
    "split_chains",
    # Database search
    "search_db",
    "search_published",
    "get_vdjdb_stats",
]