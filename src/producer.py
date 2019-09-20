#!/usr/bin/env python

import csv
from os import getenv

import boto3
import confluent_kafka as kafka
from typing import NamedTuple

aws_config = dict(service_name='s3',
                  region='us-west-2',
                  aws_secret_access_key=getenv('SECRET_ACCESS_KEY'),
                  aws_access_key_id=getenv('SECRET_ACCESS_ID'),
                  aws_session_token=getenv('SESSION_TOKEN')
                  )
resource = boto3.resource('s3')



def enumerate_keys(bucket, prefix="") -> str:
    """
    Yield keys
    :param bucket: bucket name as string
    :param prefix: prefix string
    :return: generator object
    """
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    kwargs = {'Bucket': bucket}
    if isinstance(prefix, str):
        prefixes = (prefix,)
    else:
        prefixes = prefix
    for key_prefix in prefixes:
        kwargs['Prefix'] = key_prefix
        for page in paginator.paginate(**kwargs):
            try:
                contents = page['Contents']
                for meta in contents:
                    yield meta['Key']
            except KeyError as e:
                print('Key not found.')



def stream_file(conf):
    """
    :param kwargs:
    :return: yield stream
    """
    for file in enumerate_keys(**conf):
        with open(file, 'rb') as data:
            reader = csv.reader(data)
            fields = reader.__iter__()
            StreamRecord = NamedTuple("StreamRecord_", fields)
            for row in map(StreamRecord._make, reader):
                print(row)
                yield row


conf = {"bootstrap_servers": "kafka1"}

p = kafka.Producer(**conf)
for record in stream_file(conf):
    p.poll(0)
    p.produce(topic, data.encode('utf-8'))
    p.flush()


def publish(producer_instance, topic, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')

        producer_instance.send(topic, key_bytes, value_bytes)
        producer_instance.flush()
    except Exception as e:
        print('Exception while publishing')
        print(str(e))
