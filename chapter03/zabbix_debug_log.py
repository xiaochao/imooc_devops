#coding=utf-8

import sys
import logging
from pyzabbix import ZabbixAPI

#stream = logging.StreamHandler(sys.stdout)
#stream.setLevel(logging.DEBUG)
#
#log = logging.getLogger('pyzabbix')
#log.addHandler(stream)
#log.setLevel(logging.DEBUG)

zapi = ZabbixAPI('http://13.94.56.46/zabbix')
zapi.login('Admin', '112233qqww')
