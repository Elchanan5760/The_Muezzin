import os

from services.utils.elastic.logger import Logger
import json
from services.utils.kafka.sub import Sub
from services.store_data.key.hash import CreateHash
from services.utils.elastic.mapping import Mapping
from services.utils.elastic.dal import DAL
from services.utils.mongoDB.readfile import FileRead
from services.utils.mongoDB.dal import Loader

class StoringManager:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.Topic = os.getenv('Topic','processed')
        self.sub = Sub(self.Topic)
        self.sub.connect()
        self.create_id = CreateHash()
        self.loader = DAL()
        self.mongodb = Loader()
        self.read_wav = FileRead(self.mongodb.mydb)
        mapping = Mapping()
        mapping.map_idx()
    def manage_all_files(self):
        self.logger.info("The pesister started")
        data = self.sub.sub()

        # Iterate on data from kafka.
        for msg in data:
            print('this',msg)
            hash_idx = self.create_id.hashing(msg)
            self.read_wav.upload(msg['path'],hash_idx)
            del msg['path']
            print(msg)
            json_msg = json.dumps(msg)
            self.loader.create_doc(hash_idx, json_msg)