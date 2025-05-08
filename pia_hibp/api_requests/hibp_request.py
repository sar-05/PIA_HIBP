#!/usr/bin/env python
from requests import get
from time import sleep

def hibp_breaches(email, hibp_key):
    headers = {
        'hibp-api-key':hibp_key,
        'user-agent':'py script',
        'accept' : 'application/json'
    }
    endpoint = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    response=get(endpoint, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        return (True, len(response.json()))
    elif status_code == 404:
        return (False, 0)
    elif status_code == 429:
        sleep(6)
        return hibp_breaches(email, hibp_key)
