import requests
#This script should define functons to retrieve all needed data from the 
#spreadsheet.

#Those functions should recieve the access_token, endpoint and headers
#Here, validation of the output of those functions should also ne defined

def ms_excel_request(item_id, worksheet_id, access_token, adress='G2:AK1048576'):
    graph_url = "https://graph.microsoft.com/v1.0/"
    service = f"me/drive/items/{item_id}/workbook/worksheets/{worksheet_id}/"
    excel_range = f"range(address={adress})?$select=text"
    headers = {'Authorization': f'Bearer{access_token}'}
    endpoint = f"{graph_url}{service}{excel_range}"
    print("-----------------")
    print(endpoint)
    print("-----------------")
    print(type(endpoint))
    return requests.get(endpoint, headers=headers)
