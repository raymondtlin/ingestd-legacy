
from __future__ import absolute_import
from boto3 import client
import json
import requests
from confluent_kafka import *
from conf import alphavantage
from io import StringIO

sm_client = client('secretsmanager')
secrets = {
    'ALPHAVANTAGE_ACCESS_KEY': json.loads(sm_client.get_secret_value(SecretId='alphavantage')['SecretString'])['api']
}

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



time_series, symbol, interval = 'INTRADAY', 'SPY', '5min'

response = requests.get(create_timeseries_url(time_series=time_series,
                                              symbol=symbol,
                                              interval='1min',
                                              outputsize='compact'))

key_schema = avro.loads("""{"namespace":"alphavantage","name":"ticker","type":"record",
"fields":[{"name": "timestamp", "type":"long"}]}""")

value_schema = avro.loads("""{"namespace":"alphavantage","name":"quote","type":"record",
"fields":[{"name": "1. open", "type":"double"},
           {"name": "2. high", "type":"double"},
           {"name": "3. low", "type":"double"},
           {"name": "4. close", "type":"double"},
           {"name": "5. volume", "type":"double"}]}""")

alphavantageProducer = avro.AvroProducer(alphavantage.properties,
                                          default_key_schema=key_schema,
                                          default_value_schema=value_schema
                                          )
for k,v in dict(response.json())['Time Series (1min)'].items():
    alphavantageProducer.produce(topic='my_topic', value=v, key=k)
alphavantageProducer.flush()