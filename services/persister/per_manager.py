from services.kafka.sub import Sub
from unique_id import CreateID

class PersisterManager:
    def __init__(self):
        self.sub = Sub("processed")
        self.sub.connect()
        self.create_id = CreateID()
    def manage_all_files(self):
        data = self.sub.sub()
        for msg in data:
            print(msg)
            print(self.create_id.hashing(msg))
