#!/usr/bin/env python
from pandas._config import display
from pia_hibp.setup.envs import *
from pia_hibp.config import *
from pia_hibp.setup.ms_auth import ms_graph_token
from pia_hibp.api_requests.ms_request import ms_excel_request
from pia_hibp.analyze.pd_analysis import *
import pandas as pd
#Creation of authorization token
token = ms_graph_token(app_id)

#Use of token to GET request spreadsheet from cloud to RAW dir
ms_excel_request(item_id, token)

# Creation of main dataframe
df = df_create(EXCEL_PATH, EXCEL_MAIN_COLS_RANGE, EXCEL_MAIN_COLS_NAME)

#Creation of hibp_key cells
add_hibp_cols(df, hibp_key)

#Prints of results
print(f"Porcentaje de brechas: {breach_percentage(df)}%")
print(f"Promedio de brechas: {breach_average(df)}")
print(f"Mediana de brechas: {breach_median(df)}")
