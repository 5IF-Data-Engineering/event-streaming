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
    cursor = collection.aggregate(
        [
            {
                '$addFields': {
                    'dayType': {
                        '$cond': {
                            'if': {
                                '$in': [
                                    '$day_of_week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                                ]
                            },
                            'then': 'weekday',
                            'else': 'weekend'
                        }
                    }
                }
            },
            {
                '$group': {
                    '_id': {
                        'year': '$year',
                        'month': '$month',
                        'dayType': '$dayType',
                        'hour': '$hour'
                    },
                    'avg_temperature': {
                        '$avg': '$temperature_2m'
                    },
                    'min_temperature': {
                        '$min': '$temperature_2m'
                    },
                    'max_temperature': {
                        '$max': '$temperature_2m'
                    },
                    'avg_humidity': {
                        '$avg': '$relativehumidity_2m'
                    },
                    'avg_rain': {
                        '$avg': '$precipitation'
                    },
                    'max_rain': {
                        '$max': '$precipitation'
                    },
                    'min_rain': {
                        '$min': '$precipitation'
                    },
                    'avg_wind_speed': {
                        '$avg': '$windspeed_10m'
                    },
                    'max_wind_speed': {
                        '$max': '$windspeed_10m'
                    },
                    'min_wind_speed': {
                        '$min': '$windspeed_10m'
                    }
                }
            }
        ]
    )
    return cursor
