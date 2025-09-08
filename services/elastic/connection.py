from elasticsearch import Elasticsearch

class Connection:
    @staticmethod
    def get_es_client() -> Elasticsearch:
        try:
            es = Elasticsearch("http://localhost:9200")
            print("Connected to Elasticsearch!")
            return es
        except Exception as ex:
            print(f"Could not connect to Elasticsearch, retrying...\n{ex}")
        raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")