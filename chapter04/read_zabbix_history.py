#coding=utf-8

import requests
import json
import socket
import datetime

s = socket.socket()
s.connect(('192.168.1.55', 12345))

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

    def get_history(self):
        token = 'e54a44945a32c94651ca29f107461100'
        params = {
                  "jsonrpc": "2.0",
                  "method": "history.get",
                  "params": {
                      "output": "extend",
                      "history": 0,
                      "itemids": "28288",
                      "sortfield": "clock",
                      "sortorder": "DESC",
                      "limit": 100
                  },
                  "id": 2,
                  "auth": token
              } 
        r = requests.get(self.url, data=json.dumps(params), headers=self.headers)
        for one in r.json()['result']:
            one['clock'] = datetime.datetime.fromtimestamp(int(one['clock'])-8*3600).isoformat()
            one['value'] = float(one['value'])
            s.send((json.dumps(one)+'\r\n').encode('utf-8'))
              
test = ZabbixAPI()
test.get_history()
s.close()
