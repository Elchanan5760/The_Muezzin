import os

from services.utils.elastic.connection import Connection


class Queries:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME","store_data")

    def get_all_id(self):
        res = self.es.search(index=self.IDX_NAME, query={"match_all": {}})
        list_id = []
        for hit in res["hits"]["hits"]:
            print('Changes', hit["_id"])
            list_id.append(hit["_id"])
        return list_id

    def count_words(self,doc_id,field):
        tv = self.es.termvectors(
            index=self.IDX_NAME,
            id=doc_id,
            fields=[field]
        )
        return tv