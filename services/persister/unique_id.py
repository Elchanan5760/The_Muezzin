import hashlib

class CreateID:
    def __init__(self):
        self.hasher = hashlib.sha256()

    def hashing(self,data_dict):
        sorted_items = sorted(data_dict)
        dict_string = repr(sorted_items).encode('utf-8')
        self.hasher.update(dict_string)
        return self.hasher.hexdigest()