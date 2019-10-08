# ingestd - a data-warehouse integration framework

Inspired by Snowflake DB's time-travel feature enables users to reproduce data from earlier states, ingestd is a pipeline which enables data reproduceability at scale.

ingestd ingests database events by employing `Debezium's MYSQL Kafka Connector` in order to stream CDC events from the relational store.  These messages are registered in `Confluent's Schema Registry` and serialized in `Avro` format.  

A consumer reads from the CDC Kafka topic and tags each message with its appropriate version.  Additional metadata is injected at this stage in order to provide full context as to the state.

Data is then persisted to a database store and served via `Apache Superset`.
