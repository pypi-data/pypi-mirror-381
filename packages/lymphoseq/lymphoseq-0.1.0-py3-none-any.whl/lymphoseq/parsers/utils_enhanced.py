"""
Enhanced utility functions for AIRR-seq data parsing and standardization.

Full AIRR schema compliance with comprehensive field mappings.
Compatible with LymphoSeq2 and extends functionality for modern Python stack.
"""

import re
import pandas as pd
import polars as pl
from typing import Dict, List, Union, Optional, Any
from pathlib import Path

# Suppress pandas FutureWarning about downcasting
pd.set_option('future.no_silent_downcasting', True)

from .airr_schema import (
    AIRR_SCHEMA_FIELDS,
    get_airr_field_names,
    get_required_airr_fields,
    get_essential_airr_fields,
    get_airr_default_values,
    create_empty_airr_dataframe,
    validate_airr_compliance
)


# Enhanced comprehensive column name mappings from different platforms
ENHANCED_COLUMN_MAPPINGS = {
    "immunoseq": {
        # ImmunoSEQ v3 mappings - comprehensive coverage
        "bio_identity": "sequence_id",
        "rearrangement": "sequence",
        "amino_acid": "sequence_aa",
        "frame_type": "productive",
        "v_gene": "v_call",
        "d_gene": "d_call",
        "d_gene_ties": "d2_call",
        "j_gene": "j_call",
        "c_gene": "c_call",
        "cdr3_rearrangement": "junction",
        "cdr3_amino_acid": "junction_aa",
        "cdr3_sequence": "junction",
        "cdr3_sequence_aa": "junction_aa",
        "cdr1_rearrangement": "cdr1",
        "cdr1_amino_acid": "cdr1_aa",
        "cdr2_rearrangement": "cdr2",
        "cdr2_amino_acid": "cdr2_aa",
        "cdr1_sequence": "cdr1",
        "cdr1_sequence_aa": "cdr1_aa",
        "cdr2_sequence": "cdr2",
        "cdr2_sequence_aa": "cdr2_aa",
        "cdr1_start_index": "cdr1_start",
        "cdr1_rearrangement_length": "cdr1_end",
        "cdr2_start_index": "cdr2_start",
        "cdr2_rearrangement_length": "cdr2_end",
        "cdr3_start_index": "cdr3_start",
        "cdr3_rearrangement_length": "cdr3_end",
        "cdr3_length": "junction_length",
        "n1_insertions": "n1_length",
        "n2_insertions": "n2_length",
        "v_deletions": "v_deletions",
        "d5_deletions": "d5_deletions",
        "d3_deletions": "d3_deletions",
        "j_deletions": "j_deletions",
        "templates": "duplicate_count",
        "seq_reads": "duplicate_count",
        "frequency": "duplicate_frequency",
        "productive_frequency": "productive_frequency",
        "v_family": "v_family",
        "d_family": "d_family",
        "j_family": "j_family",
        "v_allele": "v_allele",
        "d_allele": "d_allele",
        "j_allele": "j_allele",

        # ACTUAL ImmunoSEQ column mappings (based on real file headers)
        # Legacy format (TRA, IGH, IGKL, old TRB)
        "nucleotide": "sequence",
        "aminoAcid": "junction_aa",
        "count": "duplicate_count",
        "count (reads)": "duplicate_count",           # IGKL format
        "frequencyCount": "duplicate_frequency",
        "frequencyCount (%)": "duplicate_frequency",  # IGKL format
        "cdr3Length": "junction_length",

        # V3 format (modern TRB_V3)
        "bio_identity": "sequence_id",
        "rearrangement": "sequence",
        "amino_acid": "junction_aa",
        "frame_type": "productive",
        "rearrangement_type": "locus",
        "templates": "duplicate_count",
        "seq_reads": "duplicate_count",
        "frequency": "duplicate_frequency",
        "productive_frequency": "productive_frequency",
        "cdr3_length": "junction_length",
        "v_family": "v_family",
        "v_gene": "v_gene",
        "v_allele": "v_allele",
        "d_family": "d_family",
        "d_gene": "d_gene",
        "d_allele": "d_allele",
        "j_family": "j_family",
        "j_gene": "j_gene",
        "j_allele": "j_allele",
        "v_deletions": "v_deletions",
        "d5_deletions": "d5_deletions",
        "d3_deletions": "d3_deletions",
        "j_deletions": "j_deletions",
        "n1_insertions": "np1_length",
        "n2_insertions": "np2_length",

        # V gene annotations (corrected mapping)
        "vMaxResolved": "v_call",           # Full allele: TRBV12-1*01
        "vFamilyName": "v_family",          # Family: TRBV12
        "vGeneName": "v_gene",              # Gene: TRBV12-1
        "vGeneAllele": "v_allele",          # Allele: *01
        "vFamilyTies": "v_score",
        "vGeneNameTies": "v_identity",
        "vGeneAlleleTies": "v_support",

        # D gene annotations (corrected mapping)
        "dMaxResolved": "d_call",           # Full allele: TRBD1*01
        "dFamilyName": "d_family",          # Family: TRBD1
        "dGeneName": "d_gene",              # Gene: TRBD1
        "dGeneAllele": "d_allele",          # Allele: *01
        "dFamilyTies": "d_score",
        "dGeneNameTies": "d_identity",
        "dGeneAlleleTies": "d_support",

        # J gene annotations (corrected mapping)
        "jMaxResolved": "j_call",           # Full allele: TRBJ2-1*01
        "jFamilyName": "j_family",          # Family: TRBJ2
        "jGeneName": "j_gene",              # Gene: TRBJ2-1
        "jGeneAllele": "j_allele",          # Allele: *01
        "jFamilyTies": "j_score",
        "jGeneNameTies": "j_identity",
        "jGeneAlleleTies": "j_support",

        # Deletions and insertions
        "vDeletion": "v_deletions",
        "d5Deletion": "d5_deletions",
        "d3Deletion": "d3_deletions",
        "jDeletion": "j_deletions",
        "n1Insertion": "np1_length",
        "n2Insertion": "np2_length",

        # Position indices
        "vIndex": "v_start",
        "n1Index": "np1_start",
        "dIndex": "d_start",
        "n2Index": "np2_start",
        "jIndex": "j_start",

        # Quality and status
        "estimatedNumberGenomes": "umi_count",
        "sequenceStatus": "productive",
        "cloneResolved": "clone_status",  # Map to different field to avoid duplicate
        "vOrphon": "v_orphon",
        "dOrphon": "d_orphon",
        "jOrphon": "j_orphon",
        "vFunction": "v_functional",
        "dFunction": "d_functional",
        "jFunction": "j_functional",
        "fractionNucleated": "c_call",

        # IGH-specific fields (somatic hypermutation)
        "vAlignLength": "v_alignment_length",
        "vAlignSubstitutionCount": "v_mutations",
        "vAlignSubstitutionIndexes": "v_mutation_positions",
        "vAlignSubstitutionGeneThreePrimeIndexes": "v_mutation_gene_positions",
        "vSeqWithMutations": "v_sequence_mutations",

        # Alternative formats
        "count (templates/reads)": "duplicate_count",
        "count (templates)": "duplicate_count",
        "count (reads)": "duplicate_count",
        "frequencyCount (%)": "duplicate_frequency",
        "frame_type": "vj_in_frame",
    },

    "bgi": {
        # BGI IR-SEQ mappings - complete coverage
        "Sequence.ID": "sequence_id",
        "CDR3_aa": "junction_aa",
        "CDR3_nt": "junction",
        "CDR3.stripped.x.a": "junction_aa",
        "nucleotide(CDR3 in lowercase)": "junction",
        "aminoAcid(CDR3 in lowercase)": "junction_aa",
        "V_gene": "v_call",
        "vGene": "v_call",
        "D_gene": "d_call",
        "dGene": "d_call",
        "J_gene": "j_call",
        "jGene": "j_call",
        "reads": "duplicate_count",
        "cloneCount": "duplicate_count",
        "frequency": "duplicate_frequency",
        "clonefrequency (%)": "duplicate_frequency",
        "CDR3Length": "junction_length",
        "vDeletion": "v_deletions",
        "d5Deletion": "d5_deletions",
        "d3Deletion": "d3_deletions",
        "jDeletion": "j_deletions",
        "vdInsertion": "np1_length",
        "djInsertion": "np2_length",
        "vjInsertion": "np3_length",
        "function": "productive",
        "fuction": "productive",  # Common BGI typo
        "estimatedNumberGenomes": "duplicate_count",
    },

    "mixcr": {
        # MiXCR pipeline mappings - comprehensive
        "cloneId": "clone_id",
        "cloneCount": "duplicate_count",
        "cloneFraction": "duplicate_frequency",
        "targetSequences": "sequence",
        "targetQualities": "sequence_quality",
        "allVHitsWithScore": "v_call",
        "allDHitsWithScore": "d_call",
        "allJHitsWithScore": "j_call",
        "allCHitsWithScore": "c_call",
        "allVAlignments": "v_cigar",
        "allDAlignments": "d_cigar",
        "allJAlignments": "j_cigar",
        "allCAlignments": "c_cigar",
        "nSeqFR1": "fwr1",
        "minQualFR1": "fwr1_quality",
        "nSeqCDR1": "cdr1",
        "minQualCDR1": "cdr1_quality",
        "nSeqFR2": "fwr2",
        "minQualFR2": "fwr2_quality",
        "nSeqCDR2": "cdr2",
        "minQualCDR2": "cdr2_quality",
        "nSeqFR3": "fwr3",
        "minQualFR3": "fwr3_quality",
        "nSeqCDR3": "junction",
        "minQualCDR3": "junction_quality",
        "nSeqFR4": "fwr4",
        "minQualFR4": "fwr4_quality",
        "aaSeqFR1": "fwr1_aa",
        "aaSeqCDR1": "cdr1_aa",
        "aaSeqFR2": "fwr2_aa",
        "aaSeqCDR2": "cdr2_aa",
        "aaSeqFR3": "fwr3_aa",
        "aaSeqCDR3": "junction_aa",
        "aaSeqFR4": "fwr4_aa",
        "refPoints": "reference_points",
        "bestVHit": "v_call",
        "bestDHit": "d_call",
        "bestJHit": "j_call",
        "bestCHit": "c_call",
        "bestVGene": "v_call",
        "bestDGene": "d_call",
        "bestJGene": "j_call",
        "bestCGene": "c_call",
    },

    "tenx": {
        # 10X Genomics VDJ mappings - complete
        "barcode": "cell_id",
        "is_cell": "is_cell",
        "contig_id": "sequence_id",
        "high_confidence": "high_confidence",
        "length": "sequence_length",
        "chain": "locus",
        "v_gene": "v_call",
        "d_gene": "d_call",
        "j_gene": "j_call",
        "c_gene": "c_call",
        "full_length": "full_length",
        "productive": "productive",
        "cdr3": "junction_aa",
        "cdr3_nt": "junction",
        "reads": "duplicate_count",
        "umis": "consensus_count",
        "umi_count": "consensus_count",
        "raw_clonotype_id": "clone_id",
        "raw_consensus_id": "consensus_id",
        "exact_subclonotype_id": "exact_subclonotype_id",
        "sequence": "sequence",
        "rev_comp": "rev_comp",
        "productive": "productive",
        "v_start": "v_sequence_start",
        "v_end": "v_sequence_end",
        "d_start": "d_sequence_start",
        "d_end": "d_sequence_end",
        "j_start": "j_sequence_start",
        "j_end": "j_sequence_end",
        "c_start": "c_sequence_start",
        "c_end": "c_sequence_end",
    }
}


def standardize_airr_data(
    data: Union[pd.DataFrame, pl.DataFrame],
    platform: str = "auto",
    repertoire_id: Optional[str] = None,
    use_enhanced_mappings: bool = True,
    use_essential_fields_only: bool = True,
    verbose: bool = True
) -> Union[pd.DataFrame, pl.DataFrame]:
    """
    Standardize data to AIRR format with optimized memory usage.

    Args:
        data: Input data frame
        platform: Platform type for column mapping
        repertoire_id: Repertoire identifier to add
        use_enhanced_mappings: Use comprehensive field mappings
        use_essential_fields_only: Only add essential AIRR fields (saves memory)
        verbose: Show progress messages

    Returns:
        Standardized AIRR-compliant data frame
    """
    is_polars = isinstance(data, pl.DataFrame)

    # Auto-detect platform if not specified
    if platform == "auto":
        columns_list = data.columns if is_polars else data.columns.tolist()
        platform = detect_platform(columns_list)

    # Use polars native operations when possible
    if is_polars and use_enhanced_mappings and platform in ENHANCED_COLUMN_MAPPINGS:
        column_mapping = ENHANCED_COLUMN_MAPPINGS[platform]

        # Progress tracking
        if verbose and len(data) > 1000:
            print(f"🔧 Standardizing {len(data):,} sequences to AIRR format...")

        # Rename columns using polars (only rename columns that exist)
        # Filter mapping to only include columns present in the data
        # Also avoid creating duplicate columns
        existing_mapping = {}
        mapped_targets = set()  # Track which target names have been used

        for old_name, new_name in column_mapping.items():
            if old_name in data.columns:
                # Only add if:
                # 1. The new name doesn't already exist in the data, OR
                # 2. We're renaming to itself (old_name == new_name), AND
                # 3. We haven't already mapped another column to this target name
                if (new_name not in data.columns or new_name == old_name) and new_name not in mapped_targets:
                    existing_mapping[old_name] = new_name
                    mapped_targets.add(new_name)

        if existing_mapping:
            data = data.rename(existing_mapping)

        # Determine which fields to add
        if use_essential_fields_only:
            airr_fields = get_essential_airr_fields()
        else:
            airr_fields = get_airr_field_names()

        default_values = get_airr_default_values()
        missing_fields = [field for field in airr_fields if field not in data.columns]

        # Add missing columns using polars expressions (very efficient)
        if missing_fields:
            if verbose and len(missing_fields) > 20 and len(data) > 1000:
                print(f"   Adding {len(missing_fields)} missing AIRR fields...")

            new_cols = []
            for field in missing_fields:
                if field in default_values:
                    new_cols.append(pl.lit(default_values[field]).alias(field))
                elif field == "repertoire_id" and repertoire_id:
                    new_cols.append(pl.lit(repertoire_id).alias(field))
                else:
                    field_def = AIRR_SCHEMA_FIELDS.get(field)
                    if field_def:
                        if field_def.field_type.value == "string":
                            new_cols.append(pl.lit("").alias(field))
                        else:
                            new_cols.append(pl.lit(None).alias(field))

            if new_cols:
                data = data.with_columns(new_cols)

        # Generate sequence_id if missing
        if "sequence_id" not in data.columns:
            data = data.with_row_count(name="sequence_id", offset=1)
            # Convert to string with repertoire prefix if available
            if repertoire_id:
                data = data.with_columns(
                    pl.format("{}_{}", pl.lit(repertoire_id), pl.col("sequence_id")).alias("sequence_id")
                )
            else:
                data = data.with_columns(
                    pl.col("sequence_id").cast(pl.Utf8)
                )

        # Apply cleaning using polars native operations
        data = clean_and_validate_sequences_polars(data)
        data = clean_gene_calls_polars(data)
        data = compute_derived_fields_polars(data, platform)

        # Reorder columns
        available_airr_cols = [col for col in airr_fields if col in data.columns]
        other_cols = [col for col in data.columns if col not in airr_fields]
        data = data.select(available_airr_cols + other_cols)

        return data

    # Pandas fallback for non-polars or when needed
    if is_polars:
        df = data.to_pandas()
    else:
        df = data.copy()

    # Auto-detect platform
    if platform == "auto":
        platform = detect_platform(df.columns.tolist())

    # Apply enhanced column mappings
    if use_enhanced_mappings and platform in ENHANCED_COLUMN_MAPPINGS:
        column_mapping = ENHANCED_COLUMN_MAPPINGS[platform]

        # Filter mapping to only include columns present in the data
        # Also avoid creating duplicate columns
        existing_mapping = {}
        mapped_targets = set()  # Track which target names have been used

        for old_name, new_name in column_mapping.items():
            if old_name in df.columns:
                # Only add if:
                # 1. The new name doesn't already exist in the data, OR
                # 2. We're renaming to itself (old_name == old_name), AND
                # 3. We haven't already mapped another column to this target name
                if (new_name not in df.columns or new_name == old_name) and new_name not in mapped_targets:
                    existing_mapping[old_name] = new_name
                    mapped_targets.add(new_name)

        if existing_mapping:
            df = df.rename(columns=existing_mapping)

        if df.columns.duplicated().any():
            df.columns = pd.io.common.dedup_names(df.columns, is_potential_multiindex=False)

        if verbose and len(df) > 1000:
            print(f"🔧 Standardizing {len(df):,} sequences to AIRR format...")

    # Determine which fields to add
    if use_essential_fields_only:
        airr_fields = get_essential_airr_fields()
    else:
        airr_fields = get_airr_field_names()

    default_values = get_airr_default_values()
    missing_fields = [field for field in airr_fields if field not in df.columns]

    # Add missing columns efficiently
    if missing_fields:
        if verbose and len(missing_fields) > 20 and len(df) > 1000:
            print(f"   Adding {len(missing_fields)} missing AIRR fields...")

        missing_data = {}
        for field in missing_fields:
            if field in default_values:
                missing_data[field] = default_values[field]
            elif field == "repertoire_id" and repertoire_id:
                missing_data[field] = repertoire_id
            else:
                field_def = AIRR_SCHEMA_FIELDS.get(field)
                if field_def:
                    if field_def.field_type.value == "string":
                        missing_data[field] = ""
                    elif field_def.field_type.value == "integer":
                        missing_data[field] = pd.NA
                    elif field_def.field_type.value == "number":
                        missing_data[field] = pd.NA
                    elif field_def.field_type.value == "boolean":
                        missing_data[field] = pd.NA

        # Add all columns at once
        if missing_data:
            missing_df = pd.DataFrame({
                col: [value] * len(df) for col, value in missing_data.items()
            })
            df = pd.concat([df, missing_df], axis=1)

    # Generate sequence_id if missing
    if "sequence_id" not in df.columns:
        if repertoire_id:
            df["sequence_id"] = [f"{repertoire_id}_{i+1}" for i in range(len(df))]
        else:
            df["sequence_id"] = [str(i+1) for i in range(len(df))]

    # Apply cleaning
    df = clean_and_validate_sequences(df)
    df = clean_gene_calls_enhanced(df)
    df = compute_derived_fields(df, platform)

    # Reorder columns
    available_airr_cols = [col for col in airr_fields if col in df.columns]
    other_cols = [col for col in df.columns if col not in airr_fields]
    df = df[available_airr_cols + other_cols]

    return pl.from_pandas(df) if is_polars else df


def detect_platform(columns: List[str]) -> str:
    """
    Enhanced platform detection based on column names.

    Args:
        columns: List of column names

    Returns:
        Detected platform name
    """
    columns_lower = [col.lower() for col in columns]

    # Count platform-specific indicators
    immunoseq_score = 0
    bgi_score = 0
    mixcr_score = 0
    tenx_score = 0

    # ImmunoSEQ indicators
    immunoseq_indicators = [
        "bio_identity", "rearrangement", "amino_acid", "nucleotide",
        "aminoacid", "frame_type", "templates", "seq_reads", "v_gene", "d_gene"
    ]
    for indicator in immunoseq_indicators:
        if any(indicator in col for col in columns_lower):
            immunoseq_score += 1

    # BGI indicators (check for specific BGI column names with parentheses)
    # Strong indicators (unique to BGI)
    if any("nucleotide(cdr3" in col or "aminoacid(cdr3" in col for col in columns_lower):
        bgi_score += 10  # Very strong indicator

    bgi_indicators = [
        "sequence.id", "cdr3_aa", "cdr3_nt", "vgene", "dgene", "jgene",
        "clonecount", "clonefrequency", "function", "fuction"
    ]
    for indicator in bgi_indicators:
        if any(indicator in col for col in columns_lower):
            bgi_score += 1

    # MiXCR indicators
    mixcr_indicators = [
        "cloneid", "targetsequences", "allvhitswithscore", "nseqcdr3",
        "aaseqcdr3", "refpoints", "targetqualities"
    ]
    for indicator in mixcr_indicators:
        if any(indicator in col for col in columns_lower):
            mixcr_score += 1

    # 10X indicators
    tenx_indicators = [
        "barcode", "contig_id", "is_cell", "high_confidence", "chain",
        "raw_clonotype_id", "umis", "exact_subclonotype"
    ]
    for indicator in tenx_indicators:
        if any(indicator in col for col in columns_lower):
            tenx_score += 1

    # Return platform with highest score
    scores = {
        "immunoseq": immunoseq_score,
        "bgi": bgi_score,
        "mixcr": mixcr_score,
        "tenx": tenx_score
    }

    max_platform = max(scores.items(), key=lambda x: x[1])

    # Require minimum threshold for detection
    if max_platform[1] >= 2:
        return max_platform[0]
    else:
        return "generic"


def clean_and_validate_sequences_polars(data: pl.DataFrame) -> pl.DataFrame:
    """
    Polars-native sequence cleaning and validation (optimized).

    Args:
        data: Polars DataFrame with sequence columns

    Returns:
        DataFrame with cleaned sequences
    """
    # Clean junction_aa and junction using polars expressions
    cleaning_exprs = []

    if "junction_aa" in data.columns:
        # BGI format: lowercase = CDR3, uppercase = framework
        # Extract only lowercase letters (the actual CDR3), then uppercase them
        # Also remove 'x' which marks stop codons or truncations
        cleaning_exprs.append(
            pl.col("junction_aa")
            .str.replace_all(r"[A-Z]", "")  # Remove uppercase (framework)
            .str.replace_all("x", "")        # Remove lowercase x (stop/truncation)
            .str.to_uppercase()              # Convert to uppercase
            .str.replace_all(r"[^ACDEFGHIKLMNPQRSTVWY*]", "")  # Keep only valid amino acids
            .fill_null("")
            .alias("junction_aa")
        )

    if "junction" in data.columns:
        # BGI format: lowercase = CDR3, uppercase = framework
        # Extract only lowercase nucleotides (the actual CDR3), then uppercase them
        cleaning_exprs.append(
            pl.col("junction")
            .str.replace_all(r"[A-Z]", "")  # Remove uppercase (framework)
            .str.to_uppercase()              # Convert to uppercase
            .str.replace_all(r"[^ATCGN]", "")  # Keep only valid nucleotides
            .fill_null("")
            .alias("junction")
        )

    # Clean other sequence fields
    sequence_fields = {
        "sequence": False, "sequence_aa": True,
        "cdr1": False, "cdr1_aa": True,
        "cdr2": False, "cdr2_aa": True,
        "cdr3": False, "cdr3_aa": True,
        "fwr1": False, "fwr1_aa": True,
        "fwr2": False, "fwr2_aa": True,
        "fwr3": False, "fwr3_aa": True,
        "fwr4": False, "fwr4_aa": True,
    }

    for field, is_aa in sequence_fields.items():
        if field in data.columns:
            if is_aa:
                cleaning_exprs.append(
                    pl.col(field)
                    .str.to_uppercase()
                    .str.replace_all(r"[^ACDEFGHIKLMNPQRSTVWY*]", "")
                    .fill_null("")
                    .alias(field)
                )
            else:
                cleaning_exprs.append(
                    pl.col(field)
                    .str.to_uppercase()
                    .str.replace_all(r"[^ATCGN]", "")
                    .fill_null("")
                    .alias(field)
                )

    if cleaning_exprs:
        data = data.with_columns(cleaning_exprs)

    return data


def clean_gene_calls_polars(data: pl.DataFrame) -> pl.DataFrame:
    """
    Polars-native gene call cleaning (optimized).

    Args:
        data: Polars DataFrame with gene call columns

    Returns:
        DataFrame with cleaned gene calls
    """
    gene_columns = ["v_call", "d_call", "d2_call", "j_call", "c_call"]
    cleaning_exprs = []

    for col in gene_columns:
        if col in data.columns:
            # Chain operations: split by comma, take first, remove parens, strip
            cleaning_exprs.append(
                pl.col(col)
                .str.split(",").list.first()
                .str.replace_all(r"\([^)]*\)", "")
                .str.strip_chars()
                .fill_null("")
                .alias(col)
            )

    if cleaning_exprs:
        data = data.with_columns(cleaning_exprs)

    return data


def compute_derived_fields_polars(data: pl.DataFrame, platform: str) -> pl.DataFrame:
    """
    Polars-native computation of derived AIRR fields (optimized).

    Args:
        data: Polars DataFrame to enhance
        platform: Platform type for platform-specific logic

    Returns:
        DataFrame with computed fields
    """
    computed_exprs = []

    # Platform-specific transformations
    if platform == "bgi":
        # BGI uses percentages for frequency, convert to fractions (0-1)
        if "duplicate_frequency" in data.columns:
            # Cast to float first (data is read as strings), then check if percentages
            try:
                freq_col = pl.col("duplicate_frequency").cast(pl.Float64, strict=False)
                max_freq = data.select(freq_col.max()).item()
                if max_freq and max_freq > 1.0:
                    data = data.with_columns(
                        (freq_col / 100.0).alias("duplicate_frequency")
                    )
                else:
                    # Just cast to float
                    data = data.with_columns(freq_col.alias("duplicate_frequency"))
            except Exception:
                # If conversion fails, keep as is
                pass

    # Compute junction lengths
    if "junction" in data.columns and "junction_length" not in data.columns:
        computed_exprs.append(pl.col("junction").str.len_bytes().alias("junction_length"))

    if "junction_aa" in data.columns and "junction_aa_length" not in data.columns:
        computed_exprs.append(pl.col("junction_aa").str.len_bytes().alias("junction_aa_length"))

    # Compute CDR3 from junction
    if "junction" in data.columns and "cdr3" not in data.columns:
        computed_exprs.append(
            pl.when(pl.col("junction").str.len_bytes() > 6)
            .then(pl.col("junction").str.slice(3, pl.col("junction").str.len_bytes() - 6))
            .otherwise(pl.lit(""))
            .alias("cdr3")
        )

    if "junction_aa" in data.columns and "cdr3_aa" not in data.columns:
        computed_exprs.append(
            pl.when(pl.col("junction_aa").str.len_bytes() > 2)
            .then(pl.col("junction_aa").str.slice(1, pl.col("junction_aa").str.len_bytes() - 2))
            .otherwise(pl.lit(""))
            .alias("cdr3_aa")
        )

    # Compute stop_codon
    if "stop_codon" not in data.columns:
        if "junction_aa" in data.columns:
            computed_exprs.append(
                pl.col("junction_aa").str.contains(r"\*").fill_null(False).alias("stop_codon")
            )
        else:
            computed_exprs.append(pl.lit(False).alias("stop_codon"))

    # Compute or convert productive column
    if "productive" not in data.columns:
        # Compute from stop_codon if missing
        if "stop_codon" in data.columns or "stop_codon" in [e.meta.output_name() for e in computed_exprs]:
            computed_exprs.append(pl.col("stop_codon").not_().alias("productive"))
        else:
            computed_exprs.append(pl.lit(True).alias("productive"))
    else:
        # Convert existing productive column to boolean if it's a string
        # Handle various formats: "in-frame", "out-of-frame", "In", "Out", "Stop", etc.
        if data["productive"].dtype == pl.Utf8:
            computed_exprs.append(
                pl.when(pl.col("productive").str.to_lowercase().str.starts_with("in"))
                .then(pl.lit(True))
                .when(pl.col("productive").str.to_lowercase().str.starts_with("out"))
                .then(pl.lit(False))
                .when(pl.col("productive").str.to_lowercase().str.contains("stop"))
                .then(pl.lit(False))
                .when(pl.col("productive").is_in(["true", "True", "yes", "Yes", "1"]))
                .then(pl.lit(True))
                .when(pl.col("productive").is_in(["false", "False", "no", "No", "0"]))
                .then(pl.lit(False))
                .otherwise(pl.lit(True))  # Default to True for unknown values
                .alias("productive")
            )

    # Compute duplicate_frequency
    if "duplicate_count" in data.columns and "duplicate_frequency" not in data.columns:
        if "repertoire_id" in data.columns:
            computed_exprs.append(
                (pl.col("duplicate_count") / pl.col("duplicate_count").sum().over("repertoire_id"))
                .alias("duplicate_frequency")
            )
        else:
            computed_exprs.append(
                (pl.col("duplicate_count") / pl.col("duplicate_count").sum())
                .alias("duplicate_frequency")
            )

    if computed_exprs:
        data = data.with_columns(computed_exprs)

    return data


def clean_and_validate_sequences(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enhanced sequence cleaning and validation.

    Args:
        df: DataFrame with sequence columns

    Returns:
        DataFrame with cleaned sequences
    """
    # Validate and clean junction_aa sequences
    if "junction_aa" in df.columns:
        df["junction_aa"] = df["junction_aa"].apply(validate_aa_sequence_enhanced)

    # Validate and clean junction sequences
    if "junction" in df.columns:
        df["junction"] = df["junction"].apply(validate_nt_sequence_enhanced)

    # Clean other sequence fields
    sequence_fields = ["sequence", "sequence_aa", "cdr1", "cdr1_aa", "cdr2", "cdr2_aa",
                      "cdr3", "cdr3_aa", "fwr1", "fwr1_aa", "fwr2", "fwr2_aa",
                      "fwr3", "fwr3_aa", "fwr4", "fwr4_aa"]

    for field in sequence_fields:
        if field in df.columns:
            if field.endswith("_aa"):
                df[field] = df[field].apply(validate_aa_sequence_enhanced)
            else:
                df[field] = df[field].apply(validate_nt_sequence_enhanced)

    return df


def validate_aa_sequence_enhanced(seq: Any) -> str:
    """
    Enhanced amino acid sequence validation.

    Args:
        seq: Sequence to validate

    Returns:
        Cleaned sequence or empty string if invalid
    """
    if pd.isna(seq) or seq == "" or seq is None:
        return ""

    seq = str(seq).upper().strip()

    # Remove common contaminants and formatting
    seq = re.sub(r"[^ACDEFGHIKLMNPQRSTVWY*X]", "", seq)

    # Handle special cases
    seq = seq.replace("X", "")  # Remove unknown amino acids

    return seq


def validate_nt_sequence_enhanced(seq: Any) -> str:
    """
    Enhanced nucleotide sequence validation.

    Args:
        seq: Sequence to validate

    Returns:
        Cleaned sequence or empty string if invalid
    """
    if pd.isna(seq) or seq == "" or seq is None:
        return ""

    seq = str(seq).upper().strip()

    # Remove non-nucleotide characters
    seq = re.sub(r"[^ATCGN]", "", seq)

    return seq


def clean_gene_calls_enhanced(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enhanced gene call cleaning and standardization.

    Args:
        df: DataFrame with gene call columns

    Returns:
        DataFrame with cleaned gene calls
    """
    gene_columns = ["v_call", "d_call", "d2_call", "j_call", "c_call"]

    for col in gene_columns:
        if col in df.columns:
            df[col] = df[col].apply(clean_single_gene_call_enhanced)

    return df


def clean_single_gene_call_enhanced(gene_call: Any) -> str:
    """
    Enhanced single gene call cleaning.

    Args:
        gene_call: Gene call string or value

    Returns:
        Cleaned gene call string
    """
    if pd.isna(gene_call) or gene_call == "" or gene_call is None:
        return ""

    gene_call = str(gene_call).strip()

    # Handle multiple gene calls (take the first one)
    if "," in gene_call:
        gene_call = gene_call.split(",")[0]
    if ";" in gene_call:
        gene_call = gene_call.split(";")[0]
    if "|" in gene_call:
        gene_call = gene_call.split("|")[0]

    # Remove score information in parentheses
    gene_call = re.sub(r"\([^)]*\)", "", gene_call)

    # Remove common prefixes
    gene_call = re.sub(r"^(TCRBV|TCRBD|TCRBJ|TRAV|TRAJ|IGHV|IGHD|IGHJ|IGH|TRB|TRA)", "", gene_call)

    # Standardize format
    gene_call = gene_call.replace("TCR", "TR")

    return gene_call.strip()


def compute_derived_fields(df: pd.DataFrame, platform: str) -> pd.DataFrame:
    """
    Compute derived AIRR fields from available data.

    Args:
        df: DataFrame to enhance
        platform: Platform type for platform-specific logic

    Returns:
        DataFrame with computed fields
    """
    # Compute junction lengths
    if "junction" in df.columns and "junction_length" not in df.columns:
        df["junction_length"] = df["junction"].str.len()

    if "junction_aa" in df.columns and "junction_aa_length" not in df.columns:
        df["junction_aa_length"] = df["junction_aa"].str.len()

    # Compute CDR3 from junction (IMGT definition)
    if "junction" in df.columns and "cdr3" not in df.columns:
        df["cdr3"] = df["junction"].apply(
            lambda x: x[3:-3] if isinstance(x, str) and len(x) > 6 else ""
        )

    if "junction_aa" in df.columns and "cdr3_aa" not in df.columns:
        df["cdr3_aa"] = df["junction_aa"].apply(
            lambda x: x[1:-1] if isinstance(x, str) and len(x) > 2 else ""
        )

    # Compute productivity
    if "productive" not in df.columns:
        df["productive"] = True  # Default to productive

        # Check for stop codons
        if "stop_codon" in df.columns:
            df["productive"] = ~df["stop_codon"]
        elif "junction_aa" in df.columns:
            df["productive"] = ~df["junction_aa"].str.contains("*", na=False)
    else:
        # Convert text values to boolean if productive column contains strings
        if df["productive"].dtype == 'object':
            # Handle ImmunoSEQ sequenceStatus values
            mapping = {
                "In": True,        # In-frame
                "Out": False,      # Out-of-frame
                "Stop": False,     # Stop codon
                "VDJ": True,       # Successful VDJ recombination (cloneResolved)
                "DJ": True,        # DJ recombination (for some datasets)
                "V": False,        # Incomplete V-only
                "D": False,        # Incomplete D-only
                "J": False,        # Incomplete J-only
                # Handle BGI function values
                "productive": True,
                "unproductive": False,
                "yes": True,
                "no": False,
                "true": True,
                "false": False,
                "1": True,
                "0": False
            }
            # Apply mapping and handle missing values without triggering warning
            mapped_values = df["productive"].map(mapping)
            df["productive"] = mapped_values.where(mapped_values.notna(), True).astype(bool)

    # Compute stop_codon if missing
    if "stop_codon" not in df.columns:
        if "junction_aa" in df.columns:
            df["stop_codon"] = df["junction_aa"].str.contains("*", na=False)
        else:
            df["stop_codon"] = False

    # Compute reading frame
    if "reading_frame" not in df.columns:
        if "productive" in df.columns:
            df["reading_frame"] = df["productive"].apply(
                lambda x: "in-frame" if x else "out-of-frame"
            )
        else:
            df["reading_frame"] = "in-frame"

    # Compute gene families
    for gene_type in ["v", "d", "j"]:
        family_col = f"{gene_type}_family"
        call_col = f"{gene_type}_call"

        if call_col in df.columns and family_col not in df.columns:
            df[family_col] = df[call_col].apply(extract_gene_family)

    # Compute duplicate frequency if missing
    if "duplicate_count" in df.columns and "duplicate_frequency" not in df.columns:
        if "repertoire_id" in df.columns:
            # Compute frequency within each repertoire
            df["duplicate_frequency"] = df.groupby("repertoire_id")["duplicate_count"].transform(
                lambda x: x / x.sum() if x.sum() > 0 else 0
            )
        else:
            total_count = df["duplicate_count"].sum()
            df["duplicate_frequency"] = df["duplicate_count"] / total_count if total_count > 0 else 0

    # Platform-specific computations
    if platform == "tenx":
        # For 10X data, set appropriate defaults
        if "is_cell" not in df.columns:
            df["is_cell"] = True
        if "high_confidence" not in df.columns:
            df["high_confidence"] = True

    return df


def extract_gene_family(gene_call: str) -> str:
    """
    Extract gene family from gene call.

    Args:
        gene_call: Gene call string

    Returns:
        Gene family designation
    """
    if pd.isna(gene_call) or gene_call == "":
        return ""

    # Extract family pattern (e.g., TRBV12 from TRBV12-1*01)
    match = re.search(r"([A-Z]+\d+)", str(gene_call))
    if match:
        return match.group(1)

    return ""


def validate_airr_schema_enhanced(
    data: Union[pd.DataFrame, pl.DataFrame]
) -> Dict[str, Any]:
    """
    Enhanced AIRR schema validation with detailed reporting.

    Args:
        data: DataFrame to validate

    Returns:
        Comprehensive validation report
    """
    # Use base validation and enhance
    report = validate_airr_compliance(data)

    # Add platform-specific validation
    columns = data.columns if isinstance(data, pd.DataFrame) else data.columns
    detected_platform = detect_platform(list(columns))

    report["detected_platform"] = detected_platform
    report["platform_confidence"] = _calculate_platform_confidence(list(columns), detected_platform)

    # Add sequence quality metrics
    if isinstance(data, pl.DataFrame):
        df = data.to_pandas()
    else:
        df = data

    sequence_metrics = {}

    if "junction_aa" in df.columns:
        valid_aa = df["junction_aa"].apply(lambda x: bool(re.match(r"^[ACDEFGHIKLMNPQRSTVWY*]*$", str(x))))
        sequence_metrics["valid_junction_aa_sequences"] = valid_aa.sum()
        sequence_metrics["invalid_junction_aa_sequences"] = (~valid_aa).sum()

    if "junction" in df.columns:
        valid_nt = df["junction"].apply(lambda x: bool(re.match(r"^[ATCGN]*$", str(x))))
        sequence_metrics["valid_junction_sequences"] = valid_nt.sum()
        sequence_metrics["invalid_junction_sequences"] = (~valid_nt).sum()

    report["sequence_quality"] = sequence_metrics

    return report


def _calculate_platform_confidence(columns: List[str], platform: str) -> float:
    """Calculate confidence score for platform detection."""
    if platform == "generic":
        return 0.0

    # Get expected mappings for the platform
    if platform in ENHANCED_COLUMN_MAPPINGS:
        expected_fields = set(ENHANCED_COLUMN_MAPPINGS[platform].keys())
        found_fields = set(col.lower() for col in columns)
        overlap = len(expected_fields & found_fields)
        confidence = overlap / len(expected_fields)
        return min(confidence, 1.0)

    return 0.0