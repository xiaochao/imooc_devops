setenforce 0  # 可以设置配置文件永久关闭
systemctl stop iptables.service
systemctl stop firewalld.service

localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
echo 'LANG="zh_CN.UTF-8"' > /etc/locale.conf

yum -y install wget sqlite-devel xz gcc automake zlib-devel openssl-devel epel-release git

mkdir download && cd download
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
tar xf Python-3.6.5.tar.xz  && cd Python-3.6.5
./configure --prefix=/usr/local/python && make && make install

echo 'export PATH=/usr/local/python/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

cd /opt && git clone --depth=1 https://github.com/jumpserver/jumpserver.git && cd jumpserver && git checkout master
cd requirements && yum -y install $(cat rpm_requirements.txt)  && /usr/local/python/bin/pip3 install -r requirements.txt

yum -y install redis && systemctl start redis && yum -y install mariadb mariadb-devel mariadb-server && systemctl enable mariadb && systemctl start mariadb
mysql -uroot -e "create database jumpserver default charset 'utf8';grant all on jumpserver.* to 'jumpserver'@'127.0.0.1' identified by 'aabbcc';flush privileges;"

cd /opt
git clone https://github.com/jumpserver/coco.git && cd coco && git checkout master && cd /opt/coco/requirements && yum -y  install $(cat rpm_requirements.txt) && /usr/local/python/bin/pip3 install -r requirements.txt

