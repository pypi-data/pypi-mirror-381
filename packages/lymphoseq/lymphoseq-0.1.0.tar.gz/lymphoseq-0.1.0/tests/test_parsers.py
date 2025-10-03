"""
Tests for parser modules.
"""

import pytest
import pandas as pd
import polars as pl
from pathlib import Path
import tempfile
import os

from lymphoseq.parsers import read_immunoseq, read_10x, read_mixcr
from lymphoseq.parsers.utils import standardize_airr_data, detect_platform
from lymphoseq.parsers.base_parser import ParserConfig


class TestParserUtils:
    """Test utility functions."""

    def test_detect_platform(self):
        """Test platform detection from column names."""
        immunoseq_cols = ["aminoAcid", "nucleotide", "count (templates/reads)"]
        assert detect_platform(immunoseq_cols) == "immunoseq"

        tenx_cols = ["barcode", "cdr3", "v_gene"]
        assert detect_platform(tenx_cols) == "tenx"

        mixcr_cols = ["aaSeqCDR3", "nSeqCDR3", "cloneCount"]
        assert detect_platform(mixcr_cols) == "mixcr"

    def test_standardize_airr_data(self):
        """Test AIRR data standardization."""
        # Create test data
        test_data = pd.DataFrame({
            "aminoAcid": ["CASSLVGGANTDTQYF", "CASSLEGANTDTQYF"],
            "count (templates/reads)": [100, 50],
            "vGeneName": ["TRBV2*01", "TRBV3*01"],
            "sequenceStatus": ["In", "In"]
        })

        standardized = standardize_airr_data(test_data, platform="immunoseq")

        assert "junction_aa" in standardized.columns
        assert "duplicate_count" in standardized.columns
        assert "v_call" in standardized.columns
        assert "productive" in standardized.columns

    def test_parser_config(self):
        """Test parser configuration."""
        config = ParserConfig(parallel=False, threads=2)
        assert config.parallel is False
        assert config.threads == 2
        assert config.return_type == "polars"


class TestImmunoSeqParser:
    """Test ImmunoSEQ parser."""

    def create_test_immunoseq_file(self, tmpdir):
        """Create a test ImmunoSEQ file."""
        test_data = [
            "nucleotide\taminoAcid\tcount (templates/reads)\tvGeneName\tjGeneName\tsequenceStatus",
            "TGTGCCAGCAGTTTGGTGGGGCTAACACTGATACGCAGTATTTT\tCASSLVGGANTDTQYF\t100\tTRBV2*01\tTRBJ2-3*01\tIn",
            "TGTGCCAGCAGTTTGGAGGGGGCTAACACTGATACGCAGTATTTT\tCASSLEGANTDTQYF\t50\tTRBV3*01\tTRBJ2-3*01\tIn"
        ]

        file_path = tmpdir / "test_sample.tsv"
        with open(file_path, 'w') as f:
            f.write('\n'.join(test_data))

        return file_path

    def test_read_immunoseq_single_file(self, tmp_path):
        """Test reading a single ImmunoSEQ file."""
        test_file = self.create_test_immunoseq_file(tmp_path)

        data = read_immunoseq(test_file, return_type="pandas")

        assert isinstance(data, pd.DataFrame)
        assert len(data) == 2
        assert "junction_aa" in data.columns
        assert "duplicate_count" in data.columns
        assert "repertoire_id" in data.columns

    def test_read_immunoseq_polars(self, tmp_path):
        """Test reading with Polars backend."""
        test_file = self.create_test_immunoseq_file(tmp_path)

        data = read_immunoseq(test_file, return_type="polars")

        assert isinstance(data, pl.DataFrame)
        assert len(data) == 2
        assert "junction_aa" in data.columns


class TestTenXParser:
    """Test 10X parser."""

    def create_test_10x_file(self, tmpdir):
        """Create a test 10X file."""
        test_data = [
            "barcode\tcdr3\tv_gene\tj_gene\tchain\tproductive",
            "AAACCTGAGCAATCTC-1\tCASSLVGGANTDTQYF\tTRBV2\tTRBJ2-3\tTRB\tTrue",
            "AAACCTGAGCAATCTC-1\tCAVRDSSYKLIF\tTRAV8-1\tTRAJ53\tTRA\tTrue",
            "AAACCTGAGTAGGCTG-1\tCASSLEGANTDTQYF\tTRBV3\tTRBJ2-3\tTRB\tTrue"
        ]

        file_path = tmpdir / "filtered_contig_annotations.csv"
        with open(file_path, 'w') as f:
            f.write('\n'.join(test_data))

        return file_path

    def test_read_10x(self, tmp_path):
        """Test reading 10X data."""
        test_file = self.create_test_10x_file(tmp_path)

        data = read_10x(test_file, return_type="pandas")

        assert isinstance(data, pd.DataFrame)
        assert len(data) > 0
        assert "repertoire_id" in data.columns


class TestErrorHandling:
    """Test error handling in parsers."""

    def test_invalid_file_path(self):
        """Test handling of invalid file paths."""
        with pytest.raises(ValueError):
            read_immunoseq("nonexistent_file.tsv")

    def test_empty_file(self, tmp_path):
        """Test handling of empty files."""
        empty_file = tmp_path / "empty.tsv"
        empty_file.touch()

        # Should handle empty files gracefully
        with pytest.raises(ValueError):
            read_immunoseq(empty_file)

    def test_malformed_file(self, tmp_path):
        """Test handling of malformed files."""
        malformed_file = tmp_path / "malformed.tsv"
        with open(malformed_file, 'w') as f:
            f.write("this is not a valid tsv file")

        # Should handle malformed files gracefully
        with pytest.raises(ValueError):
            read_immunoseq(malformed_file)