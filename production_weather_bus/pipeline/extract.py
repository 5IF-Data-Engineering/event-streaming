import psycopg2
from event_streaming.settings import (
    POSTGRES_PORT,
    POSTGRES_HOST,
    POSTGRES_USERNAME,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
)

def extract_data():
    """
    Extract Data
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

#Extract Data From Postgres DB of Joined table