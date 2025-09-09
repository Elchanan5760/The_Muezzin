import speech_recognition as sr
from services.elastic.logger import Logger

class SpeechToText:
    def __init__(self):
        self.r = sr.Recognizer()
        self.logger = Logger.get_logger()

    def transcription(self,file_path):
        try:
            with sr.AudioFile(file_path) as source:
                audio = self.r.record(source)
            text = self.r.recognize_google(audio)
            print(f"Text from audio file transcript: {text}")
            self.logger.info("Text from audio file transcript.")
            return text

        except sr.UnknownValueError:
            print("Could not understand audio")
            self.logger.error("Could not understand audio")

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            self.logger.error(f"Could not request results from Google Speech Recognition service; {e}")