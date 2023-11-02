from pymongo import MongoClient
from event_streaming.settings import (
    MONGO_HOST,
    MONGO_PORT,
)

client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/?authSource=admin&readPreference=primary&ssl=false')
db = client['deng']


def load_data(transformed_data, daily=None):
    """
    Load data to MongoDB
    :param transformed_data
    :param daily:
    :return:
    """
    if daily is None:
        collection = db['weather-hourly']
    else:
        collection = db['weather-daily']
    collection.insert_many(transformed_data)
    return
