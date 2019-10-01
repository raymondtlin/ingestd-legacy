FROM confluentinc/cp-kafka-connect-base:5.3.1

RUN confluent-hub install --no-prompt debezium/debezium-connecter-mysql:latest \
 && confluent-hub install --no-prompt debezium/debezium-connecter-postgresql:latest \
 && confluent-hub install --no-prompt confluentinc/kafka-connect-s3-source:latest \
 && confluent-hub install --no-prompt confluentinc/kafka-connect-avro-converter:latest \
 && confluent-hub install --no-prompt confluentinc/connect-transforms:latest

