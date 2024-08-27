from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).parent.resolve()
PROJECT_DIR = next(iter(p for p in HERE.parents if (p / "pyproject.toml").exists()))
