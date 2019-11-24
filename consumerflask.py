from flask import Flask, render_template
from kafka import KafkaConsumer
# from pymongo import MongoClient
from json import loads
import pandas as pd



app = Flask(__name__, template_folder='templates')

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
    i=0

    for message in consumer:
        message = message.value
        i=i+1
        print ('{} added.'.format(message))
        list.append(message)
        if(i==10):
            break
    print(i)

    return render_template('index.html', list=list)


if __name__ == "__main__":
    app.run()
