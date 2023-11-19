from pipeline_api.settings import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB_STAGING,
    SNOWFLAKE_USERNAME,
    SNOWFLAKE_PASSWORD
)
import psycopg2
from geopy.geocoders import Nominatim


def insert_location_dim_data():
    conn_stag = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_STAGING
    )
    cursor_stag = conn_stag.cursor()
    search_query = """
        SELECT DISTINCT location FROM joined_bus_weather
        ORDER BY location ASC;
    """
    cursor_stag.execute(search_query)
    results = cursor_stag.fetchall()
    conn_prod = psycopg2.connect(
        user=SNOWFLAKE_USERNAME,
        password=SNOWFLAKE_PASSWORD,
        account='ee65799.europe-west4.gcp',
        warehouse='COMPUTE_WH',
        database='DENG_PRODUCTION',
        schema='DATA_PROD'
    )
    cursor_prod = conn_prod.cursor()
    geolocator = Nominatim(user_agent="pipeline_api")
    for result in results:
        name_location = f"{result[0]}, Toronto, Ontario, Canada"
        try:
            location = geolocator.geocode(name_location)
            params = (result[0], location.latitude, location.longitude)
        except:
            params = (result[0], None, None)
        insert_query = """
            INSERT INTO DENG_PRODUCTION.DATA_PROD.LOCATION_DIM (name, latitude, longitude) 
            VALUES (%s, %s, %s)
        """
        cursor_prod.execute(insert_query, params)
    conn_prod.commit()
    cursor_stag.close()
    conn_stag.close()
    cursor_prod.close()
    conn_prod.close()
