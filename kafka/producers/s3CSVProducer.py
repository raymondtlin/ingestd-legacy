#!/usr/bin/env python
import csv
from io import StringIO
from boto3 import client
from conf.kafka import producerConfig, bucketConfig
from confluent_kafka import Producer

# Init client connection
s3Client = client('s3')

# Iterate over keys
for obj in s3Client.list_objects_v2(**bucketConfig).get('Contents'):
    if obj['Size'] <= 0:
        continue

    print(obj['Key'])

    # Submit S3 Select Request
    r = s3Client.select_object_content(
        Bucket='rtlmimic',
        Key=obj['Key'],
        ExpressionType='SQL',
        Expression=u'select * from s3object',
        InputSerialization={'CSV': {'RecordDelimiter': '\n',
                                    'FieldDelimiter': ',',
                                    'QuoteCharacter': '"'},
                            'CompressionType': 'GZIP'},
        OutputSerialization={'JSON': {'RecordDelimiter': '\n'}}
    )


# Retrieve payload

def stream_file(resp) -> list(dict):
    """
    Generates a stream of k:v pairs corresponding to the csv column and value
    :param resp: instance of response to select object request
    :return:
    """
    for msg in r['Payload']:
        if 'Records' in msg:
            records = msg['Records']['Payload'].decode('utf-8')

            payloads = (''.join(r for r in records))

            rdr = csv.reader(StringIO(payloads))

            for row in rdr:
                yield row


def init_producer(kafka_conf):

    return Producer(**kafka_conf)


p = init_producer(kafkaConfig)

for record in stream_file(r):
    p.produce(topic='mimic',
              value=record)

    p.poll(10)
    p.flush()

