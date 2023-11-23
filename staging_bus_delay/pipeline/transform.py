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
