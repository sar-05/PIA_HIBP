#!/usr/bin/env python

from os import write
import pandas as pd
import matplotlib.pyplot as plt

from pia_hibp.analyze.category_analysis import analyze_by_answer
from pia_hibp.setup.envs import *
from pia_hibp.config import *
from pia_hibp.setup.ms_auth import ms_graph_token
from pia_hibp.api_requests.ms_request import ms_excel_request
from pia_hibp.analyze.pd_analysis import *
from pia_hibp.visualize.graphs import create_pie_graph

#Creation of authorization token
token = ms_graph_token(app_id)

#Use of token to GET request spreadsheet from cloud to RAW dir
ms_excel_request(item_id, token)

# Creation of main dataframe
df = df_create(EXCEL_PATH, EXCEL_MAIN_COLS_RANGE, EXCEL_MAIN_COLS_NAME)

#Creation of hibp_key cells
add_hibp_cols(df, hibp_key)

df.to_excel(PROCESSED_DIR / "analysis.xlsx", index=False)

for col in ANALYSIS_COLS:
    fig = create_pie_graph(col, analyze_by_answer(df, col))
    fig.savefig(f"{PROCESSED_DIR}/{col}.png", dpi=300)
    plt.close(fig)
