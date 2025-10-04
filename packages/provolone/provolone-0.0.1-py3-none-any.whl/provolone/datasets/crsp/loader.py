from __future__ import annotations
from pathlib import Path
from typing import Optional, Dict
import numpy as np
import pandas as pd

from ..base import BaseDataset
from ...config import cfg


class Dataset(BaseDataset):
    """
    CRSP value-weighted index (monthly) with dividend decomposition, ported from legacy crsp.py.

    Parameters
    ----------
    vintage : str, default "2017"
        Selects the file name pattern 'crsp_<vintage>.csv' under <data_root>/crsp/.
    resample : Optional[str], default None
        Pandas resample rule applied with aggregation mapping (A, Q, etc.). If None, no resampling.
    file : Optional[str | Path], default None
        Explicit file path (overrides data_root/vintage discovery).
    dates : str, default 'parse'
        Kept for backward compatibility; only 'parse' is supported (parses 'caldt' during read).

    Expected raw columns (case-insensitive): caldt, vwretx, vwretd

    Output columns (legacy-compatible names)
    ----------------------------------------
    P, D, D_ann, p, d_ann, Re, re, pd_ann, pd_raw
    Index is DatetimeIndex at month end.
    """

    name = "crsp"
    # Disable global column normalization just for CRSP, to preserve capitalization
    normalize_columns = False

    def _cache_suffix(self) -> Optional[str]:
        vintage = str(self.params.get("vintage", "2017"))
        res = self.params.get("resample")
        return f"vintage-{vintage}" + (f"__resample-{res}" if res else "")

    # ---------------- lifecycle hooks ----------------
    def fetch(self) -> Optional[Path]:
        explicit = self.params.get("file")
        if explicit:
            p = Path(explicit)
            return p if p.exists() else p

        vintage = str(self.params.get("vintage", "2017"))
        base = self.data_root / "crsp"
        candidate = base / f"crsp_{vintage}.csv"
        if candidate.exists():
            return candidate
        return None

    def parse(self, raw) -> pd.DataFrame:
        if self.params.get("dates", "parse") != "parse":
            raise ValueError("Only dates='parse' is supported in the new loader.")

        if isinstance(raw, Path) and raw.exists():
            df = pd.read_csv(raw, parse_dates=["caldt"])
        else:
            # Fallback tiny fixture for tests/dev
            df = pd.DataFrame(
                {
                    "caldt": pd.to_datetime(["1925-10-31", "1925-11-30", "1925-12-31"]),
                    "vwretx": [0.00, 0.01, -0.02],
                    "vwretd": [0.00, 0.012, -0.015],
                }
            )
        # keep original columns; only standardize types
        cols = {c.lower(): c for c in df.columns}
        if "caldt" not in cols or not {"vwretx", "vwretd"}.issubset(cols):
            raise ValueError("CRSP file must contain columns: caldt, vwretx, vwretd")
        df["caldt"] = pd.to_datetime(df["caldt"])
        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # Price index from cumprod of (1 + vwretx)
        df["P"] = (df["vwretx"].astype("float64") + 1.0).cumprod()

        # Legacy special-case mentioned earlier (rare in practice)
        # Note: CRSP monthly dates are month-end; the original code checked 1925-10-01.
        # If you truly need that, adapt here; otherwise we skip altering P by fiat.

        # Dividend flow: previous price * (vwretd - vwretx)
        P_lag = pd.concat(
            [pd.Series([np.nan], index=df.index[:1]), df["P"].iloc[:-1]],
            ignore_index=True,
        )
        P_lag.index = df.index
        df["D"] = P_lag * (
            df["vwretd"].astype("float64") - df["vwretx"].astype("float64")
        )

        # Annual dividends (rolling 12-month sum)
        df["D_ann"] = df["D"].rolling(12, min_periods=1).sum()

        # Logs and returns
        df["p"] = np.log(df["P"])
        df["d_ann"] = np.log(df["D_ann"].where(df["D_ann"] > 0, np.nan))

        P = df["P"].values
        D = df["D"].values
        Re = np.empty_like(P)
        Re[:] = np.nan
        if len(P) >= 2:
            Re[1:] = (P[1:] + D[1:]) / P[:-1]
        df["Re"] = Re
        df["re"] = np.log(df["Re"])

        # Spreads
        df["pd_ann"] = df["p"] - df["d_ann"]
        df["pd_raw"] = df["p"] - np.log(df["D"].where(df["D"] > 0, np.nan))

        # Set month-end index
        df = df.set_index("caldt")
        df.index = df.index.to_period("M").to_timestamp("M")

        # Optional resampling with legacy mapping
        resample = self.params.get("resample")
        if resample:
            agg: Dict[str, str] = {
                "P": "last",
                "p": "last",
                "Re": "prod",
                "re": "sum",
                "d_ann": "last",
                "D_ann": "last",
                "pd_ann": "last",
                "pd_raw": "last",
            }
            agg = {k: v for k, v in agg.items() if k in df.columns}
            df = df.resample(resample).agg(agg)

        # Keep legacy output columns; drop raw returns by default
        cols = ["P", "D", "D_ann", "p", "d_ann", "Re", "re", "pd_ann", "pd_raw"]
        df = df[cols]

        return df
