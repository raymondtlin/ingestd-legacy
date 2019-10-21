from __future__ import absolute_import

import json
import re
from pathlib import Path
from collections import defaultdict
from fastavro import writer, parse_schema
from confluent_kafka import avro


class Schema(object):
    # name: str
    # fields: list
    # as_dict: dict

    def __init__(self, fields=None, name=None, as_dict=None):
        self.fields = [] or fields
        self.name = name
        self.as_dict = as_dict

    def to_avro(self):
        """
        Parses avro from json schema
        """
        parsed = parse_schema(self.as_dict)

        with open('{0}.avsc'.format(self.name), 'wb') as handle:
            writer(handle, parsed)

    def register_schema(path_to_schema):
        c = avro.CachedSchemaRegistryClient('http://localhost:8081')
        schema_path = Path('schema_registry/schemas')
        for schema in path_to_schema.glob("*"):
            parsed_avro_schema = avro.loads(schema.read_text())
            subj = schema.as_posix().split("/")[-1].split(".")[0]
            c.register(avro_schema=parsed_avro_schema, subject=subj)


class DBTableSchema(Schema):
    """
    Abstraction for schema discovered by querying information_schema
    """

    def __init__(self, db_client=None, table_name=None):
        """
        :param table_name: string
        """
        super().__init__(db_client, table_name)

        from boto3 import client
        self.client = client(db_client)
        self.name = table_name

    def fetch(self, config, table_name):
        """
        :param: config: dict
        :param: table_name: string
        """
        # Mitigate SQL injection
        if re.search('[=]\s', table_name):
            print('Modify your parameter, it includes suspicious characters.')
            raise SyntaxError
        else:
            sql = "SELECT to_json(table_name), to_json(column_name), to_json(data_type)"
            sql += "FROM information_schema.columns"
            sql += "WHERE table_name = {0}".format(table_name)

        response = self.client.execute_statement(sql, **config.params)
        for record in response['records']:
            yield (record)

    def to_dict(self) -> defaultdict(list):

        for column_name, data_type in self.fetch():
            self.as_dict.update(
                dict({self.name: self.fields.append({"field_name": column_name,
                                                     "field_type": data_type})}))
            print(self.as_dict)
        return self.as_dict


class JSONSchema(Schema):

    def __init__(self, file_path):
        super().__init__(file_path)

        self.file_path = Path(file_path)
        self.as_dict = json.loads(self.file_path.read_text())

        #for field in self.as_dict['fields']:
        #    self.fields.append(field)

