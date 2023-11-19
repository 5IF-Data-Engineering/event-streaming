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
import snowflake.connector


def insert_incident_dim_data():
    conn_stag = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB_STAGING
    )
    cursor_stag = conn_stag.cursor()
    search_query = """
        SELECT DISTINCT incident FROM joined_bus_weather
        ORDER BY incident ASC;
    """
    cursor_stag.execute(search_query)
    results = cursor_stag.fetchall()
    conn_prod = snowflake.connector.connect(
        user=SNOWFLAKE_USERNAME,
        password=SNOWFLAKE_PASSWORD,
        account='ee65799.europe-west4.gcp',
        warehouse='COMPUTE_WH',
        database='DENG_PRODUCTION',
        schema='DATA_PROD'
    )
    cursor_prod = conn_prod.cursor()
    for result in results:
        insert_query = """
            INSERT INTO DENG_PRODUCTION.DATA_PROD.INCIDENT_DIM (name) 
            VALUES (%s)
            """
        cursor_prod.execute(insert_query, result)
    conn_prod.commit()
    cursor_stag.close()
    conn_stag.close()
    cursor_prod.close()
    conn_prod.close()
