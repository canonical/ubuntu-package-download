"""Console script for ubuntu_package_download."""

import click
import logging
import sys
import typer

from rich.console import Console
from typing_extensions import Annotated

from ubuntu_package_download.lib import download_deb

app = typer.Typer()
console = Console()


@app.command()
def main(
    package_name:
        Annotated[str, typer.Option(help="Package name")],
    package_version:
        Annotated[str, typer.Option(help="Package version")],
    logging_level:
        Annotated[str, typer.Option(
            help="How detailed would you like the output.",
            click_type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"]))] = "ERROR",
    package_architecture:
        Annotated[str, typer.Option(help="The architecture of the package you want to download.")] = "amd64",
    fallback:
        Annotated[bool, typer.Option(help="If the exact version cannot be found should we download the next version?")] = False,
    series:
        Annotated[str, typer.Option(help="The Ubuntu series eg. '20.04' or 'focal'.")] = None,
    ):
    # , package_version: str, logging_level: str, package_architecture: str, fallback: str, series: str):
    """Console script for ubuntu_package_download."""
    console.print(f"Package name is {package_name}")
    console.print(f"Package version is {package_version}")
    console.print(f"Logging level is {logging_level}")
    console.print(f"Package architecture is {package_architecture}")
    console.print(f"Fallback is {fallback}")
    console.print(f"Series is {series}")

    level = logging.getLevelName(logging_level)
    logging.basicConfig(level=level, stream=sys.stderr, format="%(asctime)s [%(levelname)s] %(message)s")

    download_deb(package_name, package_version, package_architecture, fallback, series)


if __name__ == "__main__":
    app()
