from kafka import KafkaConsumer
from kafka import KafkaProducer
from event_streaming.settings import (
    KAFKA_HOST,
    KAFKA_PORT,
)
import json
from kafka_ingestion_weather.pipeline.transform import transform_data


def consumer_transform_data(transform_topic_name: str, load_topic_name: str, city: str):
    """
    Consumer function to receive data from Kafka topic
    :param transform_topic_name:
    :param load_topic_name:
    :param city:
    :return:
    """
    consumer = KafkaConsumer(transform_topic_name, bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}',
                             auto_offset_reset='earliest', enable_auto_commit=True)
    for msg in consumer:
        data = json.loads(msg.value.decode('utf-8'))
        transformed_data = transform_data(data, city)
        producer = KafkaProducer(bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}')
        sent_data = json.dumps(transformed_data).encode('utf-8')
        producer.send(load_topic_name, sent_data)
        return