from __future__ import absolute_import
from pathlib import Path
from os import getcwd, listdir
from re import compile, findall
from struct import Struct
from confluent_kafka.avro import AvroProducer, loads
from conf.kafka import producerConfig
from datetime import datetime
from schema_registry import Schema
from confluent_kafka.admin import AdminClient


schema_path = Path(getcwd(), 'schema_registry/schemas').as_posix()
file_names = [schema for schema in listdir(schema_path) if 'finwire' in schema]

field_widths = {"SEC": (15, 3, -12, 3, 6, 4, 60, 6, 9, 17, -8, 4, 10),
                "FIN": (15, 3, 4, 60, 10, 4, 22, 4, 4, 67, 8, 4, 10),
                "CMP": (15, 3, 60, 10, 4, 5, 13, 8, 155, 12, 25, 20, 25, 90)}


def find_type(record):
    """
    Searches for the 3 character document type in the record
    :param :
    :return:
    """
    token = compile(r'(SEC|CMP|FIN)')

    return findall(token, record)[0]


def parse_field_struct(record_type: str, record: str):
    """
    Parses fields using designated widths
    :return:
    """
    # Accounting for any padding by taking the absolute value but modifying the placeholder

    fmt = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                   for fw in field_widths.get(record_type))

    field_struct = Struct(fmt)
    parse = field_struct.unpack_from
    print('fmt: {!r}, recsize: {} chars'.format(fmt, field_struct.size))

    yield parse(record)


def stream_flatfile(file_path):
    """
    Creates a filesystem handle on a local file.  Generates a list of fields.
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as handle:
        yield(handle.readline().split())





secProducer = AvroProducer(**producerConfig)
finProducer = AvroProducer(**producerConfig)
cmpProducer = AvroProducer(**producerConfig)



sf = stream_flatfile('/home/demo/data/finwire/FINWIRE1968Q1')

# Route message production based on doc type
for record in sf:
    rec_type = find_type(record)

    parse_field_struct(rec_type, record)

    if rec_type == 'SEC':
        secProducer.produce(key_schema=sec_key_schema,
                            value_schema=sec_value_schema,
                            topic='finwiresec')
    elif rec_type == 'CMP':
        cmpProducer.produce(key_schema=cmp_key_schema,
                            value_schema=cmp_value_schema,
                            topic='finwirecmp')
    elif rec_type == 'FIN':
        finProducer.produce(key_schema=fin_key_schema,
                            value_schema=fin_value_schema,
                            topic='finwirefin')
    else:
        print("Record is neither SEC, CMP, or FIN")
        raise BaseException
