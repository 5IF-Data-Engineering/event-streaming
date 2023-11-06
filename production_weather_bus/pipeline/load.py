import psycopg2
from event_streaming.settings import (
    POSTGRES_PORT,
    POSTGRES_HOST,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
)

def load_data():
    """
    Load Data
    """
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
    )
    cur = conn.cursor()

    cur.close()
    conn.close()

#Load the final data into 1 Postgres DB