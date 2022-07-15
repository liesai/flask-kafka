from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor

from pip import main

TOPIC_NAME = "INFERENCE"

KAFKA_SERVER = "localhost:9092"

NOTIFICATION_TOPIC = "NOTIFICATION"
EMAIL_TOPIC = "EMAIL"

consumer = KafkaConsumer(
    TOPIC_NAME,
    # to deserialize kafka.producer.object into dict
    value_deserializer=lambda m: json.loads(m),

)

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)

def inferencProcessFunction(data):
    print("init")
    print(f"data :{data}")
    json_data = json.dumps(data)
    print(json_data)
    
    status = data['status']
    transit = data['transit']
    panier_uuid = data['uuidpanier']
    
    print(f"status : ======================== {status}=======================")
    notification_data = json_data.encode('utf-8')
    email_data = "{\"mail\": \"mail sent\"}".encode('utf-8')
    producer.send(NOTIFICATION_TOPIC, notification_data)
    print('send pass')
    producer.flush()
    producer.send(EMAIL_TOPIC, email_data)
    print(f"send {email_data} to {EMAIL_TOPIC}")
    producer.flush()

for inf in consumer:
    print(inf)
    inf_data = inf.value
    

    inferencProcessFunction(inf_data)
