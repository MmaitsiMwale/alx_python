#!/usr/bin/python3

"""module that takes in a URL and an email address, sends a POST 
request to the parsed URL with the email as the parameter"""

import requests
import sys


def post(url, email):
    """sends a POST request to url with email as data"""
    try:
        r = requests.post(url, data=email)
        if r.status_code:
            return f"Email: {email}"
    except requests.exceptions.HTTPError as error:
        error = str(error).split(':')[-1].strip()
        return f"Something is not working: {error}"


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = sys.argv[2]
        # check for valid input
        assert len(sys.argv) == 3, "Invalid number of arguments."
        success = post(url, email)
        print(success)
    except Exception:
        print(f"Error--> Correct Usage: <./program.py> <url> <email>")
