"""
Sequence alignment functions for AIRR-seq data.

Provides multiple sequence alignment capabilities for TCR/BCR sequences.
"""

import pandas as pd
import polars as pl
from typing import Union, List, Optional, Literal
from pathlib import Path
import tempfile
import subprocess
import shutil


def align_seq(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_ids: Optional[List[str]] = None,
    sequence_list: Optional[List[str]] = None,
    edit_distance: int = 15,
    by_column: str = "junction_aa",
    method: Literal["muscle", "clustalw", "clustalo"] = "muscle",
    top: int = 150,
    output_format: Literal["fasta", "clustal", "phylip"] = "fasta"
) -> str:
    """
    Perform multiple sequence alignment on TCR/BCR sequences.

    Uses external alignment tools (MUSCLE, ClustalW, or Clustal Omega) to align
    sequences. Can filter by repertoire, search for similar sequences, or align
    top sequences.

    Args:
        data: DataFrame with sequence data
        repertoire_ids: List of repertoire IDs to include
        sequence_list: List of sequences to search for (with edit distance)
        edit_distance: Maximum edit distance for sequence search
        by_column: Column to align (junction_aa or junction)
        method: Alignment method - "muscle", "clustalw", or "clustalo"
        top: Maximum number of sequences to align
        output_format: Output format - "fasta", "clustal", or "phylip"

    Returns:
        String containing the alignment in the specified format

    Raises:
        ValueError: If alignment tool is not found or insufficient sequences
        RuntimeError: If alignment fails

    Examples:
        >>> # Align top sequences from specific repertoires
        >>> alignment = align_seq(df, repertoire_ids=["S1", "S2"], top=50)
        >>> print(alignment)

        >>> # Search and align similar sequences
        >>> alignment = align_seq(
        ...     df,
        ...     sequence_list=["CASSLAPGATNEKLFF"],
        ...     edit_distance=2
        ... )

    Notes:
        Requires external alignment tool to be installed:
        - MUSCLE: conda install -c bioconda muscle
        - ClustalW: conda install -c bioconda clustalw
        - Clustal Omega: conda install -c bioconda clustalo
    """
    # Convert to pandas for easier processing
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter by repertoire_ids if provided
    if repertoire_ids is not None:
        df = df[df["repertoire_id"].isin(repertoire_ids)]

    # Search for similar sequences if sequence_list provided
    if sequence_list is not None:
        from .sequence_ops import search_seq

        # Convert back to polars for search_seq
        if isinstance(data, pl.DataFrame):
            search_data = pl.from_pandas(df)
        else:
            search_data = pl.from_pandas(df)

        # Search for sequences
        matches = []
        for seq in sequence_list:
            result = search_seq(
                search_data,
                sequence=seq,
                max_distance=edit_distance,
                by_column=by_column
            )
            if result is not None and len(result) > 0:
                matches.append(result.to_pandas() if isinstance(result, pl.DataFrame) else result)

        if not matches:
            raise ValueError("No sequences found matching the search criteria")

        df = pd.concat(matches, ignore_index=True).drop_duplicates()

    # Filter to top sequences
    if len(df) > top:
        df = df.nlargest(top, "duplicate_frequency")

    # Filter by minimum sequence length
    if by_column == "junction":
        df = df[df[by_column].str.len() > 15]
    else:  # junction_aa
        df = df[df[by_column].str.len() > 3]

    # Check minimum sequences
    if len(df) < 3:
        raise ValueError(f"Need at least 3 sequences for alignment, found {len(df)}")

    # Create FASTA format input
    sequences = []
    for idx, row in df.iterrows():
        seq_id = f"{row.get('repertoire_id', 'seq')}_{idx}"
        seq = row[by_column]
        sequences.append(f">{seq_id}\n{seq}")

    fasta_input = "\n".join(sequences)

    # Check if alignment tool is available
    tool_map = {
        "muscle": "muscle",
        "clustalw": "clustalw",
        "clustalo": "clustalo"
    }

    tool = tool_map.get(method)
    if tool is None:
        raise ValueError(f"Unknown alignment method: {method}")

    if shutil.which(tool) is None:
        raise RuntimeError(
            f"{tool} not found. Install with: conda install -c bioconda {tool}"
        )

    # Run alignment using temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        input_file = tmpdir / "input.fasta"
        output_file = tmpdir / "output.aln"

        # Write input FASTA
        with open(input_file, 'w') as f:
            f.write(fasta_input)

        # Run alignment tool
        try:
            if method == "muscle":
                # MUSCLE command
                cmd = [
                    tool,
                    "-in", str(input_file),
                    "-out", str(output_file)
                ]
                if output_format == "clustal":
                    cmd.extend(["-clw"])
                elif output_format == "phylip":
                    cmd.extend(["-phyi"])

            elif method == "clustalw":
                # ClustalW command
                cmd = [
                    tool,
                    f"-INFILE={input_file}",
                    f"-OUTFILE={output_file}",
                    "-OUTPUT=FASTA" if output_format == "fasta" else "-OUTPUT=CLUSTAL"
                ]

            elif method == "clustalo":
                # Clustal Omega command
                cmd = [
                    tool,
                    "-i", str(input_file),
                    "-o", str(output_file),
                    "--outfmt", output_format
                ]

            # Run alignment
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode != 0:
                raise RuntimeError(
                    f"Alignment failed: {result.stderr}"
                )

            # Read output
            if output_file.exists():
                with open(output_file, 'r') as f:
                    alignment = f.read()
            else:
                # Some tools write to different files
                possible_outputs = list(tmpdir.glob("*"))
                for pfile in possible_outputs:
                    if pfile.suffix in ['.aln', '.fasta', '.phy']:
                        with open(pfile, 'r') as f:
                            alignment = f.read()
                        break
                else:
                    raise RuntimeError("Alignment output file not found")

            return alignment

        except subprocess.TimeoutExpired:
            raise RuntimeError(
                f"Alignment timed out after 5 minutes. Try reducing the number of sequences."
            )
        except Exception as e:
            raise RuntimeError(f"Alignment failed: {str(e)}")


def align_seq_biopython(
    sequences: List[str],
    sequence_ids: Optional[List[str]] = None,
    method: Literal["muscle", "clustalw", "clustalo"] = "muscle"
) -> str:
    """
    Simple sequence alignment using BioPython (if external tools not available).

    This is a fallback method that uses BioPython's pairwise alignment for small sets.

    Args:
        sequences: List of sequences to align
        sequence_ids: Optional list of sequence IDs
        method: Alignment method (used for compatibility, actual method may vary)

    Returns:
        String with alignment in FASTA format

    Examples:
        >>> seqs = ["CASSLAPGATNEKLFF", "CASSLGQANTEVFF", "CASSLAPGQYF"]
        >>> alignment = align_seq_biopython(seqs)
    """
    try:
        from Bio import AlignIO
        from Bio.Align import PairwiseAligner
        from Bio.Seq import Seq
        from Bio.SeqRecord import SeqRecord
        from Bio import SeqIO
    except ImportError:
        raise ImportError(
            "BioPython required for alignment. Install with: pip install biopython"
        )

    if len(sequences) < 2:
        raise ValueError("Need at least 2 sequences for alignment")

    # Create SeqRecord objects
    if sequence_ids is None:
        sequence_ids = [f"seq_{i}" for i in range(len(sequences))]

    records = [
        SeqRecord(Seq(seq), id=seq_id, description="")
        for seq, seq_id in zip(sequences, sequence_ids)
    ]

    # For small sets, use pairwise alignment
    # Note: This is not true multiple sequence alignment
    # For production use, install external tools (MUSCLE, etc.)

    aligner = PairwiseAligner()
    aligner.mode = 'global'

    # Align first two sequences as reference
    if len(sequences) == 2:
        alignment = aligner.align(sequences[0], sequences[1])[0]
        return str(alignment)

    # For more sequences, return as pseudo-alignment (not ideal)
    # This is a placeholder - external tools should be used
    output = []
    for record in records:
        output.append(f">{record.id}\n{str(record.seq)}")

    return "\n".join(output) + "\n\n# Note: Install MUSCLE/ClustalW for true MSA"


def phylo_tree(
    data: Union[pl.DataFrame, pd.DataFrame],
    repertoire_id: str,
    by_column: str = "junction_aa",
    method: Literal["nj", "upgma", "wpgma"] = "nj",
    distance_metric: Literal["edit", "hamming", "levenshtein"] = "edit"
):
    """
    Create a phylogenetic tree from TCR/BCR sequences.

    Builds a phylogenetic tree using distance-based methods (neighbor-joining,
    UPGMA, or WPGMA) to show evolutionary relationships between sequences.

    Args:
        data: DataFrame with sequence data
        repertoire_id: Repertoire ID to analyze
        by_column: Column to use (junction_aa or junction)
        method: Tree building method - "nj" (neighbor-joining), "upgma", or "wpgma"
        distance_metric: Distance metric - "edit", "hamming", or "levenshtein"

    Returns:
        Bio.Phylo.BaseTree.Tree object that can be visualized

    Raises:
        ValueError: If insufficient sequences or invalid parameters
        ImportError: If required libraries not installed

    Examples:
        >>> tree = phylo_tree(df, repertoire_id="S1", by_column="junction_aa")
        >>> # Visualize the tree
        >>> from Bio import Phylo
        >>> import matplotlib.pyplot as plt
        >>> Phylo.draw(tree)
        >>> plt.show()

    Notes:
        Requires BioPython: pip install biopython
        For better visualizations: pip install ete3
    """
    try:
        from Bio import Phylo
        from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
        from Bio.Phylo import BaseTree
        import numpy as np
    except ImportError:
        raise ImportError(
            "BioPython required for phylogenetic trees. Install with: pip install biopython"
        )

    # Convert to pandas
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data.copy()

    # Filter to repertoire
    df = df[df["repertoire_id"] == repertoire_id]

    # Filter by length
    if by_column == "junction":
        df = df[df[by_column].str.len() >= 9]
    else:  # junction_aa
        df = df[df[by_column].str.len() >= 3]

    if len(df) < 3:
        raise ValueError(
            f"Need at least 3 sequences for phylogenetic tree, found {len(df)}"
        )

    # Get sequences
    sequences = df[by_column].tolist()

    # Calculate distance matrix
    n = len(sequences)
    dist_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            if distance_metric == "edit" or distance_metric == "levenshtein":
                # Levenshtein distance (edit distance)
                dist = _levenshtein_distance(sequences[i], sequences[j])
            elif distance_metric == "hamming":
                # Hamming distance (only for equal length)
                if len(sequences[i]) == len(sequences[j]):
                    dist = sum(c1 != c2 for c1, c2 in zip(sequences[i], sequences[j]))
                else:
                    # Fall back to edit distance for different lengths
                    dist = _levenshtein_distance(sequences[i], sequences[j])
            else:
                raise ValueError(f"Unknown distance metric: {distance_metric}")

            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist

    # Create sequence names (truncate for display)
    names = [f"{seq[:15]}..." if len(seq) > 15 else seq for seq in sequences]

    # Build tree using BioPython
    # Create a simple distance matrix in BioPython format
    from Bio.Phylo.TreeConstruction import _DistanceMatrix

    # Convert to lower triangular format for BioPython
    lower_triangle = []
    for i in range(n):
        row = [dist_matrix[i, j] for j in range(i + 1)]
        lower_triangle.append(row)

    dm = _DistanceMatrix(names, lower_triangle)

    # Build tree
    constructor = DistanceTreeConstructor()

    if method == "nj":
        tree = constructor.nj(dm)
    elif method == "upgma":
        tree = constructor.upgma(dm)
    else:
        raise ValueError(f"Unknown tree method: {method}")

    return tree


def _levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculate Levenshtein distance between two strings.

    Args:
        s1: First string
        s2: Second string

    Returns:
        Edit distance (integer)
    """
    if len(s1) < len(s2):
        return _levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Cost of insertions, deletions, or substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def plot_phylo_tree(
    tree,
    title: str = "Phylogenetic Tree",
    width: int = 10,
    height: int = 8,
    save_path: Optional[str] = None
):
    """
    Plot a phylogenetic tree.

    Args:
        tree: Bio.Phylo tree object
        title: Plot title
        width: Figure width in inches
        height: Figure height in inches
        save_path: Optional path to save figure

    Examples:
        >>> tree = phylo_tree(df, repertoire_id="S1")
        >>> plot_phylo_tree(tree, title="Sample S1 Phylogeny")
    """
    try:
        from Bio import Phylo
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError("Matplotlib required for plotting. Install with: pip install matplotlib")

    fig, ax = plt.subplots(figsize=(width, height))
    Phylo.draw(tree, axes=ax, do_show=False)
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()
