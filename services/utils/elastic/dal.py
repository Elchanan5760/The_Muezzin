from .connection import Connection
import os
from .logger import Logger
from .mapping import  Mapping

class DAL:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME",'store_data')
        self.logger = Logger.get_logger()
        self.mapping = Mapping()

    #Loads to elastic with index store_data.
    def create_doc(self,doc_id,doc):
        try:
            self.es.index(index=self.IDX_NAME, id=doc_id, document=doc)
            self.logger.info("Metadata upload to elastic")
        except Exception as ex:
            self.logger.error(ex)

    # Update document with map by the received type.
    def update_doc(self,doc_id,field,value):
        my_type = ""
        if isinstance(value,int):
            my_type = "integer"
        if isinstance(value,float):
            my_type = "float"
        if isinstance(value,str):
            my_type = "text"
        self.mapping.add_field_map(field,my_type)
        try:
            response = self.es.update(
                index=self.IDX_NAME,
                id=doc_id,
                body={
                    "doc": {
                        field: value
                    }
                }
            )
            self.logger.info(f"Value {field}: {value} added to document id:{doc_id}.")
            return response
        except Exception as e:
            self.logger.error(f"Error updating document: {e}")
