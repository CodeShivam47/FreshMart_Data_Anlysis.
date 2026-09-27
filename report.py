"""Analysis functions. Each returns a DataFrame; each is timed."""
import time, functools
import numpy as np, pandas as pd

def timed(fn):
    """TODO: decorator that prints how long fn took. Use functools.wraps."""
    return fn

@timed
def top_margin(sales, products, store_id=None, n=10):
    """Top n products by (net_price - cost_price) * qty. Exclude rows where margin_ok is False."""
    raise NotImplementedError

@timed
def promo_lift(sales, promotions, rng=None, n_perm=1000):
    """For each promotion: qty/day in the promo window vs same weekdays in the 8 weeks before; permutation p-value."""
    raise NotImplementedError

@timed
def patterns(sales, products):
    """Return two pivot tables: category x weekday units, category x month units."""
    raise NotImplementedError

@timed
def stockouts(sales, min_rate=1.5, min_run=6):
    """Product-store pairs with >= min_rate receipts/day on average and a run of >= min_run zero-sale days."""
    raise NotImplementedError

@timed
def store_productivity(sales, products, stores):
    """Revenue, margin, receipts and margin per sq ft per store."""
    raise NotImplementedError
