"""module to display the value of X-Request-Id in the response header"""

#!/usr/bin/python3

import requests
import sys

page = sys.argv[1]
req = requests.get(page)
print(req.headers["X-Request-Id"])
