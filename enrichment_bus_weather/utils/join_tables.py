from pipeline_api.settings import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB_STAGING,
)
import psycopg2


def join_bus_weather_tables():
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_STAGING
    )
    cur = conn.cursor()
    query = """
        DROP TABLE IF EXISTS joined_bus_weather;
        
        SELECT a.year, a.month, a.day_type, a.hour, b.location, b.incident, a.avg_temperature, 
        a.min_temperature, a.max_temperature, a.avg_humidity, a.avg_rain, a.max_rain, a.min_rain, 
        a.avg_wind_speed, a.max_wind_speed, a.min_wind_speed, 
        b.avg_delay, b.min_delay, b.max_delay, b.count_delay, 
        b.avg_gap, b.min_gap, b.max_gap, b.count_gap
        INTO joined_bus_weather
        FROM staging_weather a 
        INNER JOIN staging_bus_delay b
        ON a.year = b.year AND a.month = b.month AND a.day_type = b.day_type AND a.hour = b.hour
        ORDER BY a.year, a.month, a.day_type, a.hour;
    """
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    