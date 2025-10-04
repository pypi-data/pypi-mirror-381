from pathlib import Path

import click
from prelawsql import CODE_DIR, DB_FILE, STAT_DIR, TREE_GLOB
from sqlite_utils import Database


@click.group()
def cli():
    """Extensible wrapper of commands."""
    pass


@cli.command()
@click.option("--db-name", type=str, default=DB_FILE)
@click.option("--folder", type=Path, default=STAT_DIR)
@click.option("--pattern", type=str, default=TREE_GLOB)
def source_statutes(db_name: str, folder: str, pattern: str):
    """Create statute tables and populate with *.yml files from `--folder`."""
    from .tree_statute import Statute

    Statute.source(db_name=db_name, folder=folder, pattern=pattern)


@cli.command()
@click.option("--db-name", type=str, default=DB_FILE)
def set_statute_views(db_name: str):
    """After setting up the statutes tables, create the related views."""
    from .tree_statute import Statute

    if not Path(db_name).exists():
        raise Exception("Must source statutes first.")

    db = Database(filename_or_conn=db_name, use_counts_table=True)
    Statute.create_related_views(db)


@cli.command()
@click.option("--db-name", type=str, default=DB_FILE)
def drop_statute_views(db_name: str):
    """For troubleshooting, drop views created by `set_statute_views`."""
    from .tree_statute import Statute

    if not Path(db_name).exists():
        raise Exception("Must source statutes first.")

    db = Database(filename_or_conn=db_name, use_counts_table=True)
    Statute.drop_related_views(db)


@cli.command()
@click.option("--db-name", type=str, default=DB_FILE)
@click.option("--folder", type=Path, default=CODE_DIR)
@click.option("--pattern", type=str, default=TREE_GLOB)
def source_codifications(db_name: str, folder: str, pattern: str):
    """Create codification tables and populate with *.yml files from `--folder`."""
    from .tree_codification import Codification

    Codification.source(db_name=db_name, folder=folder, pattern=pattern)


if __name__ == "__main__":
    cli()  # search @cli.command
