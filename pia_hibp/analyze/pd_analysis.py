#!/usr/bin/env python
import pandas as pd
from time import sleep
from pia_hibp.config import EXCEL_PATH, EXCEL_COLS
from pia_hibp.api_requests.hibp_request import hibp_breaches

#Creates data frame based on the Forms Excel Spreadsheet
def df_create(excel_path=EXCEL_PATH):
    try:
        df = pd.read_excel(excel_path, usecols=EXCEL_COLS)
    except FileNotFoundError:
        print(f"No existe {excel_path}")
        raise FileNotFoundError
    else:
        df.columns = ['age', 'gender', 'studies', 'num_acc', 'services', 
                      'diff_emails', 'diff_pass', '2fa', 'num_emails',
                      'main_email', 'age_email', 'usecase_email']
        return df

#Creates HIBP data colums
def add_hibp_cols(df, hibp_key):
    if 'main_email' in df:
        indices_to_drop = []
        df['breached'] = None
        df['brech_num'] = None
        for index in df.index:
            email = df.loc[index, 'main_email'] 
            try:
                response = hibp_breaches(email, hibp_key)
                df.loc[index, 'breached'] = response[0]
                df.loc[index, 'brech_num'] = response[1]
            except:
                indices_to_drop.append(index)
            sleep(6)
        if indices_to_drop is not []:
            df.drop(indices_to_drop, axis=0, inplace=True)
    else:
        print("El excel no contiene columna de correos electrónicos")
        raise ValueError
