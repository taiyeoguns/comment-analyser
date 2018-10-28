import json
import os
from watson_developer_cloud import ToneAnalyzerV3


class ToneAnalyser:
    POSITIVE_TONES = ['joy', 'confident', 'analytical']
    NEGATIVE_TONES = ['sadness', 'anger', 'fear', 'tentative']

    def __init__(self):
        self.ta = ToneAnalyzerV3(
            username=os.getenv('WATSON_API_USERNAME'),
            password=os.getenv('WATSON_API_PASSWORD'),
            version='2017-09-21')

    def __repr__(self):
        return f''

    def get_tone(self, text):
        tones = self.ta.tone(
            tone_input=text, content_type='text/plain').get_result()

        for tt in tones['document_tone']['tones']:
            if tt['tone_id'] in self.POSITIVE_TONES:
                return 'positive'
            else:
                return 'negative'
