import psycopg2
from pipeline_api.settings import (
    POSTGRES_PORT,
    POSTGRES_HOST,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB_STAGING,
)


def load_data_weekday_weekend_hour(transformed_data):
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
            INSERT INTO staging_bus_delay_weekday_weekend_hour (id, day_type, hour, 
            avg_delay, min_delay, max_delay, count_delay, 
            avg_gap, min_gap, max_gap, count_gap)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s)
        """
        data_hour = str(data["hour"])
        if data["hour"] == 0:
            data_hour = "00"
        elif 0 < data["hour"] < 10:
            data_hour = "0" + str(data["hour"])
        params = (
            data["day_type"] + data_hour,
            data["day_type"],
            data["hour"],
            data["avg_delay"],
            data["min_delay"],
            data["max_delay"],
            data["count_delay"],
            data["avg_gap"],
            data["min_gap"],
            data["max_gap"],
            data["count_gap"],
        )
        cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()


def load_data_weekday_weekend_hour_location_incident(transformed_data):
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
            INSERT INTO staging_bus_delay_weekday_weekend_hour_location_incident (day_type, hour, location, incident,
            avg_delay, min_delay, max_delay, count_delay, 
            avg_gap, min_gap, max_gap, count_gap)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)
        """
        params = (
            data["day_type"],
            data["hour"],
            data["location"],
            data["incident"],
            data["avg_delay"],
            data["min_delay"],
            data["max_delay"],
            data["count_delay"],
            data["avg_gap"],
            data["min_gap"],
            data["max_gap"],
            data["count_gap"]
        )
        cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()


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
            INSERT INTO staging_bus_delay (year, month, day_type, hour, location, incident,
            avg_delay, min_delay, max_delay, count_delay, 
            avg_gap, min_gap, max_gap, count_gap)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s)
        """
        params = (
            data["year"],
            data["month"],
            data["day_type"],
            data["hour"],
            data["location"],
            data["incident"],
            data["avg_delay"],
            data["min_delay"],
            data["max_delay"],
            data["count_delay"],
            data["avg_gap"],
            data["min_gap"],
            data["max_gap"],
            data["count_gap"]
        )
        cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()
    