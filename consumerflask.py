from flask import Flask
from kafka import KafkaConsumer
# from pymongo import MongoClient
from json import loads
import pandas as pd



app = Flask(__name__)

@app.route("/")
def hello():
    consumer = KafkaConsumer(
        'story',
         bootstrap_servers=['localhost:9092'],
         auto_offset_reset='earliest',
         enable_auto_commit=True,
         group_id='HNgroup',
         value_deserializer=lambda x: loads(x.decode('utf-8')))
    list=[]

    for message in consumer:
        message = message.value
        print ('{} added.'.format(message))
        list.append(message)

    return render_template('index.html', list=list)


if __name__ == "__main__":
    app.run()
