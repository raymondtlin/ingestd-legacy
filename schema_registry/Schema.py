from __future__ import absolute_import

import json
import re
from pathlib import Path
from typing import DefaultDict, List
from fastavro import writer, parse_schema


class Schema(object):
    # name: str
    # fields: list
    # as_dict: dict

    def __init__(self, fields=None, name=None, as_dict=None):
        self.fields = fields
        self.name = name
        self.as_dict = as_dict

    def to_avro(self):
        """
        Parses avro from json schema
        """
        parsed = parse_schema(self.as_dict)

        with open(f'{self.name}.avsc', 'wb') as handle:
            writer(handle, parsed)


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
            sql += f"WHERE table_name = {table_name}"

        response = self.client.execute_statement(sql, **config.params)
        for record in response['records']:
            yield (record)

    def to_dict(self) -> DefaultDict[List]:

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

        for field in self.as_dict['fields']:
            self.fields.append(field)