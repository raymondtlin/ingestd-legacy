from dataclasses import dataclass

import boto3

from conf import rds

# set clients
s3 = boto3.client('s3')
rds_client = boto3.client('rds-data')


@dataclass
class TableSchema:
    # namespace: str
    # name: str
    # type: str
    # fields: List[Field]
    # Field: NamedTuple('Field', 'field_name, field_type')
    query: str

    def fetch(self):
        sql = self.query

        response = rds_client.execute_statement(sql, **rds.params)
        for record in response['records']:
            print(record)

