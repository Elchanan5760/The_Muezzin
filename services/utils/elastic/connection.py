from elasticsearch import Elasticsearch
from .logger import Logger

class Connection:
    """ Connected to elasticsearch. """
    @staticmethod
    def get_es_client() -> Elasticsearch:
        logger = Logger.get_logger()
        try:
            es = Elasticsearch("http://localhost:9200")
            logger.info("Connected to elasticsearch.")
            return es
        except Exception as ex:
            logger.error(ex)
        raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")