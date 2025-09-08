from services.kafka.sub import Sub

class PersisterManager:
    def __init__(self):
        self.sub = Sub("processed")
        self.sub.connect()
    def manage_all_files(self):
        data = self.sub.sub()
        for msg in data:
            print(msg)