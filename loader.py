"""Load and validate the four FreshMart files."""
from pathlib import Path
import pandas as pd

REQUIRED = {
    "sales_2025.csv": ["receipt_id", "store_id", "product_id", "sale_date", "qty", "unit_price", "discount_pct"],
    "products.csv": ["product_id", "product_name", "category", "unit_price", "cost_price", "is_perishable"],
    "stores.csv": ["store_id", "store_name", "city", "opened_on", "floor_area_sqft"],
    "promotions.csv": ["promo_id", "product_id", "store_id", "start_date", "end_date", "discount_pct"],
}

class DataFileError(Exception):
    """A required file is missing or unreadable."""

class SchemaError(Exception):
    """A file is missing required columns."""

class SalesLoader:
    """Reads the four CSVs from a folder and validates their columns."""
    def __init__(self, folder):
        self.folder = Path(folder)
        # TODO: raise DataFileError if the folder does not exist

    def _read(self, name):
        # TODO: raise DataFileError if the file is missing
        df = pd.read_csv(self.folder / name)
        # TODO: raise SchemaError listing any missing REQUIRED columns
        return df

    def load_all(self):
        return {name.split(".")[0].replace("_2025", ""): self._read(name) for name in REQUIRED}

    def stream_sales(self, chunksize=5000):
        """Generator: yield the sales file chunk by chunk (pd.read_csv(..., chunksize=))."""
        # TODO
        yield from ()
