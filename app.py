from flask import Flask, render_template, request
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

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


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)