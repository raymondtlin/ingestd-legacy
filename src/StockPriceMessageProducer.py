from boto3 import client
import json
import requests
import confluent_kafka as kafka


sm_client = client('secretsmanager')
secrets = {
    'ALPHAVANTAGE_ACCESS_KEY':json.loads(sm_client.get_secret_value(SecretId='alphavantage')['SecretString'])['api']
}

time_series, symbol, interval ='INTRADAY', 'SPY', '5min'

def create_timeseries_url(time_series, symbol, interval, outputsize, *args, **kwargs) -> str:
    """
    param: time_series: string
    param: symbol: string
    param: interval: string (1min,5min,15min,30min,60min)
    param: outputsize: string (full, compact)
    return: url: string
    """
    
    
    baseURL = f'https://www.alphavantage.co/query?'
    url =  baseURL + f'function=TIME_SERIES_{time_series}'
    url += f'&symbol={symbol}'
    url += f'&interval={interval}'
    url += f'&outputsize={outputsize}'
    url += f'&apikey={secrets["ALPHAVANTAGE_ACCESS_KEY"]}'
    
    return url

from io import StringIO

response = requests.get(create_timeseries_url(time_series='INTRADAY',
                                              symbol='SPY',
                                              interval='1min',
                                              outputsize='compact')
                                              )

alphavantage = kafka.AvroProducer(config=conf.alphavantage.properties)

value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)

value = {"name": "Value"}
key = {"name": "Key"}

avroProducer = AvroProducer({
    'bootstrap.servers': 'mybroker,mybroker2',
    'schema.registry.url': 'http://schema_registry_host:port'
    }, default_key_schema=key_schema, default_value_schema=value_schema)

avroProducer.produce(topic='my_topic', value=value, key=key)
avroProducer.flush()

        
            