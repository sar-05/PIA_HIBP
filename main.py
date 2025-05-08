#!/usr/bin/env python
from pia_hibp.setup.envs import *
from pia_hibp.setup.ms_auth import ms_graph_token
from pia_hibp.api_requests.ms_request import ms_excel_request
from pia_hibp.analyze.pd_analysis import df_create, add_hibp_cols

#Creation of authorization token
token = ms_graph_token(app_id)

#Use of token to GET request spreadsheet from cloud to RAW dir
ms_excel_request(item_id, token)

# Creation of dataframe
df = df_create()

#Creation of hibp_key cells
add_hibp_cols(df, hibp_key)

#Test print
print(df)
