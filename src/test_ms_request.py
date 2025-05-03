from ms_auth import ms_graph_token
import os
from dotenv import load_dotenv
from ms_request import ms_excel_request

load_dotenv('.env')

#Variables for the token
app_id = os.getenv('APPLICATION_ID')
tenant_id = os.getenv('TENANT_ID')
az_scopes = ['User.Read', 'Files.Read', 'Files.ReadWrite']
# authority_url = f'https://login.microsoftonline.com/{tenant_id}'

#Variables for the request
item_id = os.getenv('ITEM_ID')
worksheet_id = os.getenv('WORKSHEET_ID')

access_token = ms_graph_token(app_id, tenant_id, az_scopes)
response = ms_excel_request(item_id, worksheet_id, access_token)
print(response)




#endpoint = f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}/workbook/worksheets/{worksheet_id}/range(address='H1:H5')?$select=text"

#access_token = ms_graph_token(app_id, authority_url, az_scopes)
##Request to graph API
#headers = {'Authorization': f'Bearer{access_token}'}
## headers = {'Authorization': 'Bearer' + access_token}
#response = requests.get(endpoint, headers=headers)
#print(response)
#data = response.json()
#print(data['text'])
