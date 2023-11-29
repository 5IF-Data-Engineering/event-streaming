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
                "year": document["year"],
                "month": document["month"],
                "day": document["day"],
                "day_of_week": document["day_of_week"],
                "day_type": document["day_type"],
                "hour": document["hour"],
                "temperature": document["temperature_2m"],
                "humidity": document["relativehumidity_2m"],
                "precipitation": document["precipitation"],
                "rain": document["rain"],
                "snowfall": document["snowfall"],
                "windspeed": document["windspeed_10m"]
            }
        )
    return result
