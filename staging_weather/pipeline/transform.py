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


def transform_data_year_month_day(cursor):
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
                "day": document["_id"]["day"],
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


def transform_full_data(cursor):
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
                "day_type": document["_id"]["dayType"],
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


def transform_data_weekday_weekend_hour(cursor):
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
