#!/usr/bin/python3
"""python scripts that fetches https://alu-intranet.hbtn.io/status"""


import requests


page = "https://alu-intranet.hbtn.io/status"
req = requests.get(page)
print(f"- type: {type(req.text)}\n- content: {req.status_code}")
