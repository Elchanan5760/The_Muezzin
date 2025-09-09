import os
from glob import glob
from services.processing_data.metadata.get_metadata import Metadata
from services.utils.kafka.pub import Pub
from services.utils.elastic.logger import Logger

class ProcessorManager:
    def __init__(self):
        self.folder_path = os.getenv("FOLDER_PATH",r"C:\Users\HOME\Music\Records_for_project\drive-download-20250907T074945Z-1-001")
        self.metadata = Metadata()
        self.TOPIC = os.getenv('TOPIC', 'metadata')
        self.pub = Pub()
        self.pub.connect()
        self.logger = Logger.get_logger()
    def manage_all_files(self):
        self.logger.info("The muazin started")
        # Construct the pattern to find all .wav files in the folder
        search_pattern = os.path.join(self.folder_path, '*.wav')

        # Iterate through all files.
        for file_path in glob(search_pattern):
            dict_info = self.metadata.get_all_info(file_path)
            self.pub.pub(dict_info,self.TOPIC)

