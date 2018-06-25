## 简介
慕课网 中小企业自动化运维架构 实战课程里相关的代码

## 目录结构

	|____.gitignore							#git配置文件
	|____chapter02							#第二章实战相关的代码
	| |____centos7_install_zabbix.sh		#centos7安装zabbix server脚本
	| |____init_flask.yml					#ansible-playbokk 初始化安装flask
	| |____install.sh						#centos7安装zabbix agent脚本
	| |____install_zabbix.yml				#ansible-playbokk 初始化安装zabbix
	| |____stop_firewall.sh					#关闭centos7防火墙脚本
	|____chapter03							#第三章实战相关的代码
	| |____centos7_install_zabbix.sh		#centos7安装zabbix server脚本
	| |____zabbix_debug_log.py				#zabbix python SDK定义输入日志格式
	| |____zabbix_http_api.py				#python 调用zabbix http api 获取主机列表
	| |____zabbix_sdk_login.py				#zabbix python SDK 获取zabbix主机列表
	|____chapter04							#第四章实战相关的代码
	| |____read_ansible_log.py				#读取ansible日志，存入ELK
	| |____read_zabbix_history.py			#读取zabbix日志，存入ELK
	| |____run_es_kibana.sh					#启动 ES 和 Kibana的脚本
	| |____test.conf						#logstash配置文件
	| |____test_data.py						#生成测试数据的脚本
	|____chapter05							#第五章实战相关的代码
	| |____add_vm.py						#python 调用jumpserver API添加主机代码
	| |____install_jumpserver.sh			#centos7 安装jumpserver脚本呢
	|____chapter06							#第六章实战相关的代码
	| |____jenkins							#持续集成的Python Web项目
	| | |____jenkins.py						#Python web项目业务代码
	| | |____test							#Python web项目测试代码
	| | | |____test_jenkins.py				#测试业务逻辑的Testcase
	|____README.md							#项目说明文件