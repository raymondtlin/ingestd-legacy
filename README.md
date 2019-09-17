# ingestd

A framework for advancing data warehousing and governance practices.

## Ingestion Layer  

Confluent Kafka python connector to ingest data from multiple sources to raw data store in S3.

## Apache Beam Orchestration

Apache Flink Cluster will execute transformations delegated by Apache Beam.

## Metadata Lake

Metadata is catalogued when it arrives in S3 and during every transformation.  Kafka metadata producers will be used to submit metadata logs to a central metadata store.

## Data Versioning

Production data is snapshotted and retained for a designated period, allowing for persistent data versioning and data lineage.
