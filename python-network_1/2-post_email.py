"""module that takes in a URL and an email address, sends a POST request
    to the parsed URL with the email as the parameter and finally displays
    the body of the response
"""

import requests
import sys

"""function that takes in url string and then uses it to send email"""
try:
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data=email)
    if r.status_code:
        print(f"Your email is: {email}")
except Exception as error:
    print("Something is not working")
