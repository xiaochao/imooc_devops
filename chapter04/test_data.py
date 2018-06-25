#coding=utf-8

import socket
import json
import datetime
import random

s = socket.socket()
s.connect(('192.168.1.45', 12345))

users = ['tom', 'hary', 'wada', 'dilong', 'eric', 'simon', 'sam']
pages = ['index', 'course', 'pay', 'login']
device = ['android', 'iphone', 'ipad']

line = 100
while line>0:
    line = line-1
    temp_time = (datetime.datetime.utcnow()+datetime.timedelta(seconds=random.randint(0, 10))).isoformat()
    data = {'name': random.choice(users), 'visit_time': temp_time, 'device': random.choice(device), 'page': random.choice(pages), 'num': random.randint(0, 10)}
    s.send(json.dumps(data)+'\r\n')
s.close()
