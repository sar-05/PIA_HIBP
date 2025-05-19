from collections import Counter
import re

from pia_hibp import config

def only_year(date):
    pattern = re.compile(r'^(\d{4})-\d{2}-\d{2}$')
    mo = pattern.match(date)
    if mo:
        return mo.group(1)

def breach_db(data):
    count_dict = {}
    date_list = []
    classes_list = []
    for element in data:
        count_dict[element.get("Name")] = element.get("PwnCount")
        date_list.append(only_year(element.get("BreachDate")))
        classes_list.extend(element.get("DataClasses", []))
    date_dict = Counter(date_list)
    sorted_years = sorted(date_dict.items())
    with open(config.HIBP_TXT, "w") as file:
        file.write("Breaches by name and number of accounts:\n")
        file.write(str(count_dict) + '\n')
        file.write("Breaches by date:\n")
        file.write(str(sorted_years) + '\n')
        file.write("Data types leaked:\n")
        file.write(str(Counter(classes_list)) + '\n')
