from ..elastic.logger import Logger
import datetime
import os

class Metadata:
    def __init__(self):
        self.dict_info = {}
        self.datetime = datetime
        self.logger = Logger.get_logger()
    def get_all_info(self,file_path):
        self.dict_info["path"] = file_path
        self.dict_info["name"] = self.get_name(file_path)
        self.dict_info["creation datetime"] = f"{self.get_creation_datetime(file_path)}"
        self.dict_info["modification datetime"] = f"{self.get_modify_timestamp(file_path)}"
        self.dict_info["size"] = self.get_size(file_path)
        print(self.dict_info)
        self.logger.info("Metadata created.")
        return self.dict_info

    def get_name(self,file_path):
        filename = os.path.basename(file_path)
        print("filename",filename)
        return filename

    def get_creation_datetime(self,file_path):
        timestamp = os.path.getctime(file_path)
        create_datetime = self.datetime.datetime.fromtimestamp(timestamp)
        print("creation time",create_datetime)
        return create_datetime

    def get_modify_timestamp(self,file_path):
        timestamp = os.path.getmtime(file_path)
        change_datetime = self.datetime.datetime.fromtimestamp(timestamp)
        print("change time", change_datetime)
        return change_datetime

    def get_size(self,file_path):
        file_size = os.path.getsize(file_path)
        print("file_size", file_size)
        return file_size