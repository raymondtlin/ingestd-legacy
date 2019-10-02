import boto3
from conf.rds import rds

# set clients
s3 = boto3.client('s3') 
rds_client = boto3.client('rds-data')

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
            


query = u"SELECT table_name, column_name, data_type"
query += u"FROM information_schema.columns"
query += u"WHERE table_catalog = 'public'"


schema = TableSchema(query)

table_schema = DefaultDict(List)

fields = []
for table_name, column_name, data_type in schema:
    for tbl in set(table_name):
        fields.append({"field_name":column_name,"field_type":data_type}) 