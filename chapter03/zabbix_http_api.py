#coding=utf-8

import requests
import json

class ZabbixAPI(object):
    def __init__(self):
        self.url = 'http://13.94.56.46/zabbix/api_jsonrpc.php'
        self.headers = {'Content-Type': 'application/json-rpc'}

    def login(self):
        params = {
                  "jsonrpc": "2.0",
                  "method": "user.login",
                  "params": {
                      "user": "Admin",
                      "password": "112233qqww"
                  },
                  "id": 1,
                  "auth": None
              } 
        r = requests.post(self.url, data=json.dumps(params), headers=self.headers)
        print(r.json())

    def get_hosts(self):
        token = 'e54a44945a32c94651ca29f107461100'
        params = {
                  "jsonrpc": "2.0",
                  "method": "host.get",
                  "params": {
                      "output": [
                          "hostid",
                          "host"
                      ],
                      "selectInterfaces": [
                          "interfaceid",
                          "ip"
                      ]
                  },
                  "id": 2,
                  "auth": token
              } 
        r = requests.get(self.url, data=json.dumps(params), headers=self.headers)
        print(r.text)
              
test = ZabbixAPI()
test.get_hosts()
