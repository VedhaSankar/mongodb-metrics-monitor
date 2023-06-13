from flask import Flask, render_template, request
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

from prometheus_client import start_http_server, Summary
import random
import time

load_dotenv(override=True)

MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)  

DB_NAME = 'trials'
database = client[DB_NAME]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():

    first_name    = request.values.get("fname")
    last_name    = request.values.get("lname")

    result = {
        'first_name'    : first_name,
        'last_name'     : last_name
    }

    collection_name = 'users'
    new_collection = database[collection_name]
    x = new_collection.insert_one(result)
    print(x)

    return render_template('index.html')



# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__== "__main__":

    app.run(host="0.0.0.0", debug = True, port = 5003)

    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        