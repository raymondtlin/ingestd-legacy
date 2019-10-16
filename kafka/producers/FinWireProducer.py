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

field_widths = {"SEC": (15, 3, 15, 6, 4, 70, 6, 13, 8, 8, 12),
                "FIN": (15, 3, 4, 1, 8, 8, 17, 17, 12, 12, 12, 17, 17, 17, 26, 150),
                "CMP": (15, 3, 60, 10, 4, 2, 4, 8, 80, 80, 12, 25, 20, 24, 46, 150)}


def create_parser(fieldwidths):
    # https://stackoverflow.com/a/4915359
    """
    Constructs a tuple of fieldwidths to parse fixedwidth records
    :param fieldwidths:
    :return:
    """
    cuts = tuple(cut for cut in accumulate(abs(fw) for fw in fieldwidths))
    pads = tuple(fw < 0 for fw in fieldwidths)
    flds = tuple(zip_longest(pads, (0,) + cuts, cuts))[:-1]
    parse = lambda line: tuple(line[i: j] for pad, i, j in flds if not pad)

    parse.size = sum(abs(fw) for fw in fieldwidths)
    parse.fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)

    return parse


def find_type(record):
    """
    Searches for the 3 character document type in the record
    :param :
    :return:
    """
    token = compile(r'(SEC|CMP|FIN)')

    return findall(token, record)[0]


def generate_payload(file_path: str):
    """
    Opens a fs handle to specified path.  Reads each line in the flatfile.  Determines type of record.
    Parses fixed width values according to record type.
    :param file_path: string
    :return:
    """
    with open(file_path) as handle:
        for line in handle.readlines():
            p = create_parser(field_widths.get(find_type(line)))(line)
            yield (find_type(line), p)


secProducer = AvroProducer(**producerConfig, default_value_schema=avro.load(Path('schema_registry/schemas/finwiresec.avsc')))
finProducer = AvroProducer(**producerConfig, default_value_schema=avro.load(Path('schema_registry/schemas/finwirefin.avsc')))
cmpProducer = AvroProducer(**producerConfig, default_value_schema=avro.load(Path('schema_registry/schemas/finwirecmp.avsc')))


finSchema = JSONSchema('../schema_registry/schemas/finwirefin.json')
cmpSchema = JSONSchema('../schema_registry/schemas/finwirecmp.json')
secSchema = JSONSchema('../schema_registry/schemas/finwiresec.json')


def stream_flatfile(file_path):
    """
    Creates a filesystem handle on a local file.  Generates a list of fields.
    :param str: file_path
    :return:
    """
    with open(file_path, 'r') as handle:
 		yield handle.read()

def callback(err, msg):
	if err is not None:
		print(f"Failed to deliver message: {err}")
	else:
		print("Produced record to topic {msg.topic} partition [{msg.partition}] @ offset {msg.offset}"



# Route message production based on doc type
for file_path in Path('data/tpcdi/').glob('FINWIRE*'):
    for rec_type, record in generate_payload(file_path):
        record_key = "{uuid4()}" + str(msg.timestamp())
    
    	if rec_type == 'SEC':
            secProducer.produce(topic='finwireSEC')
    	elif rec_type == 'CMP':
    	    cmpProducer.produce(topic='finwireCMP')
        elif rec_type == 'FIN':
    	    finProducer.produce(topic='finwireFIN')
        else:
            print("Record is neither SEC, CMP, or FIN")
            raise BaseException
