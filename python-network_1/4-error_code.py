#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL 
    and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, 
    print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys


def get_url(url):
    try:
        r = requests.get(url)
        if (r.status_code >= 400):
            raise Exception('Error Code: ' + str(r.status_code))
        return r.content
    except Exception as e:
        # print("Exception Occured")
        errorMsg = str(e).split(':')[-1].strip()
        return f"Error code: {errorMsg}"


if __name__ == "__main__":
    url = sys.argv[1]
    content = get_url(url)
    # for line in iter(content):
    #     print(line)
    print(content)
