from pymongo import MongoClient
def getMongoClient():
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % ("root", "rootpassword"))
    return client