"""
Sequence filtering and manipulation functions for AIRR-seq data.

This module provides functions for filtering, selecting, and manipulating
immune repertoire sequences similar to the R LymphoSeq2 package.
"""

from .filtering import (
    top_seqs,
    productive_seq,
    unique_seqs,
    remove_seq,
)
from .chain_merge import (
    merge_chains,
    split_chains,
)

__all__ = [
    "top_seqs",
    "productive_seq",
    "unique_seqs",
    "remove_seq",
    "merge_chains",
    "split_chains",
]
