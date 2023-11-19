import snowflake.connector
from pipeline_api.settings import (
    SNOWFLAKE_USERNAME,
    SNOWFLAKE_PASSWORD
)


def create_prod_tables():
    """
    Create production tables in Snowflake
    """
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USERNAME,
        password=SNOWFLAKE_PASSWORD,
        account='ee65799.europe-west4.gcp',
        warehouse='COMPUTE_WH',
        database='DENG_PRODUCTION',
        schema='DATA_PROD'
    )
    cur = conn.cursor()
    create_location_dim = """
        CREATE OR REPLACE TABLE DATA_PROD.LOCATION_DIM (
            id bigint NOT NULL PRIMARY KEY AUTOINCREMENT,
            name varchar(255) NOT NULL,
            latitude float,
            longitude float
        );
    """
    create_time_dim = """
        CREATE OR REPLACE TABLE DATA_PROD.TIME_DIM (
            id bigint NOT NULL PRIMARY KEY AUTOINCREMENT,
            year int NOT NULL,
            month int NOT NULL,
            day_type varchar(255) NOT NULL,
            hour int NOT NULL,
        );
    """
    create_incident_dim = """
        CREATE OR REPLACE TABLE DATA_PROD.INCIDENT_DIM (
            id bigint NOT NULL PRIMARY KEY AUTOINCREMENT,
            name varchar(255) NOT NULL,
        );
    """
    create_fact_table = """
        CREATE OR REPLACE TABLE DATA_PROD.FACT_TABLE (
            id bigint NOT NULL PRIMARY KEY AUTOINCREMENT,
            time_id bigint NOT NULL,
            location_id bigint NOT NULL,
            incident_id bigint NOT NULL,
            avg_temperature float,
            min_temperature float,
            max_temperature float,
            avg_humidity float,
            avg_rain float,
            max_rain float,
            min_rain float,
            avg_wind_speed float,
            max_wind_speed float,
            min_wind_speed float,
            avg_delay float,
            min_delay float,
            max_delay float,
            count_delay int,
            avg_gap float,
            min_gap float,
            max_gap float,
            count_gap int,
            FOREIGN KEY (time_id) REFERENCES TIME_DIM(id),
            FOREIGN KEY (location_id) REFERENCES LOCATION_DIM(id),
            FOREIGN KEY (incident_id) REFERENCES INCIDENT_DIM(id)
        );
    """
    cur.execute(create_location_dim)
    cur.execute(create_time_dim)
    cur.execute(create_incident_dim)
    cur.execute(create_fact_table)
    # conn.commit()
    cur.close()
    conn.close()
