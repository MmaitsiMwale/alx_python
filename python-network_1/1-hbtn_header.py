"""module to display the value of X-Request-Id in the response header"""


import requests
import sys

"""collect the first argument and use it as a url"""
page = sys.argv[1]
req = requests.get(page)
try:
    print(req.headers["X-Request-Id"])
except Exception as _:
    print(None)
