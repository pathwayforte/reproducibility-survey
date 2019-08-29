# -*- coding: utf-8 -*-

"""Command line interface."""

import logging
import gseapy as gp
import pandas as pd
import numpy as np
import click
import pickle

logger = logging.getLogger(__name__)


@click.group(help='pathrev')
def main():
    """Run pathrev."""
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")


@main.group()
def gsea():
    """GSEA functionalities."""


@gsea.command(help='Run GSEA')
@click.option(
    '-m', '--matrix',
    help="path to matrix",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
@click.option(
    '-c', '--cls',
    help="path to cls file",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
@click.option(
    '-g', '--gmt',
    help="path to gmt file",
    type=click.Path(file_okay=True, dir_okay=False, exists=True),
    required=True
    )
# @click.option(
#     '-p', '--pkl',
#     help="path to Miniml pkl",
#     type=click.Path(file_okay=True, dir_okay=False, exists=True),
#     required=True
#     )
def run(matrix, cls, gmt):
    """Run GSEA."""
    click.echo("Run {} with {}, {}".format(matrix, cls, gmt))
    # Miniml_data = pd.read_pickle(pkl)
    # Miniml_data.iloc[1, :].isnull().values.any()
    # Miniml_data.set_index('ID', inplace=True)
    # click.echo('Reading the matrix file')
    df = pd.read_csv(matrix, sep='\t', header=0)
    # click.echo('Processing the matrix file')
    # df['ID_REF'] = df['ID_REF'].astype(str)
    # for i in df.index:
    #     id_ref = df.at[i, 'ID_REF']
    #     try:
    #         df.at[i, 'ID_REF'] = Miniml_data.at[int(id_ref), 'GENE_SYMBOL']
    #     except KeyError:
    #         df.at[i, 'ID_REF'] = '---'
    # # if df.ID_REF.nunique() == 1:
    # # continue
    # new_index = sorted(df.columns[1:], key=lambda col_name: int(col_name[12:-4]))
    # new_index.insert(0, 'ID_REF')
    # df = df.reindex(new_index, axis=1)
    click.echo('Running GSEA')
    gs_res = gp.gsea(
        data=df,  # or data='./P53_resampling_data.txt'
        gene_sets=gmt,  # enrichr library names
        cls=cls,  # cls=class_vector
        # set permutation_type to phenotype if samples >=15
        permutation_type='phenotype',
        permutation_num=100,  # reduce number to speed up test
        outdir=None,  # do not write output to disk
        no_plot=True,  # Skip plotting
        method='signal_to_noise',
        processes=4,
        format='png',
    )
    gs_res.res2d.to_csv('results/31316060/gsea_result.tsv', sep='\t')
    gs_res.res2d.to_pickle('results/31316060/gsea_result_res2d.pkl')
    gs_res.heatmat.to_pickle('results/31316060/gsea_result_heatmat.pkl')
    click.echo('End')


if __name__ == '__main__':
    main()
