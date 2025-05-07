#!/usr/bin/env python
import os
from dotenv import load_dotenv
from pia_hibp.api_requests.ms_request import ms_excel_request
from pia_hibp.api_requests.ms_auth import ms_graph_token

load_dotenv('.env')
app_id = os.getenv('APPLICATION_ID')
tenant_id = os.getenv('TENANT_ID')
item_id = os.getenv('ITEM_ID')
az_scopes = ['Files.Read']

token = ms_graph_token(app_id, tenant_id, az_scopes)
ms_excel_request(item_id, token)

