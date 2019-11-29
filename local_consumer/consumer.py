from kafka import KafkaConsumer
# from pymongo import MongoClient
from json import loads
import pandas as pd
import json

consumer = KafkaConsumer(
    'story',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='CSVConsumer',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    df=pd.DataFrame({'id':[message['id']],'title':[message['title']],'by':[message['by']],'time':[message['time']]})
    with open('consumerdata.csv', 'a') as f:
        df.to_csv(f, header=False,index=False)
    print('{} added.'.format(message))
