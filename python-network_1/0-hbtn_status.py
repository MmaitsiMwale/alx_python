#!/usr/bin/python3
"""python scripts that fetches https://alu-intranet.hbtn.io/status"""


import requests


page = "https://alu-intranet.hbtn.io/status"
req = requests.get(page)
if req.status_code == 200:
    print(f"Body response:\n\t- type: {type(req.text)}\n\t- content: OK")
