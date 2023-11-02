from pymongo import MongoClient
from event_streaming.settings import (
    MONGO_HOST,
    MONGO_PORT,
)

client = MongoClient(f'mongodb://{MONGO_HOST}:{MONGO_PORT}/')
db = client['deng']
collection = db['bus-delay']


def extract_data_weekday_weekend_hour():
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
                        'dayType': '$dayType',
                        'hour': '$hour'
                    },
                    'avg_delay': {
                        '$avg': '$min_delay'
                    },
                    'min_delay': {
                        '$min': '$min_delay'
                    },
                    'max_delay': {
                        '$max': '$min_delay'
                    },
                    'count_delay': {
                        '$sum': 1
                    },
                    'avg_gap': {
                        '$avg': '$min_gap'
                    },
                    'min_gap': {
                        '$min': '$min_gap'
                    },
                    'max_gap': {
                        '$max': '$min_gap'
                    }
                }
            },
        ]
    )
    return cursor


def extract_data_weekday_weekend_hour_location_incident():
    """
    Extract data from MongoDB for 3 dimensions: time, location, incident
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
                        'dayType': '$dayType',
                        'hour': '$hour',
                        'location': '$location',
                        'incident': '$incident'
                    },
                    'avg_delay': {
                        '$avg': '$min_delay'
                    },
                    'min_delay': {
                        '$min': '$min_delay'
                    },
                    'max_delay': {
                        '$max': '$min_delay'
                    },
                    'count_delay': {
                        '$sum': 1
                    },
                    'avg_gap': {
                        '$avg': '$min_gap'
                    },
                    'min_gap': {
                        '$min': '$min_gap'
                    },
                    'max_gap': {
                        '$max': '$min_gap'
                    }
                }
            }
        ]
    )
    return cursor
