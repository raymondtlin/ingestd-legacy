from __future__ import absolute_import

from pathlib import Path
from os import getcwd
from re import compile, findall
from uuid import uuid4
from confluent_kafka.avro import AvroProducer, load
from itertools import zip_longest, accumulate


root_dir = Path(getcwd())
schema_dir = root_dir / "schema_registry" / "schemas"

field_widths = {"SEC": (15, 3, 15, 6, 4, 70, 6, 13, 8, 8, 12),
                "FIN": (15, 3, 4, 1, 8, 8, 17, 17, 12, 12, 12, 17, 17, 17, 26, 150),
                "CMP": (15, 3, 60, 10, 4, 2, 4, 8, 80, 80, 12, 25, 20, 24, 46, 150)}


def create_parser(fieldwidths: tuple):
    # https://stackoverflow.com/a/4915359
    """
    Constructs a tuple of fieldwidths to parse fixed-width records
    :param: fieldwidths: tuple of field-lengths + pad-lengths to split line by
    :return: parsed line as List[string]
    """
    cuts = tuple(cut for cut in accumulate(abs(fw) for fw in fieldwidths))
    pads = tuple(fw < 0 for fw in fieldwidths)
    flds = tuple(zip_longest(pads, (0,) + cuts, cuts))[:-1]
    parse = lambda line: tuple(line[i: j] for pad, i, j in flds if not pad)

    parse.size = sum(abs(fw) for fw in fieldwidths)
    parse.fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)

    return parse


def find_type(record: str) -> str:
    """
    Searches for the 3 character document type in the record
    :param: a read-line
    :return: three character token from the set (SEC,CMP,FIN)
    """
    token = compile(r'(SEC|CMP|FIN)')

    # return first match only
    matched_type = findall(token, record)[0]

    if matched_type in ['SEC', 'CMP', 'FIN']:
        return matched_type
    else:
        print('Invalid return value from find_type method.')
        raise ValueError


def stream_flatfile(fpath: str):
    """
    Creates a filesystem handle on a local file.  Generates a list of fields.
    :param fpath: str
    :return:
    """
    with open(fpath, 'r') as handle:
        yield handle.read()


def generate_payload(fpath: str):
    """
    Opens a fs handle to specified path.  Reads each line in the flatfile.  Determines type of record.
    Parses fixed width values according to record type.
    :param fpath: str
    :return: yields record token, and parsed record
    """
    try:
        for line in stream_flatfile(fpath):
            p = create_parser(field_widths.get(find_type(line)))(line)
            yield(find_type(line), p)
    except BaseException as e:
        print("Exception in generate_payload execution: {0}".format(e),
              e.args)


def ackback(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}, Error: {1}".format(msg.value(), err.str()))
    else:
        print("Produced record to topic {0} partition [{1}] @ offset {2}".format(msg.topic(), msg.partition(), msg.offset()))


config = {
    "bootstrap.servers": "localhost:9092",
    "schema.registry.url": "http://127.0.0.1:8081",
    "linger.ms": 50
}

p = AvroProducer(config=config)

# Route message production based on doc type
for file_path in Path('/data/').glob('FINWIRE*[1234]'):

    for rec_type, record_value in generate_payload(file_path.__str__()):

        record_key = str(uuid4())
        topic_subject = "finwire{0}".format(rec_type)
        record_schema = load((schema_dir / ('finwire{0}.avsc'.format(rec_type.lower()))).as_posix())

        try:
            p.produce(topic=topic_subject, key=record_key, value=record_value,
                      value_schema=record_schema, callback=ackback)
            p.poll(.25)
        except RuntimeError as e:
            print("Runtime Error: {}".format(e))
    print("Completed file {}".format(file_path.as_posix()))

p.flush()