cd /usr/local/elk/elasticsearch
ES_JAVA_OPTS="-Xms512m -Xmx512m" ./bin/elasticsearch -d
cd /usr/local/elk/kibana
nohup ./bin/kibana -H 0.0.0.0 &> run.log &
