#!/usr/bin/python

# basic script that uses Python requests to GET json result from REST API
# added header and API Key authentication

# import modules
import requests
import json

# required to avoid InsecureRequestWarning: Unverified HTTPS request is being made.
import urllib3

urllib3.disable_warnings()

r = requests.get('https://ptr.secureitquest.com/api/lists/5/members.json',
  headers={'Authorization': '0dba0006-294e-4dcb-988e-45b47869d7be'}, verify=False)

json_object = json.dumps(r.json(), indent=4)

print(json_object)