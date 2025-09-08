
import os
import wave

class ReadWave:
    @staticmethod
    def read_wav_file(file_path):
        try:
            # Extract the filename without the path
            filename = os.path.basename(file_path)
            with wave.open(file_path, mode="rb") as wf:
                n_channels = wf.getnchannels()
                sample_width = wf.getsampwidth()
                frame_rate = wf.getframerate()
                n_frames = wf.getnframes()

                print(f"Channels: {n_channels}")
                print(f"Sample Width (bytes): {sample_width}")
                print(f"Frame Rate (Hz): {frame_rate}")
                print(f"Number of Frames: {n_frames}")

            # Read the WAV file
            print(f"Successfully read: {filename}")
            return wf
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

