#!/usr/bin/python

# Script uses Python requests to GET json result from REST API
# import modules
import requests
import json
import urllib3  # required to avoid InsecureRequestWarning

urllib3.disable_warnings()

# Change to suit your needs
url = 'https://ptr.secureitquest.com/api/lists/5/members.json'
# I have included an additional URL below that requires a key
# url = 'https://ptr.secureitquest.com/api/lists/8/members.json'
api_key = '0dba0006-294e-4dcb-988e-45b47869d7be'

r = requests.get(url, headers={'Authorization': api_key}, verify=False)
# If you do not need authentication, comment out the above and uncomment the below.
# r = requests.get(url, verify=False)

# formats with a 4 space tab
json_object = json.dumps(r.json(), indent=4)

# outputs the results
print(json_object)