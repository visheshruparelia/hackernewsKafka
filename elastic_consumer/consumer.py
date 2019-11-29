from kafka import KafkaConsumer
from json import loads
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

consumer = KafkaConsumer(
    'story',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='ElasticConsumer',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message=message.value
    # message=json.dumps()
    # print(message)
    id = message['id']
    es.index(index='hn_story', doc_type='test', id=id, body=message)
    print('{} indexed.'.format(id))
