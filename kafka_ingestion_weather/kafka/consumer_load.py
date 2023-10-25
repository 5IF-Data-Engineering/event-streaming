from kafka import KafkaConsumer
from event_streaming.settings import (
    KAFKA_HOST,
    KAFKA_PORT,
)
import json
from kafka_ingestion_weather.pipeline.load import load_data


def consumer_load_data(load_topic_name: str, daily=None):
    """
    Consumer function to receive data from Kafka topic
    :param load_topic_name:
    :param daily: if daily is None, then hourly data is extracted
    :return:
    """
    consumer = KafkaConsumer(load_topic_name, bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}',
                             auto_offset_reset='earliest', enable_auto_commit=True)
    for msg in consumer:
        data = json.loads(msg.value.decode('utf-8'))
        load_data(data, daily)
        return
