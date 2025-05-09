#!/usr/bin/env python
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXCEL_PATH = RAW_DIR / "encuesta.xlsx"
EXCEL_COLS = 'F:Q'

RAW_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)
