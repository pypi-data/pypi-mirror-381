from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
from .core import topsis

def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="topsisx", description="TOPSIS CLI")
    p.add_argument("csv", help="Input CSV (first column may be an identifier).")
    p.add_argument("--weights", required=True, help="Comma-separated weights, e.g., 1,1,1,2")
    p.add_argument("--impacts", required=True, help="Comma-separated + or -, e.g., +,+,-,+")
    p.add_argument("--output", "-o", help="Output CSV (default: input + _topsis.csv)")
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    weights = [float(x) for x in args.weights.split(",")]
    impacts = [x.strip() for x in args.impacts.split(",")]
    df = pd.read_csv(args.csv)
    scores, ranks = topsis(df, weights, impacts)
    out = df.copy()
    out["Score"] = scores
    out["Rank"] = ranks
    out_path = args.output or str(Path(args.csv).with_name(Path(args.csv).stem + "_topsis.csv"))
    out.to_csv(out_path, index=False)
    print(f"Wrote TOPSIS results to: {out_path}")
