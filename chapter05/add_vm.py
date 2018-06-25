#coding=utf-8

import requests
import json

token = '4ed7b7cdd47d7a3617cb14cdb740b0fd9c9d97da'
header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-CSRFToken': 'ePQdasmlAI4y6ASA2A2nbrx01bgAzJWg6dryB8IZlW5FEK9nrCDZIDXfkEe7F56D',
    'Authorization': 'Token '+token
}

params = {
  "ip": "192.168.1.1",
  "hostname": "mukkee",
  "port": 22,
  "platform": "Linux",
  "is_active": True,
  "public_ip": "9.9.9.9",
  "admin_user": "b3c9702d-680a-4851-8f83-a7d28a05fa89",
  "nodes": [
    "92f83f8d-10fc-4b68-a6c0-1aab01c29e41"
  ],
} 

url = 'http://192.168.1.55/api/assets/v1/assets/'

r = requests.post(url, data=json.dumps(params), headers=header)

print(r.status_code, r.text)
