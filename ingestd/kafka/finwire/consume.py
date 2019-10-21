from __future__ import absolute_import

from confluent_kafka_helpers.consumer import AvroLazyConsumer
from ingestd.kafka.finwire.utils import retrieve
from confluent_kafka import avro

sec = avro.loads("""{"namespace":"ingestd.schema_registry.schemas","type":"record","name":"finwiresec","fields":[{"name":"PTS","type":["string","null"]}, {"name":"REC_TYPE","type":["string","null"]},{"name":"SYMBOL","type":["string","null"]},{"name":"ISSUE_TYPE","type":["string","null"]},{"name":"STATUS","type":["string","null"]},{"name":"NAME","type":["string","null"]},{"name":"EX_ID","type":["string","null"]},{"name":"SH_OUT","type":["int","null"]},{"name":"FIRST_TRADE_DATE","type":["int","null"]},{"name":"FIRST_TRADE_EXCHG","type":["int","null"]},{"name":"DIVIDEND","type":["int","null"]},{"name":"CO_NAME_OR_CIK","type":["string","null"]}]}""")


def consume(topic):
    print("Consuming records from topic {} with group {}.".format(topic, conf['group_id']))

    conf = retrieve("confs/finwire.yaml", "sec")["consumer"]
    key_schema=avro.loads("""{"namespace":"ingestd.schema_registry.keys","type":"record","name":"finwireSECkey",
    "fields":[{"name":PTS","type":"string"},{"name":"rec_type", "type":"string"},{"name":"
    """)

    consumer = AvroLazyConsumer(**conf, schema_registry="http://localhost:8081",
                                reader_key_schema=
                                reader_value_schema=
    )
