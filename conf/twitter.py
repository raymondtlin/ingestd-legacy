from boto3 import client
import json


sm_client = client('secretsmanager')

response = sm_client.get_secret_value(SecretId='ingestd/twitter_api_key')['SecretString']
dct = json.loads(response)

secrets = {}
keys = ['consumer_key', 'consumer_secret', 'access_token', 'access_secret']

for key in keys:
    secrets.update({f'twitter_{key}'.upper(): dct[key]})
    