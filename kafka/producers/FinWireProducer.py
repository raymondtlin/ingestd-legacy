from __future__ import absolute_import
from pathlib import Path
from os import getcwd, listdir
from re import compile, findall
from struct import Struct
from confluent_kafka import avro
schema_path = Path(getcwd(), 'avro/schemas').as_posix()
file_names = [schema for schema in listdir(schema_path) if 'finwire' in schema]
field_widths = {"SEC": (15, 3, -12, 3, 6, 4, 60, 6, 9, 17, -8, 4, 10),
                "FIN": (15, 3, 4, 60, 10, 4, 22, 4, 4, 67, 8, 4, 10),
                "CMP": (15, 3, 60, 10, 4, 5, 13, 8, 155, 12, 25, 20, 25, 90)}



for topic in topics:
    schemas[topic] = avro.loads(Path(getcwd()).joinpath('avro/schemas', topic + '.json').read_text())



def find_type(record):
    """

    :param :
    :return:
    """
    token = compile(r'(SEC|CMP|FIN)')

    return findall(token, record)


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


def readfin():
    with open('/data/finwire/FINWIRE1968Q1', 'r') as handle:
        yield(handle.readline().split())
