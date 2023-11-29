def transform_full_data(cursor, year):
    """
    Transform data from MongoDB to PostgreSQL
    :param cursor: data from MongoDB
    :param year: year
    :return: data for PostgreSQL
    """
    result = []
    for document in cursor:
        result.append(
            {
                "year": int(year),
                "month": document["month"],
                "day": document["day"],
                "day_of_week": document["day_of_week"],
                "day_type": document["day_type"],
                "hour": document["hour"],
                "location": document["location"],
                "incident": document["incident"],
                "delay": document["min_delay"],
                "gap": document["min_gap"],
                "direction": document["direction"],
                "vehicle": document["vehicle"]
            }
        )
    return result
