#!/usr/bin/python3
"""module to display the value of X-Request-Id in the response header"""

import requests
import sys

if __name__ == "__main__":
    try:
        page = sys.argv[1]
        req = requests.get(page)
        print(req.headers["X-Request-Id"])
    except Exception as e:
        raise SystemExit('Invalid Usage.\nUsage : ./main.py <url>')
