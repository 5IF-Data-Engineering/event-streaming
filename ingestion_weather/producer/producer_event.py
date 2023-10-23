from kafka import KafkaProducer
from event_streaming.settings import (
    KAFKA_HOST,
    KAFKA_PORT,
)
import datetime
import json


def producer_event(topic_name: str, name: str, description: str):
    """
    Producer function to send data to Kafka topic
    :param topic_name:
    :param name:
    :param description:
    :return:
    """
    producer = KafkaProducer(bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}')
    event = {
        "name": name,
        "description": description,
        "date_time": str(datetime.datetime.now())
    }
    sent_data = json.dumps(event).encode('utf-8')
    producer.send(topic_name, sent_data)
    return
