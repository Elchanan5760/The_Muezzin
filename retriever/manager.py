import os
from glob import glob
from pathlib import Path
from read_file import ReadWave
from get_metadata import Metadata

class Manager:
    def __init__(self):
        self.folder_path = os.getenv("FOLDER_PATH",r"C:\Users\HOME\Music\Records_for_project\drive-download-20250907T074945Z-1-001")
        self.metadata = Metadata()
    def manage_all_files(self):
        # Construct the pattern to find all .wav files in the folder
        search_pattern = os.path.join(self.folder_path, '*.wav')

        # Iterate through all files matching the pattern
        for file_path in glob(search_pattern):
            read_file = ReadWave.read_wav_file(file_path)
            dict_info = self.metadata.get_all_info(file_path)
