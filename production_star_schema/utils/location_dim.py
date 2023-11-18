from pipeline_api.settings import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB_STAGING,
    POSTGRES_DB_PRODUCTION
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
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_PRODUCTION
    )
    cursor_prod = conn_prod.cursor()
    geolocator = Nominatim(user_agent="pipeline_api")
    for result in results:
        name_location = f"{result[0]}, Toronto, Ontario, Canada"
        try:
            location = geolocator.geocode(name_location)
            result = (result[0], location.latitude, location.longitude)
        except:
            result = (result[0], None, None)
        insert_query = """INSERT INTO production_location_dimension (name, latitude, longitude) 
            VALUES (%s, %s, %s)
        """
        cursor_prod.execute(insert_query, result)
        conn_prod.commit()
    cursor_stag.close()
    conn_stag.close()
    cursor_prod.close()
    conn_prod.close()
