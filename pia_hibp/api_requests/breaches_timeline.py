#!/usr/bin/env python
import requests
from os import getenv
from dotenv import load_dotenv
import re
from collections import Counter

load_dotenv('.env')
hibp_key = getenv('HIBP_KEY')

endpoint = f"https://haveibeenpwned.com/api/v3/breaches"
headers = {
    'hibp-api-key':hibp_key,
    'user-agent':'py script',
    'accept' : 'application/json'
}

response = requests.get(endpoint, headers=headers)
data = response.json()
dates_list = []

for i in range(len(data)):
    dates_list.append(data[i]['BreachDate'])

def data_timeline(dates_list):
    pattern = re.compile(r'^(\d{4})-\d{2}-\d{2}$')
    years = []
    for date in dates_list:
        mo = pattern.match(date)
        if mo:
            year = mo.group(1)
            years.append(year)
    data = Counter(years)
    return data

data = data_timeline(dates_list)
years = list(data.keys())
years.sort()
for key in years:
    print(f"{key}:{data[key]}")
