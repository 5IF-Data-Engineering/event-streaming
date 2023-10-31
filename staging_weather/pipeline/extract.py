from pymongo import MongoClient
from event_streaming.settings import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_USERNAME,
    MONGO_PASSWORD,
)

client = MongoClient(f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/')
db = client['deng']
collection = db['weather-hourly']


def extract_data_year(year: str):
    """
    Extract data from MongoDB
    :param year: Year of data to extract
    :return: data from MongoDB
    """
    cursor = collection.aggregate(
        [
            {
                '$match': {
                    'year': int(year)
                }
            },
            {
                '$group': {
                    '_id': {
                        'year': '$year'
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


def extract_data_month(month: str):
    """
    Extract data from MongoDB
    :param month: Month of data to extract
    :return: data from MongoDB
    """
    cursor = collection.aggregate(
        [
            {
                '$match': {
                    'month': int(month)
                }
            },
            {
                '$group': {
                    '_id': {
                        'month': '$month'
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


def extract_data_hour(hour: str):
    """
    Extract data from MongoDB
    :param hour: Hour of data to extract
    :return: data from MongoDB
    """
    cursor = collection.aggregate(
        [
            {
                '$match': {
                    'hour': int(hour)
                }
            },
            {
                '$group': {
                    '_id': {
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


def extract_data_year_month():
    """
    Extract data from MongoDB
    :return: data from MongoDB
    """
    cursor = collection.aggregate(
        [
            {
                '$group': {
                    '_id': {
                        'year': '$year',
                        'month': '$month'
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


def extract_data_year_month_day():
    """
    Extract data from MongoDB
    :return: data from MongoDB
    """
    cursor = collection.aggregate(
        [
            {
                '$group': {
                    '_id': {
                        'year': '$year',
                        'month': '$month',
                        'day': '$day'
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


def extract_data_weekday_weekend():
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
                        'dayType': '$dayType'
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


def extract_data_year_month_weekday_weekend():
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
                        'dayType': '$dayType'
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
