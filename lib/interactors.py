"""
Filter by WD and Z scores
"""

import pandas as pd
import sys
from contextlib import suppress
from os import path


def _filter_and_join(df, wd_percentile, z_percentile):
    wd = df.loc[df["WD"] >= df["WD"].quantile(float(wd_percentile))]
    z = df.loc[df["Z"] >= df["Z"].quantile(float(z_percentile))]
    return pd.merge(wd, z, how="inner")


def calibrate(input_, bait, wd_percentile, z_percentile, out=None):
    df = pd.read_csv(input_, sep="\t")
    df2 = df.loc[df["Bait"] == bait]

    merged = _filter_and_join(df2, wd_percentile, z_percentile)
    with out or suppress():
        print(merged)


def filter_bait(input_, wd_percentile, z_percentile, out=None):
    df = pd.read_csv(input_, sep="\t")
    bait = df.groupby("Bait")

    frames = []
    for _, g in bait:
        frames.append(_filter_and_join(g, wd_percentile, z_percentile))

    merged = pd.concat(frames)
    out_name = path.splitext(input_)[0] + "_filtered.csv"
    merged.to_csv(out_name)
