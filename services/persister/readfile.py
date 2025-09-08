import os

import gridfs


class FileRead:
    def __init__(self,db):
        self.fs = gridfs.GridFS(db)
        self.FILE_TYPE = os.getenv("FILE_TYPE",'audio/wav')
    def upload(self,file_path,file_key):
        with open(file_path, 'rb') as f:
            file_id = self.fs.put(f, filename=os.path.basename(file_path),key=file_key, content_type=self.FILE_TYPE)
            print(f"File uploaded with ID: {file_id}")
