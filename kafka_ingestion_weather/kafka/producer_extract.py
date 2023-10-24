from kafka import KafkaProducer
from event_streaming.settings import (
    KAFKA_HOST,
    KAFKA_PORT,
)
import json
from ingestion_weather.pipeline.extract import extract_data


def producer_extract_data(transform_topic_name: str, lat: str, lon: str,
                          start_date: str, end_date: str, daily=None):
    """
    Producer function to send data to transformation Kafka topic
    :param transform_topic_name:
    :param lat:
    :param lon:
    :param start_date:
    :param end_date:
    :param daily:
    :return:
    """
    producer = KafkaProducer(bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}')
    data = extract_data(lat, lon, start_date, end_date, daily)
    sent_data = json.dumps(data).encode('utf-8')
    producer.send(transform_topic_name, sent_data)
    return
