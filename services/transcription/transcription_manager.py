import os
from services.transcription.speech_to_text import SpeechToText
from services.utils.kafka.pub import Pub
from services.utils.kafka.sub import Sub

class Transcription:
    def __init__(self):
        self.TOPIC_SUB = os.getenv('TOPIC_SUB','metadata')
        self.TOPIC_PUB = os.getenv('TOPIC_SUB','processed')
        self.sub = Sub(self.TOPIC_SUB)
        self.sub.connect()
        self.pub = Pub()
        self.pub.connect()
        self.transcription = SpeechToText()
    def manage_transcription(self):
        data = self.sub.sub()
        for msg in data:
            msg['transcribed'] = self.transcription.transcription(msg['path'])
            self.pub.pub(msg,self.TOPIC_PUB)