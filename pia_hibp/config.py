#!/usr/bin/env python
from pathlib import Path

# Estructura de directorios
ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROC_DIR = DATA_DIR / "processed"
SURVEY_DIR = PROC_DIR / "survey"
HIBP_DIR = PROC_DIR / "hibp"

# Archivos
SURVEY_FILE = RAW_DIR / "encuesta.xlsx"
HIBP_TXT = RAW_DIR / "hibp_cleaned.txt"
OUTPUT_EXCEL = SURVEY_DIR / "rates.xlsx"

# Configuración de columnas
COL_RANGE = 'F:P'
SURVEY_COLS = [
    'age', 'gender', 'studies', 'number_of_accounts',
    'used_services', 'diff_passwords', '2fa',
    'number_of_emails', 'main_email', 'main_email_age',
    'main_email_usecase'
]

# Columnas para análisis
DEMO_COLS = ['age', 'studies', 'number_of_accounts','2fa']

# Grupos Demográficos
COLS_NAMES = ['Edad', "Nivel Educativo", "Número de cuentas", "Uso de 2FA"]

# Crear directorios si no existen
DATA_DIR = ROOT_DIR / "data"
RAW_DIR.mkdir(exist_ok=True)
PROC_DIR.mkdir(exist_ok=True)
SURVEY_DIR.mkdir(exist_ok=True)
HIBP_DIR.mkdir(exist_ok=True)
