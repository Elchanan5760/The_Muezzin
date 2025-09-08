from .connection import Connection
import os

class Mapping:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME", 'metadata')
        self.mapping = os.getenv("MAPPING",{
                "mappings": {
                    "properties": {
                        "name": {"type": "keyword"},
                        'creation datetime': {"type": "date", "format": "strict_date_optional_time||yyyy-MM-dd HH:mm:ss"},
                        'modification datetime': {"type": "date", "format": "strict_date_optional_time||yyyy-MM-dd HH:mm:ss"},
                        'size': {"type": "integer"}
                    }
                }
            })

    def map_idx(self,mapping = {}):
        if not mapping:
            mapping = self.mapping
        if not self.es.indices.exists(index=self.IDX_NAME):
            res = self.es.indices.create(index=self.IDX_NAME, body=mapping,ignore=400)
            return res

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

    def get_map(self):
        mapping = self.es.indices.get_mapping(index="tweets")
        return mapping
