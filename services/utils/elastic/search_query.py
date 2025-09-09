import os

from connection import Connection


class SearchQuery:
    def __init__(self):
        self.es = Connection.get_es_client()
        self.IDX_NAME = os.getenv("IDX_NAME","store_data")

    def search_word(self,word,field):
        search_query = {
            "query": {
                "match": {
                    field: word
                }
            }
        }
        self.es.search(index=self.IDX_NAME, body=search_query)