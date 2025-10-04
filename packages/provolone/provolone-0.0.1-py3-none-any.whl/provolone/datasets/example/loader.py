from __future__ import annotations
from pathlib import Path
import pandas as pd
from ..base import BaseDataset
from ...config import cfg
from .. import register


@register("example")
class Dataset(BaseDataset):
    name = "example"
    frequency = "m"

    def fetch(self):
        # Try real file first; otherwise signal to parse() to fall back
        # data_dir points directly to this dataset's data directory
        candidate = self.data_dir / f"{self.name}.csv"
        return candidate if candidate.exists() else None

    def parse(self, raw) -> pd.DataFrame:
        if isinstance(raw, Path) and raw and raw.exists():
            df = pd.read_csv(raw, parse_dates=["date"])
            return df.set_index("date")

        # Fallback minimal DF
        df = pd.DataFrame(
            {
                "date": pd.date_range("2000-01-01", periods=3, freq="MS"),
                "value": [1.0, 2.0, 3.0],
            }
        )
        return df.set_index("date")
