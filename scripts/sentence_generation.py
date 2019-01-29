from text_processor import TextProcessor
import markovify
import numpy as np
import random
import re

data=
class TextGenerator:
    def __init__(self):
        self.disease_text_generator=markovify.NewlineText(open('response_templates.txt').read().split('\n'),state_size=2)
    def generate_response(self,disease):
        line=self.disease_text_generator.make_sentence()
        return re.sub('\w*__DISEASE__',disease,line)
