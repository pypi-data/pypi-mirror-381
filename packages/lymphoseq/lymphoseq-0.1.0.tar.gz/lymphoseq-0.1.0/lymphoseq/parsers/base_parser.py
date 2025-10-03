"""
Base parser class for AIRR-seq data formats.

Provides common functionality and interface for all parsers.
Enhanced with full AIRR schema compliance.
"""

import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union, List, Dict, Any, Optional
import pandas as pd
import polars as pl
from pydantic import BaseModel, Field

from .utils_enhanced import standardize_airr_data, validate_airr_schema_enhanced
from .airr_schema import get_essential_airr_fields


class ParserConfig(BaseModel):
    """Configuration for parser behavior."""

    parallel: bool = Field(default=True, description="Enable parallel processing")
    threads: Optional[int] = Field(default=None, description="Number of threads to use")
    chunk_size: Optional[int] = Field(default=None, description="Chunk size for processing")
    max_memory_gb: float = Field(default=8.0, description="Maximum memory to use in GB")
    streaming_mode: bool = Field(default=False, description="Enable streaming for large files")
    temp_dir: Optional[Union[str, Path]] = Field(default=None, description="Temporary directory for cache files")
    progress_detail: str = Field(default="basic", description="Progress reporting level")
    return_type: str = Field(default="polars", description="Return data type")
    use_arrow: Union[str, bool] = Field(default="auto", description="Apache Arrow usage")
    validate_airr: bool = Field(default=True, description="Validate AIRR compliance")
    enhanced_mappings: bool = Field(default=True, description="Use enhanced column mappings")
    verbose: bool = Field(default=False, description="Show detailed progress messages")


class BaseParser(ABC):
    """
    Abstract base class for all AIRR-seq data parsers.

    Provides common functionality including file discovery, validation,
    and standardization to AIRR format.
    """

    def __init__(self, config: Optional[ParserConfig] = None):
        """
        Initialize the parser with configuration.

        Args:
            config: Parser configuration options
        """
        self.config = config or ParserConfig()
        self.supported_extensions = [".tsv", ".txt", ".csv", ".tsv.gz", ".txt.gz"]
        self.platform = "generic"  # Override in subclasses

    def find_files(
        self,
        path: Union[str, Path, List[str]],
        recursive: bool = False
    ) -> List[Path]:
        """
        Find files to parse from given path(s).

        Args:
            path: Path to file(s) or directory
            recursive: Search recursively in subdirectories

        Returns:
            List of file paths to process
        """
        if isinstance(path, list):
            return [Path(p) for p in path if Path(p).exists()]

        path = Path(path)

        if path.is_file():
            return [path]

        if path.is_dir():
            pattern = "**/*" if recursive else "*"
            files = []
            for ext in self.supported_extensions:
                files.extend(path.glob(f"{pattern}{ext}"))
            return files

        raise ValueError(f"Path does not exist: {path}")

    def validate_files(self, file_paths: List[Path]) -> List[Path]:
        """
        Validate files exist and are not empty.

        Args:
            file_paths: List of file paths to validate

        Returns:
            List of valid file paths
        """
        valid_files = []
        for file_path in file_paths:
            if file_path.exists() and file_path.stat().st_size > 0:
                valid_files.append(file_path)

        if len(valid_files) != len(file_paths):
            print(f"Warning: {len(file_paths) - len(valid_files)} files were empty or missing")

        return valid_files

    def extract_repertoire_id(self, file_path: Path) -> str:
        """
        Extract repertoire ID from file path.

        Args:
            file_path: Path to the file

        Returns:
            Repertoire identifier
        """
        return file_path.stem.replace(".tsv", "").replace(".txt", "")

    def detect_delimiter(self, file_path: Path, sample_lines: int = 5) -> str:
        """
        Detect the delimiter used in a file.

        Args:
            file_path: Path to the file
            sample_lines: Number of lines to sample

        Returns:
            Detected delimiter
        """
        import csv
        import gzip

        # Handle gzip-compressed files
        if str(file_path).endswith('.gz'):
            with gzip.open(file_path, 'rt', encoding='utf-8') as f:
                sample = ''.join([f.readline() for _ in range(sample_lines)])
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                sample = ''.join([f.readline() for _ in range(sample_lines)])

        sniffer = csv.Sniffer()
        try:
            delimiter = sniffer.sniff(sample, delimiters='\t,;|').delimiter
            return delimiter
        except csv.Error:
            # Default to tab if detection fails
            return '\t'

    @abstractmethod
    def parse_file(self, file_path: Path) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Parse a single file into standardized format.

        Args:
            file_path: Path to the file to parse

        Returns:
            Parsed data in standardized format
        """
        pass

    @abstractmethod
    def standardize_columns(
        self,
        data: Union[pd.DataFrame, pl.DataFrame]
    ) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Standardize column names to AIRR format.

        Args:
            data: Raw data with original column names

        Returns:
            Data with standardized column names
        """
        pass

    def standardize_to_airr(
        self,
        data: Union[pd.DataFrame, pl.DataFrame],
        platform: str = "auto",
        repertoire_id: Optional[str] = None
    ) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Standardize data to full AIRR compliance.

        Args:
            data: Parsed data frame
            platform: Platform type for enhanced mappings
            repertoire_id: Repertoire identifier

        Returns:
            Fully AIRR-compliant data frame
        """
        return standardize_airr_data(
            data,
            platform=platform,
            repertoire_id=repertoire_id,
            use_enhanced_mappings=self.config.enhanced_mappings,
            verbose=self.config.verbose
        )

    def validate_airr_compliance(
        self,
        data: Union[pd.DataFrame, pl.DataFrame]
    ) -> Dict[str, Any]:
        """
        Validate data against AIRR schema.

        Args:
            data: Data frame to validate

        Returns:
            Validation report
        """
        if self.config.validate_airr:
            return validate_airr_schema_enhanced(data)
        else:
            return {"validation_skipped": True}

    def parse(
        self,
        path: Union[str, Path, List[str]],
        recursive: bool = False
    ) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Main parsing method that orchestrates the parsing process.

        Args:
            path: Path to file(s) or directory
            recursive: Search recursively in subdirectories

        Returns:
            Combined parsed data
        """
        # Find and validate files
        file_paths = self.find_files(path, recursive)
        valid_files = self.validate_files(file_paths)

        if not valid_files:
            raise ValueError("No valid files found to parse")

        # Parse files
        # Note: Streaming mode requires sequential processing
        if self.config.streaming_mode:
            if self.config.parallel and self.config.verbose:
                print("⚠️  Streaming mode requires sequential processing. Disabling parallel mode.")
            return self._parse_sequential(valid_files)
        elif self.config.parallel and len(valid_files) > 1:
            return self._parse_parallel(valid_files)
        else:
            return self._parse_sequential(valid_files)

    def _parse_sequential(self, file_paths: List[Path]) -> Union[pd.DataFrame, pl.DataFrame]:
        """Parse files sequentially with optional chunking."""
        # Use chunked processing for large file sets
        # In streaming mode, automatically enable chunking if not set
        chunk_size = self.config.chunk_size
        if self.config.streaming_mode and chunk_size is None and len(file_paths) > 5:
            # Use smaller chunks for very large files
            # Each chunk should fit in ~2-3GB RAM
            chunk_size = 3  # Conservative default for large gzipped files

        if chunk_size and len(file_paths) > chunk_size:
            # Store chunk_size temporarily for use in chunked processing
            original_chunk_size = self.config.chunk_size
            self.config.chunk_size = chunk_size
            result = self._parse_sequential_chunked(file_paths)
            self.config.chunk_size = original_chunk_size
            return result

        parsed_data = []
        total_records = 0

        # Add progress bar if tqdm is available
        try:
            from tqdm import tqdm
            progress_bar = tqdm(
                file_paths,
                desc="Processing files",
                unit="file",
                postfix={"records": 0}
            )
            has_tqdm = True
        except ImportError:
            progress_bar = file_paths
            has_tqdm = False
            if len(file_paths) > 1:
                print(f"Processing {len(file_paths)} files...")

        for file_path in progress_bar:
            try:
                data = self.parse_file(file_path)
                repertoire_id = self.extract_repertoire_id(file_path)
                data = self.standardize_to_airr(data, platform=self.platform, repertoire_id=repertoire_id)

                # Count records
                current_records = len(data)
                total_records += current_records

                # Update progress bar with record count
                if has_tqdm:
                    progress_bar.set_postfix({
                        "records": f"{total_records:,}",
                        "current": f"{current_records:,}"
                    })

                # Validate if requested
                if self.config.validate_airr:
                    validation_report = self.validate_airr_compliance(data)
                    if not validation_report.get("valid", True):
                        if has_tqdm:
                            progress_bar.write(f"AIRR validation warnings for {file_path.name}: {len(validation_report.get('warnings', []))} issues")
                        else:
                            print(f"AIRR validation warnings for {file_path}: {validation_report.get('warnings', [])}")

                parsed_data.append(data)
            except Exception as e:
                if has_tqdm:
                    progress_bar.write(f"Error parsing {file_path.name}: {e}")
                else:
                    print(f"Error parsing {file_path}: {e}")
                continue

        # Final summary
        if has_tqdm:
            progress_bar.close()
            print(f"✅ Completed: {len(parsed_data)} files processed, {total_records:,} total records standardized")
        elif len(file_paths) > 1:
            print(f"✅ Completed: {len(parsed_data)} files processed, {total_records:,} total records standardized")

        if not parsed_data:
            raise ValueError("No files were successfully parsed")

        # Combine data
        if self.config.return_type == "polars":
            # Use polars concat with how="diagonal" for mismatched columns
            # This is much more efficient than manual column alignment
            if len(parsed_data) > 1:
                try:
                    # Try diagonal concat first - handles column mismatches automatically
                    return pl.concat(parsed_data, how="diagonal")
                except Exception as e:
                    # Fallback: convert all to string type for consistent concatenation
                    print(f"Converting to strings for polars compatibility...")
                    cleaned_data = []
                    for df in parsed_data:
                        # Convert all columns to string, handling Null types specially
                        string_expressions = []
                        for col in df.columns:
                            col_dtype = df.schema[col]
                            if col_dtype == pl.Null:
                                # Convert Null columns to empty strings
                                string_expressions.append(pl.lit("").alias(col))
                            else:
                                # Convert other types to string
                                string_expressions.append(pl.col(col).cast(pl.Utf8).alias(col))

                        string_df = df.select(string_expressions)
                        cleaned_data.append(string_df)
                    return pl.concat(cleaned_data, how="diagonal")
            else:
                return parsed_data[0] if parsed_data else pl.DataFrame()
        else:
            return pd.concat(parsed_data, ignore_index=True, sort=False)

    def _parse_parallel(self, file_paths: List[Path]) -> Union[pd.DataFrame, pl.DataFrame]:
        """Parse files in parallel using concurrent.futures."""
        from concurrent.futures import ProcessPoolExecutor, as_completed

        parsed_data = []
        total_records = 0

        # Add progress bar for parallel processing
        try:
            from tqdm import tqdm
            progress_bar = tqdm(
                total=len(file_paths),
                desc="Processing files (parallel)",
                unit="file",
                postfix={"records": 0}
            )
            has_tqdm = True
        except ImportError:
            has_tqdm = False
            print(f"Processing {len(file_paths)} files in parallel...")

        with ProcessPoolExecutor(max_workers=self.config.threads) as executor:
            future_to_file = {
                executor.submit(self._parse_single_file, file_path): file_path
                for file_path in file_paths
            }

            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    data = future.result()
                    if data is not None:
                        current_records = len(data)
                        total_records += current_records
                        parsed_data.append(data)

                        # Update progress bar
                        if has_tqdm:
                            progress_bar.update(1)
                            progress_bar.set_postfix({
                                "records": f"{total_records:,}",
                                "current": f"{current_records:,}"
                            })
                except Exception as e:
                    error_msg = str(e)
                    if has_tqdm:
                        progress_bar.write(f"❌ Error parsing {file_path.name}: {error_msg}")
                        progress_bar.update(1)
                    else:
                        print(f"❌ Error parsing {file_path.name}: {error_msg}")

                    # Print full traceback for debugging if verbose
                    if self.config.verbose:
                        import traceback
                        traceback.print_exc()

        # Final summary
        if has_tqdm:
            progress_bar.close()
            print(f"✅ Completed: {len(parsed_data)} files processed, {total_records:,} total records standardized")
        else:
            print(f"✅ Completed: {len(parsed_data)} files processed, {total_records:,} total records standardized")

        if not parsed_data:
            raise ValueError("No files were successfully parsed")

        # Combine data
        if self.config.return_type == "polars":
            # Use polars concat with how="diagonal" for mismatched columns
            # This is much more efficient than manual column alignment
            if len(parsed_data) > 1:
                try:
                    # Try diagonal concat first - handles column mismatches automatically
                    return pl.concat(parsed_data, how="diagonal")
                except Exception as e:
                    # Fallback: convert all to string type for consistent concatenation
                    print(f"Converting to strings for polars compatibility...")
                    cleaned_data = []
                    for df in parsed_data:
                        # Convert all columns to string, handling Null types specially
                        string_expressions = []
                        for col in df.columns:
                            col_dtype = df.schema[col]
                            if col_dtype == pl.Null:
                                # Convert Null columns to empty strings
                                string_expressions.append(pl.lit("").alias(col))
                            else:
                                # Convert other types to string
                                string_expressions.append(pl.col(col).cast(pl.Utf8).alias(col))

                        string_df = df.select(string_expressions)
                        cleaned_data.append(string_df)
                    return pl.concat(cleaned_data, how="diagonal")
            else:
                return parsed_data[0] if parsed_data else pl.DataFrame()
        else:
            return pd.concat(parsed_data, ignore_index=True, sort=False)

    def _parse_single_file(self, file_path: Path) -> Union[pd.DataFrame, pl.DataFrame, None]:
        """Helper method for parallel parsing."""
        try:
            data = self.parse_file(file_path)
            repertoire_id = self.extract_repertoire_id(file_path)
            return self.standardize_to_airr(data, platform=self.platform, repertoire_id=repertoire_id)
        except Exception as e:
            # Re-raise exception to be caught by parallel executor
            raise Exception(f"Failed to parse {file_path.name}: {str(e)}")

    def _parse_sequential_chunked(self, file_paths: List[Path]) -> Union[pd.DataFrame, pl.DataFrame, pl.LazyFrame]:
        """
        Parse files in chunks to reduce memory usage.

        Processes files in batches, combining them before moving to the next batch.
        For streaming_mode=True, returns a LazyFrame to avoid loading into memory.
        """
        import tempfile
        import uuid
        try:
            from tqdm import tqdm
            has_tqdm = True
        except ImportError:
            has_tqdm = False

        # Determine temp directory
        if self.config.temp_dir:
            temp_dir = Path(self.config.temp_dir)
            temp_dir.mkdir(parents=True, exist_ok=True)
        else:
            temp_dir = Path(tempfile.gettempdir())

        # Create a unique session ID to avoid conflicts
        session_id = uuid.uuid4().hex[:8]

        if self.config.verbose:
            print(f"💾 Using temp directory: {temp_dir}")

        chunk_size = self.config.chunk_size or 10
        chunks = [file_paths[i:i + chunk_size] for i in range(0, len(file_paths), chunk_size)]

        if not has_tqdm or self.config.verbose:
            print(f"📦 Processing {len(file_paths)} files in {len(chunks)} chunks (size={chunk_size})")

        chunk_results = []

        # Use tqdm if available, otherwise simple print
        chunk_iterator = tqdm(enumerate(chunks, 1), total=len(chunks), desc="Processing chunks", unit="chunk") if has_tqdm else enumerate(chunks, 1)

        for chunk_idx, chunk in chunk_iterator:
            if not has_tqdm:
                print(f"   Chunk {chunk_idx}/{len(chunks)}: {len(chunk)} files...")

            # Parse this chunk
            chunk_data = []
            for file_path in chunk:
                try:
                    data = self.parse_file(file_path)
                    repertoire_id = self.extract_repertoire_id(file_path)
                    data = self.standardize_to_airr(data, platform=self.platform, repertoire_id=repertoire_id)
                    chunk_data.append(data)
                except Exception as e:
                    print(f"   Error parsing {file_path.name}: {e}")
                    continue

            # Combine chunk data
            if chunk_data:
                if self.config.return_type == "polars":
                    chunk_result = pl.concat(chunk_data, how="diagonal", rechunk=True)
                else:
                    chunk_result = pd.concat(chunk_data, ignore_index=True, sort=False)

                chunk_results.append(chunk_result)

                # Optionally save chunk to disk using Arrow IPC for memory management
                # In streaming mode, be more aggressive with caching to reduce memory usage
                should_cache = (
                    self.config.use_arrow == "always" or
                    (self.config.streaming_mode and len(chunk_results) > 1) or
                    (self.config.use_arrow == "auto" and len(chunk_results) > 3)
                )
                if should_cache:
                    cache_file = temp_dir / f"lymphoseq_cache_{session_id}_chunk_{chunk_idx}.arrow"
                    if self.config.return_type == "polars":
                        chunk_result.write_ipc(cache_file, compression="zstd")
                    else:
                        pl.from_pandas(chunk_result).write_ipc(cache_file, compression="zstd")
                    chunk_results[len(chunk_results) - 1] = cache_file  # Store path instead of data
                    if self.config.verbose:
                        print(f"   💾 Cached chunk to {cache_file.name}")

        # Combine all chunks by concatenating Arrow IPC files
        print(f"🔗 Combining {len(chunk_results)} chunks...")
        print(f"⚠️  Note: For very large datasets, consider using pl.scan_ipc() for lazy loading")

        # Use Polars' concat_lf (lazy frames) to avoid loading everything
        if self.config.return_type == "polars":
            # Collect all cached chunk file paths
            chunk_files = []
            for i, result in enumerate(chunk_results):
                if isinstance(result, Path):
                    chunk_files.append(result)
                else:
                    # If chunk is in memory, write it to temp file
                    temp_file = temp_dir / f"lymphoseq_mem_{session_id}_chunk_{i}.arrow"
                    result.write_ipc(temp_file, compression="zstd")
                    chunk_files.append(temp_file)

            print(f"   Combining {len(chunk_files)} cached chunks using lazy evaluation...")

            # Use scan_ipc for lazy loading and concat
            lazy_frames = [pl.scan_ipc(str(f)) for f in chunk_files]
            combined_lazy = pl.concat(lazy_frames, how="diagonal", rechunk=False)

            # Write to final output file without fully loading
            output_file = temp_dir / f"lymphoseq_output_{session_id}.arrow"
            print(f"   Writing combined output to {output_file}...")
            combined_lazy.sink_ipc(str(output_file), compression="zstd")

            # Clean up chunk files
            for f in chunk_files:
                try:
                    f.unlink()
                except:
                    pass

            print(f"✅ Combined data written to {output_file}")

            # In streaming mode, return LazyFrame instead of loading into memory
            if self.config.streaming_mode:
                print(f"🔗 Returning LazyFrame (use .collect() to load into memory if needed)")
                print(f"💡 Arrow file saved at: {output_file}")
                final_result = pl.scan_ipc(str(output_file))
                return final_result
            else:
                print(f"   Loading final result into memory...")
                try:
                    final_result = pl.read_ipc(output_file, memory_map=False)
                    total_records = len(final_result)
                except Exception as e:
                    print(f"⚠️  Could not load full dataset into memory: {e}")
                    print(f"💡 Use pl.scan_ipc('{output_file}') for lazy loading")
                    raise MemoryError(
                        f"Dataset too large to load into memory. "
                        f"Use pl.scan_ipc('{output_file}') for lazy operations."
                    )

        else:
            # Pandas path - convert chunks to Polars first for efficiency
            chunk_files = []
            for i, result in enumerate(chunk_results):
                if isinstance(result, Path):
                    chunk_files.append(result)
                else:
                    temp_file = temp_dir / f"lymphoseq_mem_{session_id}_chunk_{i}.arrow"
                    if isinstance(result, pd.DataFrame):
                        pl.from_pandas(result).write_ipc(temp_file, compression="zstd")
                    else:
                        result.write_ipc(temp_file, compression="zstd")
                    chunk_files.append(temp_file)

            print(f"   Combining {len(chunk_files)} cached chunks using lazy evaluation...")

            lazy_frames = [pl.scan_ipc(str(f)) for f in chunk_files]
            combined_lazy = pl.concat(lazy_frames, how="diagonal", rechunk=False)

            output_file = temp_dir / f"lymphoseq_output_{session_id}.arrow"
            print(f"   Writing combined output to {output_file}...")
            combined_lazy.sink_ipc(str(output_file), compression="zstd")

            # Clean up chunk files
            for f in chunk_files:
                try:
                    f.unlink()
                except:
                    pass

            print(f"✅ Combined data written to {output_file}")
            print(f"   Converting to pandas (this may take time for large datasets)...")

            try:
                final_result = pl.read_ipc(output_file, memory_map=False).to_pandas()
                total_records = len(final_result)
            except Exception as e:
                print(f"⚠️  Could not load full dataset into memory: {e}")
                print(f"💡 Use pl.scan_ipc('{output_file}').collect().to_pandas() for conversion")
                raise MemoryError(
                    f"Dataset too large to load into memory. "
                    f"Load incrementally using pl.scan_ipc('{output_file}')"
                )

        print(f"✅ Chunked processing complete: {total_records:,} total records")
        print(f"💾 Output saved to {output_file}")
        return final_result

    def save_to_arrow(self, data: Union[pd.DataFrame, pl.DataFrame], path: Union[str, Path]) -> None:
        """
        Save data to Arrow IPC format for fast I/O.

        Args:
            data: DataFrame to save
            path: Output file path
        """
        path = Path(path)
        if isinstance(data, pl.DataFrame):
            data.write_ipc(path, compression="zstd")
        else:
            pl.from_pandas(data).write_ipc(path, compression="zstd")
        print(f"💾 Saved to Arrow format: {path}")

    def load_from_arrow(self, path: Union[str, Path]) -> Union[pd.DataFrame, pl.DataFrame]:
        """
        Load data from Arrow IPC format.

        Args:
            path: Input file path

        Returns:
            Loaded DataFrame
        """
        path = Path(path)
        data = pl.read_ipc(path)

        if self.config.return_type == "pandas":
            return data.to_pandas()
        return data