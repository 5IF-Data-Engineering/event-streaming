import psycopg2
from pipeline_api.settings import (
    POSTGRES_PORT,
    POSTGRES_HOST,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB_STAGING,
)


def load_full_data(transformed_data):
    """
    Load data to PostgreSQL
    :param transformed_data: data for PostgreSQL
    :return: None
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_STAGING,
    )
    cur = conn.cursor()
    for data in transformed_data:
        query = """
            INSERT INTO staging_weather (year, month, day, day_of_week, day_type, hour, 
            temperature, humidity, precipitation, rain, snowfall, windspeed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s)
        """
        params = (
            data["year"],
            data["month"],
            data["day"],
            data["day_of_week"],
            data["day_type"],
            data["hour"],
            data["temperature"],
            data["humidity"],
            data["precipitation"],
            data["rain"],
            data["snowfall"],
            data["windspeed"]
        )
        cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
