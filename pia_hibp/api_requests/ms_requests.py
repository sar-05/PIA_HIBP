import requests

def excel_request(survey_path, item_id, token):
    endpoint = f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}/content"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        with open(survey_path, "wb") as file:
            file.write(response.content)
        print("File downloaded successfully!")
    else:
        print(f"Error code: {response.status_code}")
        print(f"Error description: {response.text}")
