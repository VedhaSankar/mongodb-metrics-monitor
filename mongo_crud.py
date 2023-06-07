from socket import AI_PASSIVE
import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

# creating a MongoClient object  
client = MongoClient(MONGO_URI)  

# accessing the database  
DB_NAME = 'trials'
database = client[DB_NAME]

def insert_records():

    result = {

        "result"    : "3"
    }

    collection_name = 'docker'
    new_collection = database[collection_name]

    x = new_collection.insert_one(result)
    print(x)


# def read_records():
#     print (DB_NAME.database.find())

    # for record in database.find():
    #     print (record)

def add_unique_key_index(collection_name):
    """
        db.members.createIndex( { "user_id": 1 }, { "unique": True } )
    """
    # access collection of the database  
    database[collection_name].create_index([("project_id", pymongo.ASCENDING)])


def get_collections():

    collections = database.list_collection_names()

    for collect in collections: 
        print(collect) 

def startpy():

    # insert_records()
    # read_records()
    add_unique_key_index('docker')



if __name__ == '__main__':

    startpy()

