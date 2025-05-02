import requests
from ms_auth import ms_graph_token
import os
from dotenv import load_dotenv

load_dotenv('.env')
app_id = os.getenv('APPLICATION_ID')
tenant_id = os.getenv('TENANT_ID')
item_id = os.getenv('ITEM_ID')
worksheet_id = os.getenv('WORKSHEET_ID')

endpoint = f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}/workbook/worksheets/{worksheet_id}/range(address='H1:H5')?$select=text"
authority_url = f'https://login.microsoftonline.com/{tenant_id}'
az_scopes = ['User.Read', 'Files.Read', 'Files.ReadWrite']

access_token = ms_graph_token(app_id, authority_url, az_scopes)
#Request to graph API
headers = {'Authorization': f'Bearer{access_token}'}
# headers = {'Authorization': 'Bearer' + access_token}
response = requests.get(endpoint, headers=headers)
print(response)
data = response.json()
print(data['text'])
