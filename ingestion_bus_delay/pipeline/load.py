from event_streaming.settings import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USERNAME,
    MONGO_PASSWORD,
)
from pymongo import MongoClient

client = MongoClient(f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/')
db = client['deng']


def load_data(transformed_data):
    """
    Load data to MongoDB
    :param transformed_data: data after transformation
    :return: True
    """
    db['bus-delay'].insert_many(transformed_data.to_dict('records'))
    return True
