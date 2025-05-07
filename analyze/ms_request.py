import requests

def ms_excel_request(item_id, worksheet_id, access_token, address="'G2:AK1048576'"):
    graph_url = "https://graph.microsoft.com/v1.0/"
    service = f"me/drive/items/{item_id}/workbook/worksheets/{worksheet_id}/"
    excel_range = f"range(address={address})/usedRange?$select=text"
    headers = {'Authorization': f'Bearer{access_token}'}
    endpoint = f"{graph_url}{service}{excel_range}"
    response = requests.get(endpoint, headers=headers)
    data = response.json()
    return data['text']
