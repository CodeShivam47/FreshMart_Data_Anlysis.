"""CLI:  python -m freshmart report --store 3 --month 6"""
import argparse
from .loader import SalesLoader
from .cleaner import clean_sales, clean_products, QualityLog
from .report import top_margin, store_productivity, stockouts

def main():
    ap = argparse.ArgumentParser(prog="freshmart")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report"); r.add_argument("--data", default="data"); r.add_argument("--store", type=int); r.add_argument("--month", type=int)
    args = ap.parse_args()
    # TODO: load -> clean -> filter by month if given -> print top_margin, store_productivity, stockouts
    print("not implemented yet")

if __name__ == "__main__":
    main()
