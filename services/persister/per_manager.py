from services.elastic.logger import Logger
import json
from services.kafka.sub import Sub
from unique_id import CreateID
from services.elastic.mapping import Mapping
from services.elastic.loader import Loading
from readfile import FileRead
from mongoDB.dal import Loader

class PersisterManager:
    def __init__(self):
        self.logger = Logger.get_logger()
        self.sub = Sub("processed")
        self.sub.connect()
        self.create_id = CreateID()
        self.loader = Loading()
        self.mongodb = Loader()
        self.read_wav = FileRead(self.mongodb.mydb)
        mapping = Mapping()
        mapping.map_idx()
    def manage_all_files(self):
        self.logger.info("The pesister started")
        data = self.sub.sub()
        for msg in data:
            print('this',msg)
            hash_idx = self.create_id.hashing(msg)
            self.read_wav.upload(msg['path'],hash_idx)
            del msg['path']
            print(msg)
            json_msg = json.dumps(msg)
            self.loader.load_es(hash_idx,json_msg)