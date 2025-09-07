from kafka import KafkaConsumer
import json
import os

class Sub:
    def __init__(self,topic):
        self.bootstrap_servers = os.getenv("KAFKA_HOST","localhost:9092")
        self.group_id = os.getenv("GROUP_ID","GROUP_ID")
        self.topic = topic
        self.consumer = None

    def connect(self):
        try:
            self.consumer = KafkaConsumer(
                self.topic,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id,
                value_deserializer=lambda v: json.loads(v.decode("utf-8"))
            )
            print('connected to kafka SUB')
        except Exception as ex:
            print(ex)
            raise Exception(ex)

    def sub(self):
        try:
            for msg in self.consumer:
                print("received: ",msg.value,type(msg))
                yield msg.value
        except Exception as ex:
            print(ex)
            raise Exception(ex)