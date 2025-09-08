from pymongo import MongoClient ,errors
import os

class Loader:
    def __init__(self):
        self.DB_HOST = os.getenv("DB_HOST","mongodb://localhost:27017/")
        self.DB_NAME = os.getenv("DB_NAME","Data")
        self.COLL_NAME = os.getenv("COLL_NAME","Records")
        self.client = MongoClient(self.DB_HOST)
        self.mydb = self.client[self.DB_NAME]
        self.collection = self.mydb[self.COLL_NAME]
    def load_to_mongodb(self,massage):
        try:
            res = self.collection.insert_one(massage)
            return res.inserted_id
        except errors.ServerSelectionTimeoutError as err:
            print(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            print(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            print(f"Configuration error: {err}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise