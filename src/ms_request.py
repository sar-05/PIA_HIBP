import requests
import os

def ms_excel_request(item_id, access_token):
    graph_url = "https://graph.microsoft.com/v1.0/"
    endpoint = f"{graph_url}me/drive/items/{item_id}/content"
    headers = {'Authorization': f'Bearer{access_token}'}
    save_location = os.getcwd()
    response = requests.get(endpoint, headers=headers)
    with open(os.path.join(save_location, "datos_encuesta.xlsx"), 'wb') as _f:
        _f.write(response.content)

print(os.path.dirname(os.getcwd()))
