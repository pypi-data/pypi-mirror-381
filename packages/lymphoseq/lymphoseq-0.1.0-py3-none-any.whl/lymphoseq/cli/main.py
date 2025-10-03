"""
Main CLI application for LymphoSeq.

Provides commands for importing, analyzing, and visualizing AIRR-seq data.
"""

import typer
from pathlib import Path
from typing import Optional, List
from rich.console import Console
from rich.progress import track

from ..parsers import read_immunoseq, read_10x, read_mixcr
from ..analysis import clonality, diversity_metrics
from ..visualization import plot_clonality

app = typer.Typer(
    name="lymphoseq",
    help="Python toolkit for analyzing AIRR-seq data",
    no_args_is_help=True
)
console = Console()


@app.command()
def import_data(
    input_path: Path = typer.Argument(..., help="Path to input data directory or file"),
    output: Path = typer.Option("output.parquet", help="Output file path"),
    platform: str = typer.Option("auto", help="Data platform (immunoseq, 10x, mixcr, auto)"),
    recursive: bool = typer.Option(False, help="Search recursively in subdirectories"),
    parallel: bool = typer.Option(True, help="Process files in parallel"),
    threads: Optional[int] = typer.Option(None, help="Number of threads to use"),
    format: str = typer.Option("parquet", help="Output format (parquet, csv, tsv)")
):
    """
    Import AIRR-seq data from various platforms.

    Supports ImmunoSEQ, 10X Genomics, and MiXCR data formats.
    """
    try:
        console.print(f"[bold blue]Importing data from {input_path}[/bold blue]")

        # Choose parser based on platform
        if platform == "immunoseq" or platform == "auto":
            data = read_immunoseq(
                input_path,
                recursive=recursive,
                parallel=parallel,
                threads=threads,
                return_type="polars"
            )
        elif platform == "10x":
            data = read_10x(
                input_path,
                recursive=recursive,
                parallel=parallel,
                threads=threads,
                return_type="polars"
            )
        elif platform == "mixcr":
            data = read_mixcr(
                input_path,
                recursive=recursive,
                parallel=parallel,
                threads=threads,
                return_type="polars"
            )
        else:
            console.print(f"[bold red]Error: Unknown platform '{platform}'[/bold red]")
            raise typer.Exit(1)

        # Save data
        console.print(f"[green]Successfully imported {len(data)} sequences[/green]")

        output.parent.mkdir(parents=True, exist_ok=True)

        if format == "parquet":
            data.write_parquet(output)
        elif format == "csv":
            data.write_csv(output)
        elif format == "tsv":
            data.write_csv(output, separator="\t")
        else:
            console.print(f"[bold red]Error: Unknown format '{format}'[/bold red]")
            raise typer.Exit(1)

        console.print(f"[green]Data saved to {output}[/green]")

    except Exception as e:
        console.print(f"[bold red]Error importing data: {e}[/bold red]")
        raise typer.Exit(1)


@app.command()
def analyze(
    input_file: Path = typer.Argument(..., help="Input data file (parquet, csv, tsv)"),
    output_dir: Path = typer.Option("analysis_results", help="Output directory"),
    analysis_type: str = typer.Option("clonality", help="Analysis type (clonality, diversity)"),
    rarefy: bool = typer.Option(False, help="Perform rarefaction analysis"),
    min_count: Optional[int] = typer.Option(None, help="Minimum count for rarefaction"),
    iterations: int = typer.Option(100, help="Number of rarefaction iterations")
):
    """
    Perform repertoire analysis on imported data.

    Calculate diversity metrics, clonality, and other repertoire characteristics.
    """
    try:
        console.print(f"[bold blue]Analyzing data from {input_file}[/bold blue]")

        # Load data
        import polars as pl
        if input_file.suffix == ".parquet":
            data = pl.read_parquet(input_file)
        elif input_file.suffix == ".csv":
            data = pl.read_csv(input_file)
        elif input_file.suffix == ".tsv":
            data = pl.read_csv(input_file, separator="\t")
        else:
            console.print(f"[bold red]Error: Unsupported file format[/bold red]")
            raise typer.Exit(1)

        output_dir.mkdir(parents=True, exist_ok=True)

        if analysis_type == "clonality":
            console.print("[yellow]Calculating clonality metrics...[/yellow]")
            results = clonality(
                data,
                rarefy=rarefy,
                min_count=min_count,
                iterations=iterations
            )

            # Save results
            output_file = output_dir / "clonality_results.csv"
            results.write_csv(output_file)
            console.print(f"[green]Clonality results saved to {output_file}[/green]")

        elif analysis_type == "diversity":
            console.print("[yellow]Calculating diversity metrics...[/yellow]")
            results = diversity_metrics(data)

            # Save results
            output_file = output_dir / "diversity_results.csv"
            results.write_csv(output_file)
            console.print(f"[green]Diversity results saved to {output_file}[/green]")

        else:
            console.print(f"[bold red]Error: Unknown analysis type '{analysis_type}'[/bold red]")
            raise typer.Exit(1)

    except Exception as e:
        console.print(f"[bold red]Error during analysis: {e}[/bold red]")
        raise typer.Exit(1)


@app.command()
def plot(
    input_file: Path = typer.Argument(..., help="Input analysis results file"),
    output_dir: Path = typer.Option("plots", help="Output directory for plots"),
    plot_type: str = typer.Option("clonality", help="Plot type (clonality, diversity)")
):
    """
    Generate visualizations from analysis results.

    Create publication-ready plots and interactive visualizations.
    """
    try:
        console.print(f"[bold blue]Creating plots from {input_file}[/bold blue]")

        # Load results
        import polars as pl
        if input_file.suffix == ".parquet":
            data = pl.read_parquet(input_file)
        else:
            data = pl.read_csv(input_file)

        output_dir.mkdir(parents=True, exist_ok=True)

        if plot_type == "clonality":
            console.print("[yellow]Generating clonality plots...[/yellow]")
            fig = plot_clonality(data)

            # Save plot
            output_file = output_dir / "clonality_plot.html"
            fig.write_html(output_file)
            console.print(f"[green]Clonality plot saved to {output_file}[/green]")

        else:
            console.print(f"[bold red]Error: Unknown plot type '{plot_type}'[/bold red]")
            raise typer.Exit(1)

    except Exception as e:
        console.print(f"[bold red]Error creating plots: {e}[/bold red]")
        raise typer.Exit(1)


@app.command()
def version():
    """Show version information."""
    from .. import __version__
    console.print(f"LymphoSeq version {__version__}")


@app.command()
def pipeline(
    input_path: Path = typer.Argument(..., help="Path to input data"),
    output_dir: Path = typer.Option("lymphoseq_results", help="Output directory"),
    platform: str = typer.Option("auto", help="Data platform"),
    recursive: bool = typer.Option(False, help="Search recursively"),
    parallel: bool = typer.Option(True, help="Process in parallel"),
    analysis_types: List[str] = typer.Option(["clonality"], help="Analysis types to run")
):
    """
    Run complete LymphoSeq analysis pipeline.

    Import data, perform analysis, and generate visualizations in one command.
    """
    try:
        console.print("[bold blue]Running LymphoSeq pipeline[/bold blue]")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Step 1: Import data
        console.print("[yellow]Step 1: Importing data...[/yellow]")
        data_file = output_dir / "imported_data.parquet"

        # Import based on platform
        if platform == "immunoseq" or platform == "auto":
            data = read_immunoseq(input_path, recursive=recursive, parallel=parallel)
        elif platform == "10x":
            data = read_10x(input_path, recursive=recursive, parallel=parallel)
        elif platform == "mixcr":
            data = read_mixcr(input_path, recursive=recursive, parallel=parallel)
        else:
            console.print(f"[bold red]Error: Unknown platform '{platform}'[/bold red]")
            raise typer.Exit(1)

        data.write_parquet(data_file)
        console.print(f"[green]✓ Data imported: {len(data)} sequences[/green]")

        # Step 2: Analysis
        for analysis_type in analysis_types:
            console.print(f"[yellow]Step 2: Running {analysis_type} analysis...[/yellow]")

            if analysis_type == "clonality":
                results = clonality(data)
                results_file = output_dir / "clonality_results.csv"
                results.write_csv(results_file)

                # Generate plot
                fig = plot_clonality(results)
                plot_file = output_dir / "clonality_plot.html"
                fig.write_html(plot_file)

                console.print(f"[green]✓ Clonality analysis complete[/green]")

        console.print("[bold green]Pipeline completed successfully![/bold green]")
        console.print(f"[green]Results saved to: {output_dir}[/green]")

    except Exception as e:
        console.print(f"[bold red]Pipeline failed: {e}[/bold red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()