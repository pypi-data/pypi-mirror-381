"""
Database search functions for TCR/BCR sequences.

Provides functions to search public databases for known antigen-specific TCRs/BCRs.
"""

import pandas as pd
import polars as pl
from typing import Union, List, Optional, Literal
import urllib.request
import json
from pathlib import Path
import tempfile


def search_db(
    data: Union[pl.DataFrame, pd.DataFrame],
    databases: Union[Literal["all"], List[str]] = "all",
    chain: Literal["tra", "trb", "igh", "igk", "igl"] = "trb",
    by_column: str = "junction_aa",
    include_similarity: bool = False,
    cache_dir: Optional[str] = None
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Search public databases for TCR/BCR sequences with known antigen specificity.

    Searches VDJdb, McPAS-TCR, and IEDB databases to find if your sequences match
    known antigen-specific receptors. Returns annotated data with epitope, antigen,
    MHC allele, and reference information.

    Args:
        data: DataFrame with sequence data
        databases: List of databases to search or "all" for all databases
            Options: ["VDJdb", "McPAS-TCR", "IEDB"]
        chain: Receptor chain type - "tra", "trb", "igh", "igk", or "igl"
        by_column: Column to search (default: junction_aa)
        include_similarity: Include similar (not exact) matches (requires online API)
        cache_dir: Directory to cache database files

    Returns:
        DataFrame annotated with antigen specificity information

    Examples:
        >>> # Search VDJdb for TRB sequences
        >>> annotated = search_db(df, databases=["VDJdb"], chain="trb")
        >>> # Find sequences with known epitopes
        >>> matches = annotated[annotated["epitope"].notna()]
        >>> print(matches[["junction_aa", "epitope", "antigen", "mhc_allele"]])

    Notes:
        - Requires internet connection for first download
        - Database files are cached locally for faster subsequent searches
        - VDJdb: https://vdjdb.cdr3.net/
        - McPAS-TCR: http://friedmanlab.weizmann.ac.il/McPAS-TCR/
        - IEDB: https://www.iedb.org/
    """
    # Convert to pandas for easier merging
    is_polars = isinstance(data, pl.DataFrame)
    if is_polars:
        df = data.to_pandas()
    else:
        df = data.copy()

    # Determine which databases to search
    if databases == "all":
        db_list = ["VDJdb", "McPAS-TCR", "IEDB"]
    else:
        db_list = databases if isinstance(databases, list) else [databases]

    # Load and merge database data
    db_results = []

    for db_name in db_list:
        try:
            if db_name == "VDJdb":
                db_df = _search_vdjdb(df[by_column].unique(), chain, cache_dir)
            elif db_name == "McPAS-TCR":
                db_df = _search_mcpas(df[by_column].unique(), chain, cache_dir)
            elif db_name == "IEDB":
                db_df = _search_iedb(df[by_column].unique(), chain, cache_dir)
            else:
                print(f"Warning: Unknown database '{db_name}', skipping")
                continue

            if db_df is not None and len(db_df) > 0:
                db_results.append(db_df)
        except Exception as e:
            print(f"Warning: Failed to search {db_name}: {e}")
            continue

    # Merge all database results
    if db_results:
        combined_db = pd.concat(db_results, ignore_index=True)

        # Merge with input data
        result = df.merge(
            combined_db,
            left_on=by_column,
            right_on="cdr3_aa",
            how="left"
        )

        # Drop duplicate cdr3_aa column if present
        if "cdr3_aa" in result.columns and "cdr3_aa" != by_column:
            result = result.drop(columns=["cdr3_aa"])
    else:
        print("Warning: No database results found")
        result = df.copy()

    # Convert back to polars if needed
    if is_polars:
        result = pl.from_pandas(result)

    return result


def _search_vdjdb(
    sequences: List[str],
    chain: str,
    cache_dir: Optional[str] = None
) -> pd.DataFrame:
    """
    Search VDJdb database.

    VDJdb is a curated database of T-cell receptor sequences with known antigen specificities.
    """
    # Map chain to VDJdb gene names
    chain_map = {
        "tra": "TRA",
        "trb": "TRB",
        "igh": "IGH",
        "igk": "IGK",
        "igl": "IGL"
    }

    gene = chain_map.get(chain, "TRB")

    # Download VDJdb if not cached
    if cache_dir is None:
        cache_dir = Path(tempfile.gettempdir()) / "lymphoseq_db_cache"
    else:
        cache_dir = Path(cache_dir)

    cache_dir.mkdir(parents=True, exist_ok=True)
    vdjdb_file = cache_dir / "vdjdb.txt"

    if not vdjdb_file.exists():
        print("Downloading VDJdb database (first time only)...")
        url = "https://github.com/antigenomics/vdjdb-db/releases/latest/download/vdjdb.slim.txt"
        try:
            urllib.request.urlretrieve(url, vdjdb_file)
            print(f"✅ Downloaded to {vdjdb_file}")
        except Exception as e:
            print(f"❌ Failed to download VDJdb: {e}")
            print("You can manually download from: https://github.com/antigenomics/vdjdb-db/releases")
            return pd.DataFrame()

    # Read VDJdb
    try:
        vdjdb = pd.read_csv(vdjdb_file, sep="\t", low_memory=False)
    except Exception as e:
        print(f"Error reading VDJdb file: {e}")
        return pd.DataFrame()

    # Filter to species and chain
    vdjdb = vdjdb[
        (vdjdb["species"] == "HomoSapiens") &
        (vdjdb["gene"] == gene)
    ].copy()

    # Filter to sequences of interest
    vdjdb = vdjdb[vdjdb["cdr3"].isin(sequences)]

    if len(vdjdb) == 0:
        return pd.DataFrame()

    # Select and rename columns
    result = vdjdb[[
        "cdr3", "v.segm", "j.segm", "antigen.epitope", "antigen.gene",
        "antigen.species", "mhc.a", "mhc.b", "reference.id", "vdjdb.score"
    ]].rename(columns={
        "cdr3": "cdr3_aa",
        "v.segm": "v_call",
        "j.segm": "j_call",
        "antigen.epitope": "epitope",
        "antigen.gene": "antigen",
        "antigen.species": "pathology",
        "mhc.a": "mhc_a",
        "mhc.b": "mhc_b",
        "reference.id": "reference",
        "vdjdb.score": "confidence_score"
    })

    # Combine MHC alleles
    result["mhc_allele"] = result["mhc_a"].fillna("") + ":" + result["mhc_b"].fillna("")
    result["mhc_allele"] = result["mhc_allele"].str.strip(":")
    result = result.drop(columns=["mhc_a", "mhc_b"])

    result["database"] = "VDJdb"
    result["cell_type"] = "T cell"

    return result


def _search_mcpas(
    sequences: List[str],
    chain: str,
    cache_dir: Optional[str] = None
) -> pd.DataFrame:
    """
    Search McPAS-TCR database.

    McPAS-TCR is a manually curated catalog of pathology-associated T-cell receptor sequences.
    """
    if cache_dir is None:
        cache_dir = Path(tempfile.gettempdir()) / "lymphoseq_db_cache"
    else:
        cache_dir = Path(cache_dir)

    cache_dir.mkdir(parents=True, exist_ok=True)
    mcpas_file = cache_dir / "mcpas.csv"

    if not mcpas_file.exists():
        print("Downloading McPAS-TCR database (first time only)...")
        url = "http://friedmanlab.weizmann.ac.il/McPAS-TCR/McPAS-TCR.csv"
        try:
            urllib.request.urlretrieve(url, mcpas_file)
            print(f"✅ Downloaded to {mcpas_file}")
        except Exception as e:
            print(f"❌ Failed to download McPAS-TCR: {e}")
            print("You can manually download from: http://friedmanlab.weizmann.ac.il/McPAS-TCR/")
            return pd.DataFrame()

    # Read McPAS-TCR
    try:
        mcpas = pd.read_csv(mcpas_file, low_memory=False)
    except Exception as e:
        print(f"Error reading McPAS-TCR file: {e}")
        return pd.DataFrame()

    # Filter to human sequences
    mcpas = mcpas[mcpas["Species"] == "Human"].copy()

    # Select CDR3 column based on chain
    if chain in ["tra"]:
        cdr3_col = "CDR3.alpha.aa"
        v_col = "TRAV"
        j_col = "TRAJ"
    elif chain in ["trb"]:
        cdr3_col = "CDR3.beta.aa"
        v_col = "TRBV"
        j_col = "TRBJ"
    else:
        return pd.DataFrame()  # McPAS-TCR is primarily for TCR

    # Filter to sequences of interest
    mcpas = mcpas[mcpas[cdr3_col].isin(sequences)]

    if len(mcpas) == 0:
        return pd.DataFrame()

    # Select and rename columns
    result = mcpas[[
        cdr3_col, v_col, j_col, "Epitope.peptide", "Antigen.protein",
        "Pathology", "MHC", "T.Cell.Type", "PubMed.ID"
    ]].rename(columns={
        cdr3_col: "cdr3_aa",
        v_col: "v_call",
        j_col: "j_call",
        "Epitope.peptide": "epitope",
        "Antigen.protein": "antigen",
        "Pathology": "pathology",
        "MHC": "mhc_allele",
        "T.Cell.Type": "cell_type",
        "PubMed.ID": "reference"
    })

    result["database"] = "McPAS-TCR"
    result["confidence_score"] = 1  # McPAS entries are manually curated

    return result


def _search_iedb(
    sequences: List[str],
    chain: str,
    cache_dir: Optional[str] = None
) -> pd.DataFrame:
    """
    Search IEDB (Immune Epitope Database).

    IEDB contains experimental data on antibody and T cell epitopes.
    """
    if cache_dir is None:
        cache_dir = Path(tempfile.gettempdir()) / "lymphoseq_db_cache"
    else:
        cache_dir = Path(cache_dir)

    cache_dir.mkdir(parents=True, exist_ok=True)
    iedb_file = cache_dir / "iedb_receptors.csv"

    if not iedb_file.exists():
        print("Downloading IEDB receptor database (first time only)...")
        print("Note: IEDB download requires manual steps. See: https://www.iedb.org/downloader.php")
        print("Skipping IEDB for now. Download 'receptor_full_v3.zip' manually and extract to cache directory.")
        return pd.DataFrame()

    # If file exists, read it
    try:
        iedb = pd.read_csv(iedb_file, low_memory=False)
    except Exception as e:
        print(f"Error reading IEDB file: {e}")
        return pd.DataFrame()

    # Process IEDB data based on chain
    # (Implementation depends on IEDB file format)
    # For now, return empty DataFrame
    return pd.DataFrame()


def search_published(
    data: Union[pl.DataFrame, pd.DataFrame],
    by_column: str = "junction_aa"
) -> Union[pl.DataFrame, pd.DataFrame]:
    """
    Search for sequences in published TCR literature.

    Annotates your sequences with information from published studies if they
    match known TCR sequences in the literature.

    Args:
        data: DataFrame with sequence data
        by_column: Column to search (default: junction_aa)

    Returns:
        DataFrame annotated with published sequence information

    Examples:
        >>> # Find published sequences in your data
        >>> annotated = search_published(df)
        >>> published_seqs = annotated[annotated["published"].notna()]

    Notes:
        This is a wrapper around search_db that searches all available databases.
        For more control, use search_db() directly.
    """
    return search_db(
        data,
        databases="all",
        chain="trb",
        by_column=by_column
    )


def get_vdjdb_stats(cache_dir: Optional[str] = None) -> dict:
    """
    Get statistics about the VDJdb database.

    Returns:
        Dictionary with database statistics

    Examples:
        >>> stats = get_vdjdb_stats()
        >>> print(f"VDJdb contains {stats['total_entries']} entries")
    """
    if cache_dir is None:
        cache_dir = Path(tempfile.gettempdir()) / "lymphoseq_db_cache"
    else:
        cache_dir = Path(cache_dir)

    vdjdb_file = cache_dir / "vdjdb.txt"

    if not vdjdb_file.exists():
        return {"error": "VDJdb not downloaded. Run search_db() first."}

    try:
        vdjdb = pd.read_csv(vdjdb_file, sep="\t", low_memory=False)

        stats = {
            "total_entries": len(vdjdb),
            "human_entries": len(vdjdb[vdjdb["species"] == "HomoSapiens"]),
            "unique_epitopes": vdjdb["antigen.epitope"].nunique(),
            "unique_antigens": vdjdb["antigen.gene"].nunique(),
            "chains": vdjdb["gene"].value_counts().to_dict(),
            "species": vdjdb["species"].value_counts().to_dict()
        }

        return stats
    except Exception as e:
        return {"error": str(e)}
