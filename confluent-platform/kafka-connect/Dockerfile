FROM confluentinc/cp-kafka-connect-base:5.3.1

ENV plugins.path=/usr/local/share/kafka/plugins


RUN confluent-hub install --no-prompt debezium/debezium-connecter-mysql:latest
RUN confluent-hub install --no-prompt debezium/debezium-connecter-postgresql:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-s3:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-storage-common:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-avro-converter:latest
RUN confluent-hub install --no-prompt confluentinc/connect-transforms:latest
