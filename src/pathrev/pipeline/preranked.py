# -*- coding: utf-8 -*-

import gseapy as gp
import pandas as pd
import os
import click


def do_preranked(rnk, gmt, out_dir):
    """Run GSEA-PreRanked."""

    rnk = pd.read_csv(rnk, sep='\t', header=0, index_col=0)
    click.echo('Running GSEA-PreRanked')
    pre_res = gp.prerank(rnk=rnk,
                         gene_sets=gmt,
                         processes=4,
                         permutation_num=100,  # reduce number to speed up testing
                         outdir=out_dir, format='png')
    out_path = os.path.join(out_dir, 'prerank_result.tsv')
    pre_res.res2d.to_csv(out_path, sep='\t')
