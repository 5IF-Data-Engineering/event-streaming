def transform_data_year(cursor):
    """
    Transform data from MongoDB to PostgreSQL
    :param cursor: data from MongoDB
    :return: data for PostgreSQL
    """
    result = []
    for document in cursor:
        result.append(
            {
                "year": document["_id"]["year"],
                "avg_temperature": document["avg_temperature"],
                "min_temperature": document["min_temperature"],
                "max_temperature": document["max_temperature"],
                "avg_humidity": document["avg_humidity"],
                "avg_rain": document["avg_rain"],
                "max_rain": document["max_rain"],
                "min_rain": document["min_rain"],
                "avg_wind_speed": document["avg_wind_speed"],
                "max_wind_speed": document["max_wind_speed"],
                "min_wind_speed": document["min_wind_speed"],
            }
        )
    return result


def transform_data_month(cursor):
    """
    Transform data from MongoDB to PostgreSQL
    :param cursor: data from MongoDB
    :return: data for PostgreSQL
    """
    result = []
    for document in cursor:
        result.append(
            {
                "month": document["_id"]["month"],
                "avg_temperature": document["avg_temperature"],
                "min_temperature": document["min_temperature"],
                "max_temperature": document["max_temperature"],
                "avg_humidity": document["avg_humidity"],
                "avg_rain": document["avg_rain"],
                "max_rain": document["max_rain"],
                "min_rain": document["min_rain"],
                "avg_wind_speed": document["avg_wind_speed"],
                "max_wind_speed": document["max_wind_speed"],
                "min_wind_speed": document["min_wind_speed"],
            }
        )
    return result


def transform_data_hour(cursor):
    """
    Transform data from MongoDB to PostgreSQL
    :param cursor: data from MongoDB
    :return: data for PostgreSQL
    """
    result = []
    for document in cursor:
        result.append(
            {
                "hour": document["_id"]["hour"],
                "avg_temperature": document["avg_temperature"],
                "min_temperature": document["min_temperature"],
                "max_temperature": document["max_temperature"],
                "avg_humidity": document["avg_humidity"],
                "avg_rain": document["avg_rain"],
                "max_rain": document["max_rain"],
                "min_rain": document["min_rain"],
                "avg_wind_speed": document["avg_wind_speed"],
                "max_wind_speed": document["max_wind_speed"],
                "min_wind_speed": document["min_wind_speed"],
            }
        )
    return result


def transform_data_year_month(cursor):
    """
    Transform data from MongoDB to PostgreSQL
    :param cursor: data from MongoDB
    :return: data for PostgreSQL
    """
    result = []
    for document in cursor:
        result.append(
            {
                "year": document["_id"]["year"],
                "month": document["_id"]["month"],
                "avg_temperature": document["avg_temperature"],
                "min_temperature": document["min_temperature"],
                "max_temperature": document["max_temperature"],
                "avg_humidity": document["avg_humidity"],
                "avg_rain": document["avg_rain"],
                "max_rain": document["max_rain"],
                "min_rain": document["min_rain"],
                "avg_wind_speed": document["avg_wind_speed"],
                "max_wind_speed": document["max_wind_speed"],
                "min_wind_speed": document["min_wind_speed"],
            }
        )
    return result


def transform_data_weekday_weekend(cursor):
    """
    Transform data from MongoDB to PostgreSQL
    :param cursor: data from MongoDB
    :return: data for PostgreSQL
    """
    result = []
    for document in cursor:
        result.append(
            {
                "day_type": document["_id"]["dayType"],
                "avg_temperature": document["avg_temperature"],
                "min_temperature": document["min_temperature"],
                "max_temperature": document["max_temperature"],
                "avg_humidity": document["avg_humidity"],
                "avg_rain": document["avg_rain"],
                "max_rain": document["max_rain"],
                "min_rain": document["min_rain"],
                "avg_wind_speed": document["avg_wind_speed"],
                "max_wind_speed": document["max_wind_speed"],
                "min_wind_speed": document["min_wind_speed"],
            }
        )
    return result
