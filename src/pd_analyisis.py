#!/usr/bin/env python
import pandas as pd
from time import sleep
from hibp_request import hibp

df = pd.read_excel("Encuesta PIA.xlsx", usecols='G:R')
df.columns = ['age', 'gender', 'studies', 'num_acc', 'services', 
              'diff_emails', 'diff_pass', '2fa', 
              'num_emails', 'main_email', 'age_email', 'usecase_email']

indices_to_drop = []
df['breached'] = None
for index in df.index:
    response = hibp(df.loc[index, 'main_email'])
    if response is not None:
        df.loc[index, 'breached'] = response
    else:
        indices_to_drop.append(index)
    sleep(6)

df.drop(indices_to_drop, axis=0, inplace=True)

print(df['breached'])
