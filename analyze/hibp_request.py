#!/usr/bin/env python
from os import getenv
from dotenv import load_dotenv
from requests import get
from time import sleep

load_dotenv('.env')
hibp_key = getenv('HIBP_KEY')

headers = {
    'hibp-api-key':hibp_key,
    'user-agent':'py script',
    'accept' : 'application/json'
}

def hibp_breaches(email, headers=headers):
    endpoint = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    response=get(endpoint, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        return (True, len(response.json()))
    elif status_code == 404:
        return (False, 0)
    elif status_code == 429:
        sleep(6)
        return hibp_breaches(email)
