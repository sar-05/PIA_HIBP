import requests
from ms_auth import ms_graph_token
import os
from dotenv import load_dotenv

load_dotenv('.env')
app_id = os.getenv('APPLICATION_ID')
tenant_id = os.getenv('TENANT_ID')
 
endpoint = 'https://graph.microsoft.com/v1.0/me'
authority_url = f'https://login.microsoftonline.com/{tenant_id}'
az_scopes = ['User.Read', 'Files.Read']

access_token = ms_graph_token(app_id, authority_url, az_scopes)
#Request to graph API
headers = {'Authorization': f'Bearer{access_token}'}
# headers = {'Authorization': 'Bearer' + access_token}
response = requests.get(endpoint, headers=headers)
print(response)
print(response.json())
