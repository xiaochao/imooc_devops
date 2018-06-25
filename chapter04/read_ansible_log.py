#coding=utf-8

import socket
import json
import os
import sys
import re

if len(sys.argv) != 2:
    print('Usage:', sys.argv[0], 'ansbile_log_path')
    sys.exit(1)

if not os.path.exists(sys.argv[1]):
    print('file', sys.argv[1], 'not exists')
    sys.exit(1)

s = socket.socket()
s.connect(('192.168.1.55', 12345))

r = re.compile(r'(?P<time>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}).*\su=(?P<user>.*)\s\|\s\s(?P<host>.*)\s\|\s(?P<status>.*)\s=>.*')

for line in open(sys.argv[1]).readlines():
    result = re.finditer(r, line)
    items = [m.groupdict() for m in result]
    if not items:
        continue
    s.send((json.dumps(items[0])+'\r\n').encode('utf-8'))
s.close()
