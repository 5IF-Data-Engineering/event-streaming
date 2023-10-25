from pymongo import MongoClient
from event_streaming.settings import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USERNAME,
    MONGO_PASSWORD,
)

client = MongoClient(f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/')
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
