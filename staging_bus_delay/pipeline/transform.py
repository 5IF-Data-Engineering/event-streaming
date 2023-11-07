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
                "avg_delay": document["avg_delay"],
                "min_delay": document["min_delay"],
                "max_delay": document["max_delay"],
                "count_delay": document["count_delay"],
                "avg_gap": document["avg_gap"],
                "min_gap": document["min_gap"],
                "max_gap": document["max_gap"],
                "count_gap": document["count_gap"]
            }
        )
    return result


def transform_data_weekday_weekend_hour_location_incident(cursor):
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
                "location": document["_id"]["location"],
                "incident": document["_id"]["incident"],
                "avg_delay": document["avg_delay"],
                "min_delay": document["min_delay"],
                "max_delay": document["max_delay"],
                "count_delay": document["count_delay"],
                "avg_gap": document["avg_gap"],
                "min_gap": document["min_gap"],
                "max_gap": document["max_gap"],
                "count_gap": document["count_gap"]
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
                "location": document["_id"]["location"],
                "incident": document["_id"]["incident"],
                "avg_delay": document["avg_delay"],
                "min_delay": document["min_delay"],
                "max_delay": document["max_delay"],
                "count_delay": document["count_delay"],
                "avg_gap": document["avg_gap"],
                "min_gap": document["min_gap"],
                "max_gap": document["max_gap"],
                "count_gap": document["count_gap"]
            }
        )
    return result
