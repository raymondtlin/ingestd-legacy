FROM confluentinc/cp-kafka-connect-base:5.3.1

RUN confluent-hub install --no-prompt debezium/debezium-connecter-mysql:latest
RUN confluent-hub install --no-prompt debezium/debezium-connecter-postgresql:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-s3:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-storage-common:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-avro-converter:latest
RUN confluent-hub install --no-prompt confluentinc/connect-transforms:latest
