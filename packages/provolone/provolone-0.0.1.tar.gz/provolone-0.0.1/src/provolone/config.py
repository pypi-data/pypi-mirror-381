from __future__ import annotations
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    data_root: Path = Path.home() / "data"
    cache_dir: Path = Path.home() / ".cache" / "provolone"
    snapshots_root: Path = Path.home() / ".local" / "share" / "provolone" / "snapshots"
    io_format: str = "parquet"  # "feather" or "parquet"
    io_compression: str | None = "zstd"  # "zstd"|"lz4"|None
    normalize_columns: bool = True  # global default; datasets can override

    model_config = SettingsConfigDict(
        env_prefix="PROVOLONE_",  # expects PROVOLONE_SNAPSHOTS_ROOT, etc.
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


cfg = Settings()
# Directories are created lazily when needed, not on import
# See _snapshot_paths() in snapshots.py which creates directories when writing
