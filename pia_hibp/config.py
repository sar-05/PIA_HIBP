#!/usr/bin/env python
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXCEL_PATH = RAW_DIR / "encuesta.xlsx"
EXCEL_MAIN_COLS_RANGE = 'F:P'
EXCEL_MAIN_COLS_NAME = ['age', 'gender', 'studies', 'number_of_accounts',
                        'used_services', 'diff_passwords', '2fa',
                        'number_of_emails', 'main_email', 'main_email_age',
                        'main_email_usecase']

ANALYSIS_COLS = ['age', 'gender', 'studies', 'number_of_accounts',
                        'diff_passwords', '2fa', 'number_of_emails', 'main_email_age',]
                        



DATA_TXT_PATH = PROCESSED_DIR / "data.txt"


RAW_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)
