#coding=utf-8

from pyzabbix import ZabbixAPI

zapi = ZabbixAPI('http://13.94.56.46/zabbix')
zapi.login('Admin', '112233qqww')
for h in zapi.item.get(output='extend'):
    print(h)
