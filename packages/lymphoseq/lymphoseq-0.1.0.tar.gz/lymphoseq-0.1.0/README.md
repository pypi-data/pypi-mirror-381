# LymphoSeq - Python Toolkit for AIRR-Seq Analysis

A Python implementation of the LymphoSeq2 R package for analyzing high-throughput sequencing of T and B cell receptors.

## Overview

LymphoSeq provides a comprehensive toolkit for importing, manipulating, and visualizing Adaptive Immune Receptor Repertoire Sequencing (AIRR-seq) data from various platforms including:

- Adaptive Biotechnologies ImmunoSEQ
- BGI IR-SEQ
- 10X Genomics VDJ sequencing
- MiXCR pipeline outputs

## Features

- **Multi-platform support**: Import data from major AIRR-seq platforms
- **AIRR standard compliance**: Full support for AIRR Community data standards
- **Automatic field mapping**: Platform-specific columns automatically converted to AIRR standard names
- **High-performance parsing**: Optimized for large datasets with parallel processing
- **10X single-cell support**: Merge paired alpha/beta chains for bulk-style analysis
- **Comprehensive analysis**: Clonality, diversity, and repertoire comparison tools
- **Database integration**: Search VDJdb, McPAS-TCR, and IEDB for known antigen specificities
- **Rich visualizations**: Interactive plots and publication-ready figures

## Documentation

- **[AIRR Field Mappings](docs/AIRR_FIELD_MAPPINGS.md)**: Complete documentation of platform-specific column mappings to AIRR standard fields
- **[10X Chain Merging Guide](docs/10X_CHAIN_MERGING.md)**: How to merge alpha/beta chains from 10X single-cell data
- **Command-line interface**: Easy-to-use CLI for batch processing

## Installation

```bash
pip install lymphoseq
```

For development installation:

```bash
git clone https://github.com/shashidhar22/lymphoseq.git
cd lymphoseq
pip install -e ".[dev]"
```

## Quick Start

### Bulk TCR-Seq Data

```python
import lymphoseq as ls

# Import AIRR-seq data
data = ls.read_immunoseq("path/to/data/")

# Calculate repertoire diversity metrics
diversity = ls.clonality(data)

# Visualize clonal expansion
fig = ls.plot_clonality(data)
fig.show()
```

### 10X Single-Cell Data

```python
import lymphoseq as ls

# Read 10X data
data_10x = ls.read_10x("path/to/10x_data/")

# Merge alpha and beta chains for bulk-style analysis
merged = ls.merge_chains(data_10x)

# Now use any bulk analysis function
clonality = ls.clonality(merged)
diversity = ls.diversity_metrics(merged)

# Search for known antigen specificities
annotated = ls.search_db(merged, databases="all", chain="trb")

# Visualize
fig = ls.plot_top_seqs(merged, top=50)
fig.show()
```

## Command Line Usage

```bash
# Import and analyze data
lymphoseq import --input data/ --output results/

# Calculate diversity metrics
lymphoseq analyze clonality --input results/data.parquet --output results/
```

## Documentation

Full documentation is available at [lymphoseq.readthedocs.io](https://lymphoseq.readthedocs.io)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgments

This package is inspired by and compatible with the original LymphoSeq2 R package by Elena Wu, Shashidhar Ravishankar, and David Coffey.