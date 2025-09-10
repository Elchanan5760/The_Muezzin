from services.utils.elastic.logger import Logger
import datetime
import os

class Metadata:
    def __init__(self):
        self.dict_info = {}
        self.datetime = datetime
        self.logger = Logger.get_logger()

    # Get the file path and returns the information from methods below.
    def get_all_info(self,file_path):
        self.dict_info["path"] = file_path
        self.dict_info["name"] = self.get_name(file_path)
        self.dict_info["creation_datetime"] = f"{self.get_creation_datetime(file_path)}"
        self.dict_info["modification_datetime"] = f"{self.get_modify_timestamp(file_path)}"
        self.dict_info["size"] = self.get_size(file_path)
        print(self.dict_info)
        self.logger.info("Metadata created.")
        return self.dict_info

    # Return the name of file.
    def get_name(self,file_path):
        filename = os.path.basename(file_path)
        print("filename",filename)
        return filename

    # Return the date and time of creation.
    def get_creation_datetime(self,file_path):
        timestamp = os.path.getctime(file_path)
        create_datetime = self.datetime.datetime.fromtimestamp(timestamp)
        print("creation time",create_datetime)
        return create_datetime

    # Return the date and time when it changed.
    def get_modify_timestamp(self,file_path):
        timestamp = os.path.getmtime(file_path)
        change_datetime = self.datetime.datetime.fromtimestamp(timestamp)
        print("change time", change_datetime)
        return change_datetime

    # Return the size of file.
    def get_size(self,file_path):
        file_size = os.path.getsize(file_path)
        print("file_size", file_size)
        return file_size