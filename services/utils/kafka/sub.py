from kafka import KafkaConsumer
import json
import os
from services.utils.elastic.logger import Logger

class Sub:
    def __init__(self,topic):
        self.bootstrap_servers = os.getenv("KAFKA_HOST","localhost:9092")
        self.group_id = os.getenv("GROUP_ID","GROUP_ID")
        self.topic = topic
        self.consumer = None
        self.logger = Logger.get_logger()

    # Connects to kafka consumer.
    def connect(self):
        try:
            self.consumer = KafkaConsumer(
                self.topic,
                bootstrap_servers=self.bootstrap_servers,
                group_id=self.group_id,
                auto_offset_reset='earliest',
                value_deserializer=lambda v: json.loads(v.decode("utf-8"))
            )
            self.logger.info('Connected to kafka SUB')
            print('connected to kafka SUB')
        except Exception as ex:
            self.logger.error(ex)
            print(ex)
            raise Exception(ex)

    # Receive the messages from "topic" shown above.
    def sub(self):
        try:
            for msg in self.consumer:
                print("received: ",msg.value,type(msg))
                yield msg.value
                self.logger.info('Massage received successfully')
        except Exception as ex:
            self.logger.error(ex)
            print(ex)
            raise Exception(ex)