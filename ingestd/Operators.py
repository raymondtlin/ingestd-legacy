from SchemaRegistryAbstraction import Schema, JSONSchema
from pathlib import Path
from confluent_kafka import Message



class Connector:
    CONFIG={}



class FlatFileConnector(Connector):
    def super().__init__(self, **kwargs):
        """
        :param str file_path:
        ;param str file_format: "fwf, csv, tsv, bar, xml"
        """
        self.file_path = kwargs['file_path']
        self.file_format = kwargs['file_format']
        self.file_type = self.file_path.split('\.')[-1]
        self.delimiter = kwargs['delimiter']


    def route():
        if self.file_format in ["csv","tsv","bar"]:
            operator = DelimiterOperator(self.delimiter)
        elif self.file_format == 'xml'
            operator = XMLOperator()
        elif self.file_format == 'fwf'
            operator = FixedWidthOperator()
        else:
            operator = StringOperator()
        return operator


class Record(FlatFileConnector):
    def __init__(self,
                 topic = None,
                 num_partitions = 1,
                 key_schema = None,
                 key = None,
                 value_schema = None,
                 value = None,
                 schema_registry_url = None,
                 iterable = None:
        self.schema_registry_url = schema_registry_url
        self.num_partitions = num_partitions
        self.topic = topic
        self.key = key
        self.value = value
        self.key_schema = key_schema
        self.value_schema = value_schema

    # Needs revision
    for schema in [self.key_schema, self.value_schema]:
        if schema:
            try:
                sch = JSONSchema(schema).to_avro()
                try:
                    sch.register(schema_registry_url=self.schema_registry_url)

                except BaseException as e:
                    print('Could not register schema in the registry', e)
                finally:
                    self.valid_schemas.append(sch)
            except Exception as e:
                print('Could not convert schema to avro')



class StringOperator:
    def __init__(self):
        pass

    def apply(record):
        yield(record)


class DelimiterOperator(FlatFileConnector):
    def __init__(self):
        pass

    def apply():
        while True:
            with open(self.file_path,'r') as stream:
                for line in stream.readlines():
                    record = Record(iterable=line.split(self.delimiter)
                    if key_schema:
                        key = record.apply(key_schema)
                    if value_schema:
                        value = record.apply(value_schema)
                    yield from record, key, value


class FixedWidthOperator(FlatFileConnector):

    def configure(**kwargs):
        CONFIG = {**kwargs}

    def apply()