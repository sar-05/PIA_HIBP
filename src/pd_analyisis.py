#!/usr/bin/env python
import pandas as pd
from time import sleep
from hibp_request import hibp_breaches

#Creation of data frame based on the Forms Excel Spreadsheet
df = pd.read_excel("Encuesta PIA.xlsx", usecols='G:R')
df.columns = ['age', 'gender', 'studies', 'num_acc', 'services', 
              'diff_emails', 'diff_pass', '2fa', 
              'num_emails', 'main_email', 'age_email', 'usecase_email']

#Creation of HIBP data colums
indices_to_drop = []
df['breached'] = None
df['brech_num'] = None
for index in df.index:
    email = df.loc[index, 'main_email'] 
    response = hibp_breaches(email)
    if response is not None:
        df.loc[index, 'breached'] = response[0]
        df.loc[index, 'brech_num'] = response[1]
    else:
        indices_to_drop.append(index)
    sleep(6)
df.drop(indices_to_drop, axis=0, inplace=True)

print(df)
