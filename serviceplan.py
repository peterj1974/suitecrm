import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## Global Static Variables
HOST = morpheus["morpheus"]["applianceHost"]
INTERNAL_HOST = morpheus["customOptions"]["internalHost"]
TOKEN = morpheus["morpheus"]["apiAccessToken"]
INTERNAL_URL = "https://%s" % (INTERNAL_HOST)

## Request headers
HTTP_HEADERS = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (TOKEN)}
HTTP_UPLOAD_HEADERS = {"Authorization": "BEARER " + (TOKEN)}

## Get list of AWS Plans
"https://adm-euw2-lab10.morpheus.training/api/service-plans?includeZones=true&provisionTypeId=7" \
  -H "Authorization: Bearer 0b1a1085-0a17-458b-8a9a-c8afa2050195"

url = "https://%s/api/service-plans?includeZones=true&provisionTypeId=7" % (HOST)

response = requests.get(url, headers=HTTP_HEADERS, verify=False)
data = response.json()
print(data)
