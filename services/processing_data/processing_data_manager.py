import os
from glob import glob
from services.processing_data.read_file import ReadWave
from services.processing_data.get_metadata import Metadata
from services.kafka.pub import Pub
from services.elastic.logger import Logger
from transcription.speech_to_text import SpeechToText

class ProcessorManager:
    def __init__(self):
        self.folder_path = os.getenv("FOLDER_PATH",r"C:\Users\HOME\Music\Records_for_project\drive-download-20250907T074945Z-1-001")
        self.metadata = Metadata()
        self.pub = Pub()
        self.pub.connect()
        self.logger = Logger.get_logger()
        self.transcription = SpeechToText()
    def manage_all_files(self):
        self.logger.info("The muazin started")
        # Construct the pattern to find all .wav files in the folder
        search_pattern = os.path.join(self.folder_path, '*.wav')

        # Iterate through all files.
        for file_path in glob(search_pattern):
            dict_info = self.metadata.get_all_info(file_path)
            dict_info["transcribed"] = self.transcription.transcription(file_path)
            self.pub.pub(dict_info,"processed")

