#!/usr/bin/env python

import pandas as pd

import pia_hibp.config as config
from pia_hibp.setup import envs, ms_auth
from pia_hibp.api_requests import ms_requests, hibp_request
from pia_hibp.analyze import df_setup, breach_rate, hibp_db, hibp_analysis
from pia_hibp.visualize import graphs

#Creation of authorization token
token = ms_auth.ms_graph_token(envs.app_id)

#Use of token to GET request spreadsheet from cloud to RAW dir
ms_requests.excel_request(config.SURVEY_FILE, envs.item_id, token)

# Creation of main dataframe
df = df_setup.df_create(config.SURVEY_FILE,config.COL_RANGE,config.SURVEY_COLS)

#Creation of hibp_key cells
print("Generando columnas en base a HIBP")
df_setup.add_hibp_cols(df, envs.hibp_key)

rates_dfs = []
for col in config.DEMO_COLS:
    rates_dfs.append(breach_rate.by_group(df, col))

with pd.ExcelWriter(config.OUTPUT_EXCEL) as excel:
    for i in range(len(rates_dfs)):
        graphs.rates_graphs(config.SURVEY_DIR, config.COLS_NAMES[i], rates_dfs[i])
        rates_dfs[i].to_excel(excel, sheet_name=config.COLS_NAMES[i], index=False)

hibp_data = hibp_request.hibp_requests(envs.hibp_key)

hibp_db.breach_db(hibp_data)

hibp_analysis.main_hibp_analyisis()
