import parameters
from boto3 import client
import json

sm_client = client('secretsmanager')

response = sm_client.get_secret_value(SecretId='ingestd/twitter_api_key')['SecretString']
secrets = json.dumps(response)

