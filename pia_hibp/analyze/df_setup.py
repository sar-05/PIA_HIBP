#!/usr/bin/env python
import pandas as pd
from time import sleep
from pia_hibp.api_requests.hibp_request import hibp_requests 

#Creates data frame based on the Forms Excel Spreadsheet
def df_create(excel_path, col_range, col_names):
    try:
        df = pd.read_excel(excel_path, usecols=col_range)
    except FileNotFoundError:
        print(f"No existe {excel_path}")
    else:
        df.columns = col_names  
        return df

#Creates HIBP data colums
def add_hibp_cols(df, hibp_key):
    if 'main_email' in df:
        indices_to_drop = []
        df['breached'] = None
        df['breach_num'] = None
        for index in df.index:
            email = df.loc[index, 'main_email'] 
            try:
                response = hibp_requests(hibp_key, email=email)
            except:
                indices_to_drop.append(index)
            else:
                df.loc[index, 'breached'] = response[0]
                df.loc[index, 'breach_num'] = response[1]
            sleep(6)
        if len(indices_to_drop) > 0:
            df.drop(indices_to_drop, axis=0, inplace=True)
    else:
        print("El excel no contiene columna de correos electrónicos")
        raise ValueError

def breach_percentage(df):
    if 'breached' not in df.columns:
        raise ValueError("El dataframe no contiene columna breached")
    total_participants = len(df) #Total de filas
    affected_participants = df['breached'].sum() #Suma num filas donde breached es True
    if total_participants > 0:
        percentage = (affected_participants / total_participants) * 100
    else:
        percentage = 0
    return percentage
