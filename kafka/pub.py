from kafka import KafkaProducer
import os
import json

class Pub:
    def __init__(self,group_id):
        self.bootstrap_servers = os.getenv("KAFKA_HOST","localhost:9092")
        self.group_id = os.getenv("GROUP_ID","GROUP_ID")
        self.producer = None

    def connect(self):
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode("utf-8")            )
            print('connected to kafka PUB')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def pub(self,data,topic):
        try:
            print("sending to topic:",topic,data)
            self.producer.send(topic,value=data)
        except Exception as ex:
            print(ex)
            raise Exception(ex)