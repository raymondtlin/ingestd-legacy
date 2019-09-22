#!/usr/bin/env python
import re

import boto3
import confluent_kafka as kafka

def enumerate_keys(bucket, prefix="") -> str:
    """
    Yield keys
    :param bucket: bucket name as string
    :param prefix: prefix string
    :return: generator object
    """
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    kwargs = {'Bucket': bucket,
              'Prefix': prefix}
    if isinstance(prefix, str):
        prefixes = (prefix,)
    else:
        prefixes = prefix
    for key_prefix in prefixes:
        kwargs['Prefix'] = key_prefix

        # yield ALL keys

        for page in paginator.paginate(**kwargs):
            try:
                contents = page['Contents']
                for meta in contents:
                    yield meta['Key']
            except KeyError as e:
                print('Key not found.')

def open_stream(conf):
    """
    :param: conf
    :return: yield stream
    """
    for file in enumerate_keys(bucket=conf['Bucket'],prefix=conf['Prefix']):
        if re.findall('csv', file):
            resource = boto3.resource('s3')
            response = resource.Object(conf['Bucket'], key=file).get()

            for rec in response['Body'].iter_lines():
                print(rec)

                yield (rec, file.split('/')[1])

conf={"Bucket":"ingestd-prod-raw",
      "Prefix":"sec-web-access"}
kafka_conf = {"bootstrap.servers": "kafka",}
import codecs

p = kafka.Producer(**kafka_conf)
for record in open_stream(conf):
    p.poll(1)
    p.produce(topic='sec')
p.flush()

