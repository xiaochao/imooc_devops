rpm -ivh http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-2.el7.noarch.rpm
yum -y install zabbix-server-mysql
yum -y install zabbix-proxy-mysql
yum -y install zabbix-web-mysql
yum -y install mariadb-server
systemctl start mariadb
#mysql -uroot -e "create database zabbix"
sed  's/DBUser=zabbix/DBUser=root/g' -i /etc/zabbix/zabbix_server.conf 
zcat /usr/share/doc/zabbix-server-mysql-3.4.8/create.sql.gz | mysql -uroot zabbix
setenforce 0
systemctl start zabbix-server
