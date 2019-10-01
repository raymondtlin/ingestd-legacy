FROM confluentinc/cp-kafka-connect-base:5.3.1

RUN confluent-hub install --no-prompt debezium/debezium-connecter-mysql:0.9.5 \
 && confluent-hub install --no-prompt debezium/debezium-connecter-postgresql:0.9.5 \ 
 && confluent-hub install --no-prompt confluentinc/kafka-connect-s3-source:1.0.1 \ 
 && confluent-hub install --no-prompt confluentinc/kafka-connect-avro-converter:5.3.1 \
 && confluent-hub install --no-prompt confluentinc/connect-transforms:1.2.1

# docker-machine create --driver amazonec2 --amazonec2-region us-west-2 \
	--amazonec2-open-port 8081,8088 ingestd-connect

# docker run 

