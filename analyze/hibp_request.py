import requests
import time
import os
from dotenv import load_dotenv

def have_i_been_pwned (validated_emails, headers):
    emails_to_check = validated_emails.copy()
    attempts = {}
    for email in emails_to_check:
        attempts[email] = 0

    while len(emails_to_check) > 0:
        email = emails_to_check.pop(0)
        attempts[email] += 1
        
        try:
            endpoint = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'
            response=requests.get(endpoint, headers=headers)
            status = response.status_code
            print(status)

            if status == 200:
                data=response.json()
                print("It has been breached")
                for breach in data:
                    print("Name: ", breach["Name"])
                    print("Breach date: ", breach["BreachDate"])
                    print("Tipos de datos: ", breach["DataClasses"])
                    print("Number of accounts loaded into the system: ", breach["PwnCount"])
                    print("It's unverified: ", breach["IsVerified"])
                    print("It's sensitive: ", breach["IsSensitive"])
                    print("It's sourced from malware: ",breach["IsMalware"])
                    print("Description: ", breach["Description"])
                time.sleep(6)
            elif status == 404:
                print("It has not been breached")
                time.sleep(6)
            elif status == 429:
                print("waiting 60 seconds")
                time.sleep(60)
                if attempts[email] < 5:
                    emails_to_check.insert(0,email)
                else:
                    print(f"already tried {email} 5 times")
        except requests.exceptions.ConnectionError:
            print("Couldn't connect to HIBP")
        except requests.exceptions.Timeout:
            print("The HIBP request took too long to answer")

def email_validation(email):
    email.lower()
    email.replace(" ", "")
    if email.count("@") != 1:
        return None
    else:
        email_parts = email.split("@")
        emailp1 = email_parts[0]
        emailp2 = email_parts[1]
        if len(emailp1) == 0:
            return None
        elif "." not in emailp2:
            return None
        else:
            return email
    

load_dotenv('.env')
hibp_key = os.getenv('HIBP_KEY')
#Test account with known breaches
test_pwned = os.getenv('TEST_PWNED')
test_not_pwned = os.getenv('TEST_NOT_PWNED')

headers = {
    'hibp-api-key':hibp_key,
    'user-agent':'py script',
    'accept' : 'application/json'
}

emails_list = [test_pwned, test_not_pwned, test_pwned, test_not_pwned]
validated_emails = list()
for email in emails_list:
    new_email = email_validation(email)
    if new_email is not None:
        validated_emails.append(new_email)

have_i_been_pwned(validated_emails, headers)