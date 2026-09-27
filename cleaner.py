"""Every cleaning rule as a function; QualityLog records what each one did."""
import pandas as pd

class QualityLog:
    def __init__(self): self.rows = []
    def add(self, problem, affected, fix, why): self.rows.append({"problem": problem, "rows_affected": int(affected), "fix": fix, "why": why})
    def to_frame(self): return pd.DataFrame(self.rows)

def clean_products(products, log):
    p = products.copy()
    # TODO: product_name whitespace; cost_price > unit_price -> flag column margin_ok. Log each rule.
    p["margin_ok"] = True
    return p

def clean_sales(sales, products, stores, log):
    df = sales.copy()
    # TODO, in this order, logging each: duplicates -> unit_price text to number -> dates (two formats!)
    #       -> negative qty -> unknown product_id -> unknown store_id -> missing discount_pct
    # Then derive: net_price = unit_price * (1 - discount_pct/100); revenue = net_price * qty
    return df.reset_index(drop=True)
