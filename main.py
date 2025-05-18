#!/usr/bin/env python

import pia_hibp.config as config
from pia_hibp.setup import envs, ms_auth
from pia_hibp.api_requests import ms_requests
from pia_hibp.analyze import df_setup, breach_rate
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

print("Creando Dataframes de Tasas de Compromisos")
rates_dfs = []
for col in config.DEMO_COLS:
    rates_dfs.append(breach_rate.by_group(df, col))

for i in range(len(rates_dfs)):
    graphs.rates_graphs(config.PROC_DIR, config.COLS_NAMES[i], rates_dfs[i])
