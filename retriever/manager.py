wav_data = {}
    # Construct the pattern to find all .wav files in the folder
    search_pattern = os.path.join(folder_path, '*.wav')

    # Iterate through all files matching the pattern
    for file_path in glob(search_pattern):
        folder = r"C:\Users\HOME\Music\Records_for_project\drive-download-20250907T074945Z-1-001"

        all_wav_files_data = ReadWave.read_wav_files_from_folder(folder)
        print(all_wav_files_data)
        # You can now access the data:
        for filename, (rate, data) in all_wav_files_data.items():
            print(f"File: {filename}, Sample Rate: {rate} Hz, Data Shape: {data.shape}")