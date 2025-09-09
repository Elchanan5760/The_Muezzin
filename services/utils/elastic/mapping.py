from .connection import Connection
import os
from .logger import Logger

class Mapping:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME", 'store_data')
        self.mapping = os.getenv("MAPPING",{
                "mappings": {
                    "properties": {
                        "name": {"type": "keyword"},
                        'creation datetime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss[.S{1,9}]"},
                        'modification datetime': {"type": "date", "format": "yyyy-MM-dd HH:mm:ss[.S{1,9}]"},
                        'size': {"type": "integer"},
                        'Transcribed': {'type': 'text'}
                    }
                }
            })
        self.logger = Logger.get_logger()

    # Mapping with types templates.
    def map_idx(self,mapping = {}):
        try:
            if not mapping:
                mapping = self.mapping
            if not self.es.indices.exists(index=self.IDX_NAME):
                res = self.es.indices.create(index=self.IDX_NAME, body=mapping,ignore=400)
                self.logger.info("Metadata mapped successfully.")
                return res
        except Exception as ex:
            self.logger.error(ex)

    # Add field of mapping.
    def add_field_map(self,field_name,type_field):
        res = self.es.indices.put_mapping(
            index=self.IDX_NAME,
            body={
                "properties": {
                    field_name: {
                        "type": type_field
                    }
                }
            }
        )
        return res
