import requests
import os
from dotenv import load_dotenv

load_dotenv('.env')
hibp_key = os.getenv('HIBP_KEY')
#Test account with known breaches
test_pwned = os.getenv('TEST_PWNED')
test_not_pwned = os.getenv('TEST_NOT_PWNED')

endpoint = f'https://haveibeenpwned.com/api/v3/breachedaccount/{test_not_pwned}'

headers = {
    'hibp-api-key':hibp_key,
    'user-agent':'py script'
}

response=requests.get(endpoint, headers=headers)
status = response.status_code
print(status)

if status == 200:
    data=response.json()
    print(data)
