#!/usr/bin/env python
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXCEL_PATH = RAW_DIR / "encuesta.xlsx"
EXCEL_MAIN_COLS_RANGE = 'F:P'
EXCEL_MAIN_COLS_NAME = ['age', 'gender', 'studies', 'num_acc', 'services', 
                   'diff_pass', '2fa', 'num_emails','main_email',
                   'age_email', 'usecase_email']

RAW_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)
