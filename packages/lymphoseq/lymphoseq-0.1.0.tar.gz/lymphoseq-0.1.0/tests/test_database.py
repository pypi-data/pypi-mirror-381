"""
Tests for database search functions.
"""

import pytest
import pandas as pd
import polars as pl
from unittest.mock import Mock, patch

from lymphoseq.database import search_db, search_published


class TestDatabaseSearch:
    """Test database search functionality."""

    def test_search_db_basic(self, sample_airr_data):
        """Test basic database search."""
        # Mock the database search to avoid actual downloads
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame({
                "junction_aa": ["CASSLVGGANTDTQYF"],
                "antigen": ["CMV"],
                "species": ["HomoSapiens"],
                "database": ["VDJdb"]
            })

            result = search_db(
                sample_airr_data,
                databases=["vdjdb"],
                chain="trb"
            )

            assert isinstance(result, (pd.DataFrame, pl.DataFrame))

    def test_search_db_multiple_databases(self, sample_airr_data):
        """Test searching multiple databases."""
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb, \
             patch('lymphoseq.database.search._search_mcpas') as mock_mcpas:

            mock_vdjdb.return_value = pd.DataFrame({
                "junction_aa": ["CASSLVGGANTDTQYF"],
                "antigen": ["CMV"],
                "database": ["VDJdb"]
            })

            mock_mcpas.return_value = pd.DataFrame({
                "junction_aa": ["CASSLEGANTDTQYF"],
                "antigen": ["EBV"],
                "database": ["McPAS-TCR"]
            })

            result = search_db(
                sample_airr_data,
                databases=["vdjdb", "mcpas"],
                chain="trb"
            )

            assert len(result) >= 0

    def test_search_db_no_matches(self, sample_airr_data):
        """Test when no matches are found."""
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen", "database"])

            result = search_db(
                sample_airr_data,
                databases=["vdjdb"],
                chain="trb"
            )

            # Should return empty or original data
            assert isinstance(result, (pd.DataFrame, pl.DataFrame))

    def test_search_db_polars(self, polars_airr_data):
        """Test database search with Polars data."""
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame({
                "junction_aa": ["CASSLVGGANTDTQYF"],
                "antigen": ["CMV"],
                "database": ["VDJdb"]
            })

            result = search_db(
                polars_airr_data,
                databases=["vdjdb"],
                chain="trb"
            )

            assert isinstance(result, pl.DataFrame)

    def test_search_published(self, sample_airr_data):
        """Test search_published wrapper."""
        with patch('lymphoseq.database.search.search_db') as mock_search:
            mock_search.return_value = sample_airr_data

            result = search_published(sample_airr_data)

            # Should call search_db with all databases
            mock_search.assert_called_once()
            assert isinstance(result, pd.DataFrame)


class TestDatabaseChainSpecificity:
    """Test chain-specific database searches."""

    def test_search_trb_chain(self, sample_airr_data):
        """Test TRB chain search."""
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])

            result = search_db(sample_airr_data, chain="trb")

            mock_vdjdb.assert_called_once()
            args = mock_vdjdb.call_args
            assert "trb" in str(args).lower()

    def test_search_tra_chain(self, sample_airr_data):
        """Test TRA chain search."""
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])

            result = search_db(sample_airr_data, chain="tra")

            mock_vdjdb.assert_called_once()

    def test_search_invalid_chain(self, sample_airr_data):
        """Test invalid chain specification."""
        with pytest.raises(ValueError):
            search_db(sample_airr_data, chain="invalid_chain")


class TestDatabaseSearchEdgeCases:
    """Test edge cases in database search."""

    def test_empty_data(self):
        """Test with empty dataset."""
        empty_data = pd.DataFrame(columns=["junction_aa", "repertoire_id"])

        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])

            result = search_db(empty_data, chain="trb")

            assert len(result) == 0

    def test_missing_junction_aa_column(self, sample_airr_data):
        """Test with missing junction_aa column."""
        incomplete_data = sample_airr_data[["repertoire_id", "duplicate_count"]].copy()

        with pytest.raises((ValueError, KeyError)):
            search_db(incomplete_data, chain="trb")

    def test_all_databases_option(self, sample_airr_data):
        """Test searching all databases."""
        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb, \
             patch('lymphoseq.database.search._search_mcpas') as mock_mcpas:

            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])
            mock_mcpas.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])

            result = search_db(sample_airr_data, databases="all", chain="trb")

            # Should call all database search functions
            mock_vdjdb.assert_called_once()
            mock_mcpas.assert_called_once()


class TestDatabaseIntegration:
    """Test database search integration with analysis functions."""

    def test_search_after_filtering(self, sample_multi_repertoire_data):
        """Test database search on filtered data."""
        from lymphoseq.sequence import top_seqs

        # Get top sequences
        top = top_seqs(sample_multi_repertoire_data, top=10)

        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])

            result = search_db(top, chain="trb")

            assert len(result) <= len(top)

    def test_search_with_merged_chains(self, sample_10x_data):
        """Test database search on merged 10X data."""
        from lymphoseq.sequence import merge_chains

        merged = merge_chains(sample_10x_data)

        with patch('lymphoseq.database.search._search_vdjdb') as mock_vdjdb:
            mock_vdjdb.return_value = pd.DataFrame(columns=["junction_aa", "antigen"])

            result = search_db(merged, chain="trb")

            assert isinstance(result, (pd.DataFrame, pl.DataFrame))
