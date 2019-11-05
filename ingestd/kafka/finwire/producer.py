from itertools import zip_longest, accumulate
from ingestd.kafka.finwire import utils

from confluent_kafka import avro
from pathlib import Path
from kafkian import Producer
from kafkian.serde.serialization import (AvroSerializer,
                                         AvroStringKeySerializer,
                                         SubjectNameStrategy)
from kafkian.serde.avroserdebase import AvroRecord


class AbstractRecord(AvroRecord):
    def __init__(self, path_to_schema):
        with open(path_to_schema, 'r') as j:
            self._schema = avro.loads(j.read())

        self.fields = []

        for field in self._schema.to_json()['fields']:
            self.fields.append(field.get('name'))


def instantiate_producer(**kwargs):
    conf = utils.retrieve(kwargs['--path_to_config'], kwargs['--section'])

    producer = Producer(config=conf, key_serializer=AvroStringKeySerializer(
        schema_registry_url="http://localhost:8081"),
        value_serializer=AvroSerializer(
            schema_registry_url="http://localhost:8081",
            subject_name_strategy=SubjectNameStrategy.TopicRecordNameStrategy)
            )


def io_stream(file_path):


def produce(producer: Producer, record: AbstractRecord, **kwargs):

    for key, value in
       producer.produce(
            config=utils.retrieve(
                kwargs['--path_to_config'], kwargs['--section']),
            topic_name=kwargs['--topic'],
            num_partitions=kwargs['--partitions'],
            key=kwargs['--key'],
            value={**record}
            )


class Producer()

   def __init__(self, **kwargs) -> None:
        self.config = utils.retrieve(
            kwargs['--path_to_config'], kwargs['--section'])
        self.topic_name = kwargs['--topic']
        self.num_partitions = kwargs['--partitions']
        self.key = kwargs['--key']

        self.producer = avro.AvroProducer(self.config)
        self.source_file = kwargs['--source_file']
        self.key_schema = kwargs['--key_schema']
        self.value_schema = kwargs['--value_schema']
        self.file_extension = kwargs['--file_extension']

    def produce(self, **kwargs):
        for rec_type, record_value in utils.generate_payload(self.source_file):
            path_to_key_schema = Path(
                'ingestd/kafka/schemas') / self.key_schema
            path_to_value_schema = Path(
                'ingestd/kafka/schemas') / self.value_schema

            record_key = avro.load(path_to_key_schema.as_posix() )
            record_schema = avro.load(path_to_value_schema.as_posix())

            self.producer.produce(key=record_key, value=record_value,
                                  key_schema=record_key,
                                  value_schema=record_value)


p = avro.AvroProducer(config=utils.retrieve(
    file_path='confs/finwire.yaml', section='producer'))
   # Route message production based on doc type
for file_path in Path('/data/').glob('FINWIRE*[1234]'):
    for rec_type, record_value in utils.generate_payload(file_path.__str__()):
        topic_subject = "finwire{0}".format(rec_type)
        record_schema = avro.load(
            (schema_dir / ('finwire{0}.avsc'.format(rec_type.lower()))).as_posix())

        try:
            p.produce(topic=topic_subject,
                      value=record_value,
                      value_schema=record_schema,
                      callback=utils.ackback)
            p.poll(.25)
        except RuntimeError as e:
            print("Runtime Error: {}".format(e))
    print("Completed file {}".format(file_path.as_posix()))

p.flush()
