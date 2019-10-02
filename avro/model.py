import boto3
from fastavro import writer, parse_schema
from typing import DefaultDict, List
from conf import rds
import re



rds_client = boto3.client('rds')

class TableSchema:
    fields: list
    name:   str
    
    def __init__(self, fields, name):
        self.fields = [] or None
        self.name = name
    
    
    def fetch(self):
        """
        param: table_name: string
        """
        # Mitigate SQL injection
        if re.search('[=]|\s', self.name):
            print('Modify your parameter, it includes suspicious characters.')
            sql = None
            raise SyntaxError
        else:
            sql = f"""SELECT to_json(table_name), to_json(column_name), to_json(data_type)\
            FROM    information_schema.columns\
            WHERE   table_name = {self.name}
            """
        response = rds_client.execute_statement(sql, **rds.params)
        for record in response['records']:
            yield(record)

            
    def to_dict(self) -> DefaultDict(List):
        
        self.json_schema = {}
        
        for column_name, data_type in self.fetch():
            self.json_schema.update(
                dict(
                    {self.name: self.fields.append(
                        {"field_name":column_name,
                         "field_type": data_type}
                         )
                    })
                    )
            print(self.json_schema)
        return(self.json_schema)
    
    
    def to_avro(self, schema: DefaultDict[List]):
        
        parsed = parse_schema(schema)
        
        with open(f'{schema.name}.avsc', 'wb') as handle:
            writer(handle, parsed)
        
            
    def register_schema(self, schema):
        pass


    def store_in_s3(self):
        pass
        

#query = u"SELECT table_name, column_name, data_type"
#query += u"FROM information_schema.columns"
#query += u"WHERE table_catalog = 'public'"