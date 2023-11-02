from event_streaming.settings import (
    MONGO_HOST,
    MONGO_PORT,
)
from pymongo import MongoClient

client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/?authSource=admin&readPreference=primary&ssl=false')
db = client['deng']


def load_data(transformed_data):
    """
    Load data to MongoDB
    :param transformed_data: data after transformation
    :return: True
    """
    db['bus-delay'].insert_many(transformed_data.to_dict('records'))
    return True
