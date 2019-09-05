# -*- coding: utf-8 -*-

import gseapy as gp
import pandas as pd
import os
import click


def do_gsea(matrix, cls, gmt, out_dir):
    """Run GSEA."""
    mat = pd.read_csv(matrix, sep='\t', header=0, index_col=0)
    click.echo('Running GSEA')
    gs_res = gp.gsea(
        data=mat,  # data matrix
        gene_sets=gmt,  # enrichr library names
        cls=cls,  # cls=class_vector
        # set permutation_type to phenotype if samples >=15
        permutation_type='phenotype',
        permutation_num=100,  # reduce number to speed up test
        outdir=out_dir,
        no_plot=True,  # Skip plotting
        method='signal_to_noise',
        processes=4,
        format='png',
    )
    out_path = os.path.join(out_dir, 'gsea_result.tsv')
    gs_res.res2d.to_csv(out_path, sep='\t')