from convert_to_datetime import DateTime
import json
from services.kafka.sub import Sub
from unique_id import CreateID
from services.elastic.mapping import Mapping
from services.elastic.loader import Loading

class PersisterManager:
    def __init__(self):
        self.sub = Sub("processed")
        self.sub.connect()
        self.create_id = CreateID()
        self.loader = Loading()
        mapping = Mapping()
        mapping.map_idx()
    def manage_all_files(self):
        data = self.sub.sub()
        for msg in data:
            print(msg)
            print(type(self.create_id.hashing(msg)))
            hash_idx = self.create_id.hashing(msg)
            del msg['path']
            print(msg)
            json_msg = json.dumps(msg)
            self.loader.load_es(hash_idx,json_msg)