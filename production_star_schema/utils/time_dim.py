from pipeline_api.settings import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB_STAGING,
    POSTGRES_DB_PRODUCTION
)
import psycopg2


def insert_time_dim_data():
    conn_stag = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_STAGING
    )
    cursor_stag = conn_stag.cursor()
    search_query = """
        SELECT DISTINCT year INTO temp_year FROM joined_bus_weather
        ORDER BY year ASC;

        SELECT DISTINCT month INTO temp_month FROM joined_bus_weather
        ORDER BY month ASC;

        SELECT DISTINCT day_type INTO temp_day_type FROM joined_bus_weather
        ORDER BY day_type ASC;

        SELECT DISTINCT hour INTO temp_hour FROM joined_bus_weather
        ORDER BY hour ASC;
    """
    cursor_stag.execute(search_query)
    conn_stag.commit()
    search_query_all = """
        SELECT * FROM temp_year, temp_month, temp_day_type, temp_hour
        ORDER BY year, month, day_type, hour ASC;
    """
    cursor_stag.execute(search_query_all)
    results = cursor_stag.fetchall()
    conn_prod = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_PRODUCTION
    )
    cursor_prod = conn_prod.cursor()
    for result in results:
        insert_query = """INSERT INTO production_time_dimension (year, month, day_type, hour) 
            VALUES (%s, %s, %s, %s)
            """
        cursor_prod.execute(insert_query, result)
        conn_prod.commit()
    cursor_stag.close()
    conn_stag.close()
    cursor_prod.close()
    conn_prod.close()
