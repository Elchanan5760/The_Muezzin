import os

from services.utils.elastic.connection import Connection


class Queries:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME","store_data")

    def get_all_data(self):
        res = self.es.search(index=self.IDX_NAME, query={"match_all": {}})
        list_id = []
        for hit in res["hits"]["hits"]:
            list_id.append(hit)
        return list_id