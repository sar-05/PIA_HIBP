#!/usr/bin/env python
from os import getenv
from dotenv import load_dotenv
from requests import get

load_dotenv('.env')
hibp_key = getenv('HIBP_KEY')

headers = {
    'hibp-api-key':hibp_key,
    'user-agent':'py script',
    'accept' : 'application/json'
}

def hibp(email, headers=headers):
    endpoint = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'
    status_code=get(endpoint, headers=headers).status_code
    if status_code == 200:
        return True
    elif status_code == 404:
        return False
    else:
        return None
