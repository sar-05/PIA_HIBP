import requests
import os
from pia_hibp.config import EXCEL_PATH

def ms_excel_request(item_id, token):
    endpoint = f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}/content"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        with open(EXCEL_PATH, "wb") as file:
            file.write(response.content)
        print("File downloaded successfully!")
    else:
        print(f"Error code: {response.status_code}")
        print(f"Error description: {response.text}")
