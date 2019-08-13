# -*- coding: utf-8 -*-

"""Command line interface."""

import logging

import click

logger = logging.getLogger(__name__)


@click.group(help='pathrev')
def main():
    """Run pathrev."""
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")


@main.group()
def gsea():
    """Preprocessing utilities."""


@gsea.command(help='Run GSEA')
@click.option('-m', '--matrix', help="path to matrix", type=click.Path())
@click.option('-c', '--cls', help="path to cls file", type=click.Path())
@click.option('-g', '--gmt', help="path to gmt file", type=click.Path())
def run(matrix, cls, gmt):
    """Run GSEA."""
    NotImplemented


if __name__ == '__main__':
    main()
