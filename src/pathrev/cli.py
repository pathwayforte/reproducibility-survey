# -*- coding: utf-8 -*-

"""Command line interface."""

import logging
import click
from pathrev.pipeline import (
    do_gsea, do_preranked,
)

logger = logging.getLogger(__name__)


@click.group(help='pathrev')
def main():
    """Run pathrev."""
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

matrix_option = click.option(
    '-m', '--matrix',
    help="path to matrix",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
rnk_option = click.option(
    '-r', '--rank',
    help="path to rank file",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
phenotype_option = click.option(
    '-c', '--cls',
    help="path to cls file",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
gene_set_option = click.option(
    '-g', '--gmt',
    help="path to gmt file",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
out_dir_option = click.option(
    '-o', '--out',
    help="path to output directory",
    type=click.Path(file_okay=False, dir_okay=True, exists=False),
    required=True
    )


@matrix_option
@phenotype_option
@gene_set_option
@out_dir_option
@main.command()
def gsea(matrix, cls, gmt, out_dir):
    """Run normal GSEA with a matrix file."""
    click.echo("Running GSEA on {} with {}, {} and outputting to {}".format(matrix, cls, gmt, out_dir))
    do_gsea(matrix, cls, gmt, out_dir)
    click.echo('Done with GSEA analysis')

@rnk_option
@gene_set_option
@out_dir_option
@main.command()
def prerank(rnk, gmt, out_dir):
    """Run prerank GSEA with a sorted rank file."""
    click.echo("Running GSEA-PreRanked on {} with {} and outputting to {}".format(rnk, gmt, out_dir))
    do_preranked(rnk, gmt, out_dir)
    click.echo('Done with prerank analysis')


if __name__ == '__main__':
    main()
