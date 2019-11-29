from flask import Flask, render_template
from kafka import KafkaConsumer
from json import loads
import pandas as pd
import csv
import threading
import atexit


POOL_TIME = 5 #Seconds

list = []
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
consumerThread = threading.Thread()

def create_app():
    app = Flask(__name__,template_folder='templates')

    def interrupt():
        global consumerThread
        consumerThread.cancel()

    def consume():
        global commonDataStruct
        global consumerThread
        with dataLock:
            consumer = KafkaConsumer(
                'story',
                 bootstrap_servers=['localhost:9092'],
                 auto_offset_reset='earliest',
                 enable_auto_commit=True,
                 group_id='FlaskConsumer',
                 value_deserializer=lambda x: loads(x.decode('utf-8')))
            for message in consumer:
                message = message.value
                print ('{} added.'.format(message))
                list.append((message.get("id"),message.get("title"),message.get("by"),message.get("time")))
            consumer.close()
        consumerThread = threading.Timer(POOL_TIME, consume, ())
        consumerThread.start()

    def consumeStart():
        global consumerThread
        # Create thread
        consumerThread = threading.Timer(POOL_TIME, consume, ())
        consumerThread.start()

    # Initiate
    consumeStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app

app = create_app()


@app.route("/")
def hello():
    global list
    return render_template('index.html', list=list)


if __name__ == "__main__":
    app.run()
