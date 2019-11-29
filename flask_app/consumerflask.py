from flask import Flask, render_template
from kafka import KafkaConsumer
from json import loads
import pandas as pd
import csv
import threading
import atexit


POOL_TIME = 5 #Seconds

# variables that are accessible from anywhere
list = []
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
yourThread = threading.Thread()

def create_app():
    app = Flask(__name__,template_folder='templates')

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
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
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app

app = create_app()


# app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():

    # list=[]
    # i=0
    #
    # for message in consumer:
    #     message = message.value
    #     i=i+1
    #     print ('{} added.'.format(message))
    #     list.append(message)
    #     if(i==10):
    #         break
    # print(i)
    # with open('./../local_consumer/consumerdata.csv','rt')as f:
    #     data = csv.reader(f)
    #     for row in data:
    #         list.append(row)
    #
    global list
    return render_template('index.html', list=list)



if __name__ == "__main__":
    app.run()
