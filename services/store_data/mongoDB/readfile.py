import os
from services.utils.elastic.logger import Logger
import gridfs


class FileRead:
    def __init__(self,db):
        self.fs = gridfs.GridFS(db)
        self.FILE_TYPE = os.getenv("FILE_TYPE",'audio/wav')
        self.logger = Logger.get_logger()

    # Get file path and load it to mongoDB.
    def upload(self,file_path,file_key):
        try:
            with open(file_path, 'rb') as f:
                file_id = self.fs.put(f, filename=os.path.basename(file_path),key=file_key, content_type=self.FILE_TYPE)
                print(f"File uploaded with ID: {file_id}")
            self.logger.info(f"{os.path.basename(file_path)} uploaded successfully.")
        except Exception as ex:
            self.logger.error(ex)
