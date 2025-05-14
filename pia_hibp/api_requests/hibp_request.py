import requests
from time import sleep

def hibp_requests(hibp_key, email=None):
    headers = {
            'hibp-api-key':hibp_key,
            'user-agent':'py script',
            'accept' : 'application/json'
             }
    url = f'https://haveibeenpwned.com/api/v3/'
    if email is None:
        endpoint= f"{url}breaches"
        response = requests.get(endpoint, headers=headers)
        try:
            data = response.json()
        except AttributeError as e:
            print(f"Invalid GET request {e}")
        else:
            return data
    else:
        endpoint= f"{url}breachedaccount/{email}"
        acum = 0
        response = requests.get(endpoint, headers=headers)
        status_code = response.status_code
        if status_code == 200:
            return (True, len(response.json()))
        elif status_code == 404:
            return (False, 0)
        elif status_code == 429 and acum < 5:
            acum += 1
            sleep(6)
            return hibp_requests(hibp_key, email=email)
