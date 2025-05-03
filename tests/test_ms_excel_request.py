from ms_auth import ms_graph_token
import os
from dotenv import load_dotenv
from ms_request import ms_excel_request

load_dotenv('.env')

#Variables for the token
app_id = os.getenv('APPLICATION_ID')
tenant_id = os.getenv('TENANT_ID')
az_scopes = ['User.Read', 'Files.Read', 'Files.ReadWrite']

#Variables for the request
item_id = os.getenv('ITEM_ID')
worksheet_id = os.getenv('WORKSHEET_ID')

access_token = ms_graph_token(app_id, tenant_id, az_scopes)
response = ms_excel_request(item_id, worksheet_id, access_token)
print(response)
