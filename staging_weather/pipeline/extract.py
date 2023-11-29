from pymongo import MongoClient
from pipeline_api.settings import (
    MONGO_HOST,
    MONGO_PORT,
)

client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/?authSource=admin&readPreference=primary&ssl=false')
db = client['deng']
collection = db['weather-hourly']


def extract_full_data():
    """
    Extract data from MongoDB
    :return: data from MongoDB
    """
    cursor = collection.find({})
    # Add day_type field
    for doc in cursor:
        doc['day_type'] = 'weekend' if doc['day_of_week'] in ['Saturday', 'Sunday'] else 'weekday'
        yield doc
    return cursor
