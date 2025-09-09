import hashlib
from services.utils.elastic.logger import Logger

class CreateID:
    def __init__(self):
        self.hasher = hashlib.sha256()
        self.logger = Logger.get_logger()

    # Get data and return hash from data itself.
    def hashing(self,data_dict):
        try:
            sorted_items = sorted(data_dict)
            dict_string = repr(sorted_items).encode('utf-8')
            self.hasher.update(dict_string)
            self.logger.info("Hash ID created.")
            return self.hasher.hexdigest()
        except Exception as ex:
            self.logger.error(ex)