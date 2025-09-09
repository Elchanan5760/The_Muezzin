from .connection import Connection
import os
from .logger import Logger

class Loading:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME",'store_data')
        self.logger = Logger.get_logger()

    #Loads store_data to elastic.
    def load_es(self,doc_id,doc):
        try:
            self.es.index(index=self.IDX_NAME, id=doc_id, document=doc)
            self.logger.info("Metadata upload to elastic")
        except Exception as ex:
            self.logger.error(ex)