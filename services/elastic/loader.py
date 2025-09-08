from .connection import Connection
import os

class Loading:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME",'metadata')
    def load_es(self,doc_id,doc):
         response = self.es.index(index=self.IDX_NAME, id=doc_id, document=doc)
         print(response['result'])