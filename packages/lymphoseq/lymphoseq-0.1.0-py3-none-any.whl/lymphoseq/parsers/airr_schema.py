"""
AIRR (Adaptive Immune Receptor Repertoire) schema definitions.

Complete implementation of AIRR standard fields based on official specifications
and LymphoSeq2 compatibility.
"""

from typing import Dict, List, Any, Optional, Union
from enum import Enum

try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    pd = None

try:
    import polars as pl
    HAS_POLARS = True
except ImportError:
    HAS_POLARS = False
    pl = None


class AIRRFieldType(Enum):
    """AIRR field data types."""
    STRING = "string"
    INTEGER = "integer"
    NUMBER = "number"
    BOOLEAN = "boolean"


class AIRRField:
    """AIRR field definition."""

    def __init__(
        self,
        name: str,
        field_type: AIRRFieldType,
        description: str,
        required: bool = False,
        default_value: Any = None,
        example: Optional[str] = None
    ):
        self.name = name
        self.field_type = field_type
        self.description = description
        self.required = required
        self.default_value = default_value
        self.example = example


# Complete AIRR schema with all 155+ fields
AIRR_SCHEMA_FIELDS = {
    # Core sequence identification
    "sequence_id": AIRRField(
        "sequence_id", AIRRFieldType.STRING,
        "Unique identifier for the sequence within the repertoire",
        required=True, example="sequence_1"
    ),
    "sequence": AIRRField(
        "sequence", AIRRFieldType.STRING,
        "Nucleotide sequence (e.g., V(D)J rearrangement)",
        example="ATGGATTCCTGCAAGAAGTATGAGCTC"
    ),
    "sequence_aa": AIRRField(
        "sequence_aa", AIRRFieldType.STRING,
        "Amino acid sequence translation of the sequence field",
        example="MDSCKKYELC"
    ),
    "rev_comp": AIRRField(
        "rev_comp", AIRRFieldType.BOOLEAN,
        "True if sequence is reverse complement of original sequence",
        default_value=False
    ),
    "productive": AIRRField(
        "productive", AIRRFieldType.BOOLEAN,
        "True if the sequence is predicted to be productive",
        required=True, default_value=True
    ),
    "vj_in_frame": AIRRField(
        "vj_in_frame", AIRRFieldType.BOOLEAN,
        "True if V and J gene segments are in-frame",
        default_value=True
    ),
    "stop_codon": AIRRField(
        "stop_codon", AIRRFieldType.BOOLEAN,
        "True if the sequence contains a stop codon",
        default_value=False
    ),
    "complete_vdj": AIRRField(
        "complete_vdj", AIRRFieldType.BOOLEAN,
        "True if the sequence spans the entire V(D)J region",
        default_value=False
    ),
    "locus": AIRRField(
        "locus", AIRRFieldType.STRING,
        "Gene locus (e.g., IGH, IGK, IGL, TRA, TRB, TRG, TRD)",
        required=True, example="TRB"
    ),

    # Gene calls
    "v_call": AIRRField(
        "v_call", AIRRFieldType.STRING,
        "V gene assignment",
        required=True, example="TRBV12-1*01"
    ),
    "d_call": AIRRField(
        "d_call", AIRRFieldType.STRING,
        "D gene assignment",
        example="TRBD1*01"
    ),
    "d2_call": AIRRField(
        "d2_call", AIRRFieldType.STRING,
        "Second D gene assignment for longer junctions"
    ),
    "j_call": AIRRField(
        "j_call", AIRRFieldType.STRING,
        "J gene assignment",
        required=True, example="TRBJ2-1*01"
    ),
    "c_call": AIRRField(
        "c_call", AIRRFieldType.STRING,
        "Constant region gene assignment",
        example="TRBC1*01"
    ),

    # Sequence alignments
    "sequence_alignment": AIRRField(
        "sequence_alignment", AIRRFieldType.STRING,
        "Alignment of sequence to V(D)J references"
    ),
    "sequence_alignment_aa": AIRRField(
        "sequence_alignment_aa", AIRRFieldType.STRING,
        "Amino acid alignment of sequence"
    ),
    "germline_alignment": AIRRField(
        "germline_alignment", AIRRFieldType.STRING,
        "Alignment of sequence to germline V(D)J references"
    ),
    "germline_alignment_aa": AIRRField(
        "germline_alignment_aa", AIRRFieldType.STRING,
        "Amino acid alignment to germline"
    ),

    # Junction and CDR3
    "junction": AIRRField(
        "junction", AIRRFieldType.STRING,
        "Junction region sequence",
        example="TGTGCCAGCAGTGAAGCCGGTCCCTTT"
    ),
    "junction_aa": AIRRField(
        "junction_aa", AIRRFieldType.STRING,
        "Junction region amino acid sequence",
        example="CASSEPGPF"
    ),
    "junction_length": AIRRField(
        "junction_length", AIRRFieldType.INTEGER,
        "Length of junction region in nucleotides"
    ),
    "junction_aa_length": AIRRField(
        "junction_aa_length", AIRRFieldType.INTEGER,
        "Length of junction region in amino acids"
    ),

    # N/P additions
    "np1": AIRRField(
        "np1", AIRRFieldType.STRING,
        "Nucleotide sequence of the N/P region between V and D segments"
    ),
    "np1_aa": AIRRField(
        "np1_aa", AIRRFieldType.STRING,
        "Amino acid sequence of the N/P region between V and D segments"
    ),
    "np2": AIRRField(
        "np2", AIRRFieldType.STRING,
        "Nucleotide sequence of the N/P region between D and J segments"
    ),
    "np2_aa": AIRRField(
        "np2_aa", AIRRFieldType.STRING,
        "Amino acid sequence of the N/P region between D and J segments"
    ),
    "np3": AIRRField(
        "np3", AIRRFieldType.STRING,
        "Nucleotide sequence of the N/P region for V-J rearrangements"
    ),
    "np3_aa": AIRRField(
        "np3_aa", AIRRFieldType.STRING,
        "Amino acid sequence of the N/P region for V-J rearrangements"
    ),

    # CDR and framework regions
    "cdr1": AIRRField(
        "cdr1", AIRRFieldType.STRING,
        "CDR1 nucleotide sequence according to IMGT"
    ),
    "cdr1_aa": AIRRField(
        "cdr1_aa", AIRRFieldType.STRING,
        "CDR1 amino acid sequence according to IMGT"
    ),
    "cdr2": AIRRField(
        "cdr2", AIRRFieldType.STRING,
        "CDR2 nucleotide sequence according to IMGT"
    ),
    "cdr2_aa": AIRRField(
        "cdr2_aa", AIRRFieldType.STRING,
        "CDR2 amino acid sequence according to IMGT"
    ),
    "cdr3": AIRRField(
        "cdr3", AIRRFieldType.STRING,
        "CDR3 nucleotide sequence according to IMGT"
    ),
    "cdr3_aa": AIRRField(
        "cdr3_aa", AIRRFieldType.STRING,
        "CDR3 amino acid sequence according to IMGT"
    ),
    "fwr1": AIRRField(
        "fwr1", AIRRFieldType.STRING,
        "Framework 1 nucleotide sequence according to IMGT"
    ),
    "fwr1_aa": AIRRField(
        "fwr1_aa", AIRRFieldType.STRING,
        "Framework 1 amino acid sequence according to IMGT"
    ),
    "fwr2": AIRRField(
        "fwr2", AIRRFieldType.STRING,
        "Framework 2 nucleotide sequence according to IMGT"
    ),
    "fwr2_aa": AIRRField(
        "fwr2_aa", AIRRFieldType.STRING,
        "Framework 2 amino acid sequence according to IMGT"
    ),
    "fwr3": AIRRField(
        "fwr3", AIRRFieldType.STRING,
        "Framework 3 nucleotide sequence according to IMGT"
    ),
    "fwr3_aa": AIRRField(
        "fwr3_aa", AIRRFieldType.STRING,
        "Framework 3 amino acid sequence according to IMGT"
    ),
    "fwr4": AIRRField(
        "fwr4", AIRRFieldType.STRING,
        "Framework 4 nucleotide sequence according to IMGT"
    ),
    "fwr4_aa": AIRRField(
        "fwr4_aa", AIRRFieldType.STRING,
        "Framework 4 amino acid sequence according to IMGT"
    ),

    # Alignment scores and statistics
    "v_score": AIRRField(
        "v_score", AIRRFieldType.NUMBER,
        "V gene alignment score"
    ),
    "v_identity": AIRRField(
        "v_identity", AIRRFieldType.NUMBER,
        "V gene alignment identity"
    ),
    "v_support": AIRRField(
        "v_support", AIRRFieldType.NUMBER,
        "V gene alignment E-value, p-value or other support measure"
    ),
    "v_cigar": AIRRField(
        "v_cigar", AIRRFieldType.STRING,
        "V gene alignment CIGAR string"
    ),
    "d_score": AIRRField(
        "d_score", AIRRFieldType.NUMBER,
        "D gene alignment score"
    ),
    "d_identity": AIRRField(
        "d_identity", AIRRFieldType.NUMBER,
        "D gene alignment identity"
    ),
    "d_support": AIRRField(
        "d_support", AIRRFieldType.NUMBER,
        "D gene alignment E-value, p-value or other support measure"
    ),
    "d_cigar": AIRRField(
        "d_cigar", AIRRFieldType.STRING,
        "D gene alignment CIGAR string"
    ),
    "d2_score": AIRRField(
        "d2_score", AIRRFieldType.NUMBER,
        "Second D gene alignment score"
    ),
    "d2_identity": AIRRField(
        "d2_identity", AIRRFieldType.NUMBER,
        "Second D gene alignment identity"
    ),
    "d2_support": AIRRField(
        "d2_support", AIRRFieldType.NUMBER,
        "Second D gene alignment support measure"
    ),
    "d2_cigar": AIRRField(
        "d2_cigar", AIRRFieldType.STRING,
        "Second D gene alignment CIGAR string"
    ),
    "j_score": AIRRField(
        "j_score", AIRRFieldType.NUMBER,
        "J gene alignment score"
    ),
    "j_identity": AIRRField(
        "j_identity", AIRRFieldType.NUMBER,
        "J gene alignment identity"
    ),
    "j_support": AIRRField(
        "j_support", AIRRFieldType.NUMBER,
        "J gene alignment E-value, p-value or other support measure"
    ),
    "j_cigar": AIRRField(
        "j_cigar", AIRRFieldType.STRING,
        "J gene alignment CIGAR string"
    ),
    "c_score": AIRRField(
        "c_score", AIRRFieldType.NUMBER,
        "Constant region alignment score"
    ),
    "c_identity": AIRRField(
        "c_identity", AIRRFieldType.NUMBER,
        "Constant region alignment identity"
    ),
    "c_support": AIRRField(
        "c_support", AIRRFieldType.NUMBER,
        "Constant region alignment support measure"
    ),
    "c_cigar": AIRRField(
        "c_cigar", AIRRFieldType.STRING,
        "Constant region alignment CIGAR string"
    ),

    # Sequence coordinates
    "v_sequence_start": AIRRField(
        "v_sequence_start", AIRRFieldType.INTEGER,
        "Start coordinate of V region in sequence (1-based)"
    ),
    "v_sequence_end": AIRRField(
        "v_sequence_end", AIRRFieldType.INTEGER,
        "End coordinate of V region in sequence (1-based)"
    ),
    "v_germline_start": AIRRField(
        "v_germline_start", AIRRFieldType.INTEGER,
        "Start coordinate of V region in germline (1-based)"
    ),
    "v_germline_end": AIRRField(
        "v_germline_end", AIRRFieldType.INTEGER,
        "End coordinate of V region in germline (1-based)"
    ),
    "v_alignment_start": AIRRField(
        "v_alignment_start", AIRRFieldType.INTEGER,
        "Start coordinate of V region alignment (1-based)"
    ),
    "v_alignment_end": AIRRField(
        "v_alignment_end", AIRRFieldType.INTEGER,
        "End coordinate of V region alignment (1-based)"
    ),
    "d_sequence_start": AIRRField(
        "d_sequence_start", AIRRFieldType.INTEGER,
        "Start coordinate of D region in sequence (1-based)"
    ),
    "d_sequence_end": AIRRField(
        "d_sequence_end", AIRRFieldType.INTEGER,
        "End coordinate of D region in sequence (1-based)"
    ),
    "d_germline_start": AIRRField(
        "d_germline_start", AIRRFieldType.INTEGER,
        "Start coordinate of D region in germline (1-based)"
    ),
    "d_germline_end": AIRRField(
        "d_germline_end", AIRRFieldType.INTEGER,
        "End coordinate of D region in germline (1-based)"
    ),
    "d_alignment_start": AIRRField(
        "d_alignment_start", AIRRFieldType.INTEGER,
        "Start coordinate of D region alignment (1-based)"
    ),
    "d_alignment_end": AIRRField(
        "d_alignment_end", AIRRFieldType.INTEGER,
        "End coordinate of D region alignment (1-based)"
    ),
    "d2_sequence_start": AIRRField(
        "d2_sequence_start", AIRRFieldType.INTEGER,
        "Start coordinate of second D region in sequence (1-based)"
    ),
    "d2_sequence_end": AIRRField(
        "d2_sequence_end", AIRRFieldType.INTEGER,
        "End coordinate of second D region in sequence (1-based)"
    ),
    "d2_germline_start": AIRRField(
        "d2_germline_start", AIRRFieldType.INTEGER,
        "Start coordinate of second D region in germline (1-based)"
    ),
    "d2_germline_end": AIRRField(
        "d2_germline_end", AIRRFieldType.INTEGER,
        "End coordinate of second D region in germline (1-based)"
    ),
    "d2_alignment_start": AIRRField(
        "d2_alignment_start", AIRRFieldType.INTEGER,
        "Start coordinate of second D region alignment (1-based)"
    ),
    "d2_alignment_end": AIRRField(
        "d2_alignment_end", AIRRFieldType.INTEGER,
        "End coordinate of second D region alignment (1-based)"
    ),
    "j_sequence_start": AIRRField(
        "j_sequence_start", AIRRFieldType.INTEGER,
        "Start coordinate of J region in sequence (1-based)"
    ),
    "j_sequence_end": AIRRField(
        "j_sequence_end", AIRRFieldType.INTEGER,
        "End coordinate of J region in sequence (1-based)"
    ),
    "j_germline_start": AIRRField(
        "j_germline_start", AIRRFieldType.INTEGER,
        "Start coordinate of J region in germline (1-based)"
    ),
    "j_germline_end": AIRRField(
        "j_germline_end", AIRRFieldType.INTEGER,
        "End coordinate of J region in germline (1-based)"
    ),
    "j_alignment_start": AIRRField(
        "j_alignment_start", AIRRFieldType.INTEGER,
        "Start coordinate of J region alignment (1-based)"
    ),
    "j_alignment_end": AIRRField(
        "j_alignment_end", AIRRFieldType.INTEGER,
        "End coordinate of J region alignment (1-based)"
    ),

    # CDR and framework coordinates
    "cdr1_start": AIRRField(
        "cdr1_start", AIRRFieldType.INTEGER,
        "Start coordinate of CDR1 (1-based)"
    ),
    "cdr1_end": AIRRField(
        "cdr1_end", AIRRFieldType.INTEGER,
        "End coordinate of CDR1 (1-based)"
    ),
    "cdr2_start": AIRRField(
        "cdr2_start", AIRRFieldType.INTEGER,
        "Start coordinate of CDR2 (1-based)"
    ),
    "cdr2_end": AIRRField(
        "cdr2_end", AIRRFieldType.INTEGER,
        "End coordinate of CDR2 (1-based)"
    ),
    "cdr3_start": AIRRField(
        "cdr3_start", AIRRFieldType.INTEGER,
        "Start coordinate of CDR3 (1-based)"
    ),
    "cdr3_end": AIRRField(
        "cdr3_end", AIRRFieldType.INTEGER,
        "End coordinate of CDR3 (1-based)"
    ),
    "fwr1_start": AIRRField(
        "fwr1_start", AIRRFieldType.INTEGER,
        "Start coordinate of FWR1 (1-based)"
    ),
    "fwr1_end": AIRRField(
        "fwr1_end", AIRRFieldType.INTEGER,
        "End coordinate of FWR1 (1-based)"
    ),
    "fwr2_start": AIRRField(
        "fwr2_start", AIRRFieldType.INTEGER,
        "Start coordinate of FWR2 (1-based)"
    ),
    "fwr2_end": AIRRField(
        "fwr2_end", AIRRFieldType.INTEGER,
        "End coordinate of FWR2 (1-based)"
    ),
    "fwr3_start": AIRRField(
        "fwr3_start", AIRRFieldType.INTEGER,
        "Start coordinate of FWR3 (1-based)"
    ),
    "fwr3_end": AIRRField(
        "fwr3_end", AIRRFieldType.INTEGER,
        "End coordinate of FWR3 (1-based)"
    ),
    "fwr4_start": AIRRField(
        "fwr4_start", AIRRFieldType.INTEGER,
        "Start coordinate of FWR4 (1-based)"
    ),
    "fwr4_end": AIRRField(
        "fwr4_end", AIRRFieldType.INTEGER,
        "End coordinate of FWR4 (1-based)"
    ),

    # Additional alignment sequences
    "v_sequence_alignment": AIRRField(
        "v_sequence_alignment", AIRRFieldType.STRING,
        "Portion of sequence aligned to V reference"
    ),
    "v_sequence_alignment_aa": AIRRField(
        "v_sequence_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of V alignment"
    ),
    "d_sequence_alignment": AIRRField(
        "d_sequence_alignment", AIRRFieldType.STRING,
        "Portion of sequence aligned to D reference"
    ),
    "d_sequence_alignment_aa": AIRRField(
        "d_sequence_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of D alignment"
    ),
    "d2_sequence_alignment": AIRRField(
        "d2_sequence_alignment", AIRRFieldType.STRING,
        "Portion of sequence aligned to second D reference"
    ),
    "d2_sequence_alignment_aa": AIRRField(
        "d2_sequence_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of second D alignment"
    ),
    "j_sequence_alignment": AIRRField(
        "j_sequence_alignment", AIRRFieldType.STRING,
        "Portion of sequence aligned to J reference"
    ),
    "j_sequence_alignment_aa": AIRRField(
        "j_sequence_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of J alignment"
    ),
    "c_sequence_alignment": AIRRField(
        "c_sequence_alignment", AIRRFieldType.STRING,
        "Portion of sequence aligned to C reference"
    ),
    "c_sequence_alignment_aa": AIRRField(
        "c_sequence_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of C alignment"
    ),
    "v_germline_alignment": AIRRField(
        "v_germline_alignment", AIRRFieldType.STRING,
        "Portion of germline V aligned to sequence"
    ),
    "v_germline_alignment_aa": AIRRField(
        "v_germline_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of germline V alignment"
    ),
    "d_germline_alignment": AIRRField(
        "d_germline_alignment", AIRRFieldType.STRING,
        "Portion of germline D aligned to sequence"
    ),
    "d_germline_alignment_aa": AIRRField(
        "d_germline_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of germline D alignment"
    ),
    "d2_germline_alignment": AIRRField(
        "d2_germline_alignment", AIRRFieldType.STRING,
        "Portion of germline second D aligned to sequence"
    ),
    "d2_germline_alignment_aa": AIRRField(
        "d2_germline_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of germline second D alignment"
    ),
    "j_germline_alignment": AIRRField(
        "j_germline_alignment", AIRRFieldType.STRING,
        "Portion of germline J aligned to sequence"
    ),
    "j_germline_alignment_aa": AIRRField(
        "j_germline_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of germline J alignment"
    ),
    "c_germline_alignment": AIRRField(
        "c_germline_alignment", AIRRFieldType.STRING,
        "Portion of germline C aligned to sequence"
    ),
    "c_germline_alignment_aa": AIRRField(
        "c_germline_alignment_aa", AIRRFieldType.STRING,
        "Amino acid sequence of germline C alignment"
    ),

    # N/P region lengths
    "np1_length": AIRRField(
        "np1_length", AIRRFieldType.INTEGER,
        "Length of N/P region between V and D segments"
    ),
    "np2_length": AIRRField(
        "np2_length", AIRRFieldType.INTEGER,
        "Length of N/P region between D and J segments"
    ),
    "np3_length": AIRRField(
        "np3_length", AIRRFieldType.INTEGER,
        "Length of N/P region for V-J rearrangements"
    ),
    "n1_length": AIRRField(
        "n1_length", AIRRFieldType.INTEGER,
        "Length of N region additions between V and D segments"
    ),
    "n2_length": AIRRField(
        "n2_length", AIRRFieldType.INTEGER,
        "Length of N region additions between D and J segments"
    ),
    "n3_length": AIRRField(
        "n3_length", AIRRFieldType.INTEGER,
        "Length of N region additions for V-J rearrangements"
    ),
    "p3v_length": AIRRField(
        "p3v_length", AIRRFieldType.INTEGER,
        "Length of P nucleotides added to 3' end of V region"
    ),
    "p5d_length": AIRRField(
        "p5d_length", AIRRFieldType.INTEGER,
        "Length of P nucleotides added to 5' end of D region"
    ),
    "p3d_length": AIRRField(
        "p3d_length", AIRRFieldType.INTEGER,
        "Length of P nucleotides added to 3' end of D region"
    ),
    "p5d2_length": AIRRField(
        "p5d2_length", AIRRFieldType.INTEGER,
        "Length of P nucleotides added to 5' end of second D region"
    ),
    "p3d2_length": AIRRField(
        "p3d2_length", AIRRFieldType.INTEGER,
        "Length of P nucleotides added to 3' end of second D region"
    ),
    "p5j_length": AIRRField(
        "p5j_length", AIRRFieldType.INTEGER,
        "Length of P nucleotides added to 5' end of J region"
    ),

    # Clone and frequency information
    "consensus_count": AIRRField(
        "consensus_count", AIRRFieldType.INTEGER,
        "Number of reads supporting consensus sequence"
    ),
    "duplicate_count": AIRRField(
        "duplicate_count", AIRRFieldType.INTEGER,
        "Number of duplicate reads for this sequence",
        default_value=1
    ),
    "duplicate_frequency": AIRRField(
        "duplicate_frequency", AIRRFieldType.NUMBER,
        "Frequency of this sequence within the repertoire"
    ),

    # Cell and clone identifiers
    "cell_id": AIRRField(
        "cell_id", AIRRFieldType.STRING,
        "Cell identifier for single-cell data"
    ),
    "clone_id": AIRRField(
        "clone_id", AIRRFieldType.STRING,
        "Clone identifier linking sequences of common clonal origin"
    ),

    # Sample and processing identifiers
    "repertoire_id": AIRRField(
        "repertoire_id", AIRRFieldType.STRING,
        "Unique identifier for the repertoire",
        required=True, example="subject_1_timepoint_0"
    ),
    "sample_processing_id": AIRRField(
        "sample_processing_id", AIRRFieldType.STRING,
        "Unique identifier for sample processing procedure"
    ),
    "data_processing_id": AIRRField(
        "data_processing_id", AIRRFieldType.STRING,
        "Unique identifier for data processing procedure"
    ),

    # Additional annotations
    "reading_frame": AIRRField(
        "reading_frame", AIRRFieldType.STRING,
        "Reading frame designation (in-frame, out-of-frame)",
        example="in-frame"
    ),
    "v_family": AIRRField(
        "v_family", AIRRFieldType.STRING,
        "V gene family designation",
        example="TRBV12"
    ),
    "d_family": AIRRField(
        "d_family", AIRRFieldType.STRING,
        "D gene family designation",
        example="TRBD1"
    ),
    "j_family": AIRRField(
        "j_family", AIRRFieldType.STRING,
        "J gene family designation",
        example="TRBJ2"
    ),

    # Additional 10X specific fields
    "is_cell": AIRRField(
        "is_cell", AIRRFieldType.BOOLEAN,
        "True if sequence is from a cell (10X Genomics)",
        default_value=True
    ),
    "high_confidence": AIRRField(
        "high_confidence", AIRRFieldType.BOOLEAN,
        "High confidence sequence annotation",
        default_value=True
    ),
    "full_length": AIRRField(
        "full_length", AIRRFieldType.BOOLEAN,
        "True if sequence is full length",
        default_value=False
    ),

    # Chain-specific fields for paired data
    "tra_junction": AIRRField(
        "tra_junction", AIRRFieldType.STRING,
        "TRA chain junction sequence"
    ),
    "tra_junction_aa": AIRRField(
        "tra_junction_aa", AIRRFieldType.STRING,
        "TRA chain junction amino acid sequence"
    ),
    "tra_v_call": AIRRField(
        "tra_v_call", AIRRFieldType.STRING,
        "TRA chain V gene assignment"
    ),
    "tra_d_call": AIRRField(
        "tra_d_call", AIRRFieldType.STRING,
        "TRA chain D gene assignment"
    ),
    "tra_j_call": AIRRField(
        "tra_j_call", AIRRFieldType.STRING,
        "TRA chain J gene assignment"
    ),
    "trb_junction": AIRRField(
        "trb_junction", AIRRFieldType.STRING,
        "TRB chain junction sequence"
    ),
    "trb_junction_aa": AIRRField(
        "trb_junction_aa", AIRRFieldType.STRING,
        "TRB chain junction amino acid sequence"
    ),
    "trb_v_call": AIRRField(
        "trb_v_call", AIRRFieldType.STRING,
        "TRB chain V gene assignment"
    ),
    "trb_d_call": AIRRField(
        "trb_d_call", AIRRFieldType.STRING,
        "TRB chain D gene assignment"
    ),
    "trb_j_call": AIRRField(
        "trb_j_call", AIRRFieldType.STRING,
        "TRB chain J gene assignment"
    ),
}


def get_airr_field_names() -> List[str]:
    """Get list of all AIRR field names."""
    return list(AIRR_SCHEMA_FIELDS.keys())


def get_required_airr_fields() -> List[str]:
    """Get list of required AIRR field names."""
    return [name for name, field in AIRR_SCHEMA_FIELDS.items() if field.required]


def get_essential_airr_fields() -> List[str]:
    """
    Get list of essential AIRR fields that are commonly used.

    This is a subset of all AIRR fields focusing on the most critical
    fields for analysis, reducing memory overhead.

    Returns:
        List of essential field names
    """
    return [
        # Core identifiers
        "sequence_id",
        "repertoire_id",

        # Sequences
        "sequence",
        "sequence_aa",
        "junction",
        "junction_aa",
        "junction_length",
        "junction_aa_length",

        # Gene calls
        "v_call",
        "d_call",
        "j_call",
        "c_call",

        # Status flags
        "productive",
        "vj_in_frame",
        "stop_codon",
        "locus",

        # Counts and frequencies
        "duplicate_count",
        "duplicate_frequency",
        "consensus_count",

        # Gene families
        "v_family",
        "d_family",
        "j_family",

        # CDR regions
        "cdr1",
        "cdr1_aa",
        "cdr2",
        "cdr2_aa",
        "cdr3",
        "cdr3_aa",

        # Clone identifiers
        "clone_id",
        "cell_id"
    ]


def get_airr_field_types() -> Dict[str, str]:
    """Get mapping of field names to types."""
    return {name: field.field_type.value for name, field in AIRR_SCHEMA_FIELDS.items()}


def get_airr_default_values() -> Dict[str, Any]:
    """Get mapping of field names to default values."""
    return {
        name: field.default_value
        for name, field in AIRR_SCHEMA_FIELDS.items()
        if field.default_value is not None
    }


def create_empty_airr_dataframe(backend: str = "polars"):
    """
    Create an empty DataFrame with all AIRR fields.

    Args:
        backend: "polars" or "pandas"

    Returns:
        Empty DataFrame with AIRR schema or dict if libraries not available
    """
    field_types = get_airr_field_types()
    default_values = get_airr_default_values()

    if backend == "polars" and HAS_POLARS:
        # Create polars schema
        schema = {}
        for name, field_type in field_types.items():
            if field_type == "string":
                schema[name] = pl.Utf8
            elif field_type == "integer":
                schema[name] = pl.Int64
            elif field_type == "number":
                schema[name] = pl.Float64
            elif field_type == "boolean":
                schema[name] = pl.Boolean

        return pl.DataFrame(schema=schema)

    elif backend == "pandas" and HAS_PANDAS:
        # Create empty DataFrame with appropriate dtypes
        data = {}
        for name, field_type in field_types.items():
            if field_type == "string":
                data[name] = pd.Series([], dtype="string")
            elif field_type == "integer":
                data[name] = pd.Series([], dtype="Int64")
            elif field_type == "number":
                data[name] = pd.Series([], dtype="float64")
            elif field_type == "boolean":
                data[name] = pd.Series([], dtype="boolean")

        return pd.DataFrame(data)

    else:
        # Return schema information as dict if libraries not available
        return {
            "schema": field_types,
            "defaults": default_values,
            "message": f"Cannot create {backend} DataFrame - library not available"
        }


def validate_airr_compliance(data) -> Dict[str, Any]:
    """
    Validate data against AIRR schema.

    Args:
        data: DataFrame to validate or column list

    Returns:
        Validation report
    """
    report = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "statistics": {},
        "missing_required": [],
        "missing_optional": [],
        "extra_fields": []
    }

    # Handle different input types
    if hasattr(data, 'columns'):
        # DataFrame-like object
        columns = list(data.columns)
        if HAS_PANDAS and isinstance(data, pd.DataFrame):
            total_rows = len(data)
            empty_sequences = (data["junction_aa"] == "").sum() if "junction_aa" in columns else 0
        elif HAS_POLARS and isinstance(data, pl.DataFrame):
            total_rows = data.height
            empty_sequences = data.filter(pl.col("junction_aa") == "").height if "junction_aa" in columns else 0
        else:
            total_rows = 0
            empty_sequences = 0
    elif isinstance(data, (list, tuple)):
        # Column list
        columns = list(data)
        total_rows = 0
        empty_sequences = 0
    else:
        report["errors"].append("Invalid data type for validation")
        return report

    airr_fields = set(get_airr_field_names())
    required_fields = set(get_required_airr_fields())

    # Check required fields
    missing_required = required_fields - set(columns)
    if missing_required:
        report["valid"] = False
        report["errors"].append(f"Missing required fields: {sorted(missing_required)}")
        report["missing_required"] = sorted(missing_required)

    # Check optional fields
    missing_optional = (airr_fields - required_fields) - set(columns)
    if missing_optional:
        report["warnings"].append(f"Missing optional fields: {len(missing_optional)} fields")
        report["missing_optional"] = sorted(missing_optional)

    # Check for extra fields
    extra_fields = set(columns) - airr_fields
    if extra_fields:
        report["warnings"].append(f"Extra non-AIRR fields: {sorted(extra_fields)}")
        report["extra_fields"] = sorted(extra_fields)

    # Statistics
    report["statistics"] = {
        "total_rows": total_rows,
        "total_columns": len(columns),
        "airr_fields_present": len(set(columns) & airr_fields),
        "airr_fields_total": len(airr_fields),
        "required_fields_present": len(set(columns) & required_fields),
        "required_fields_total": len(required_fields),
        "empty_sequences": empty_sequences,
        "compliance_percentage": round(len(set(columns) & airr_fields) / len(airr_fields) * 100, 1) if airr_fields else 0
    }

    return report