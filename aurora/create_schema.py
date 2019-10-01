import boto3

s3 = boto3.client('s3')

rds = boto3.client('rds-data')

with open('create_table_ddl.sql','r') as sql:
    print(str(sql))
]