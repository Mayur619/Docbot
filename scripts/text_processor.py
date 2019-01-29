import numpy as np
from nltk.tokenize import word_tokenize

class TextProcessor:
    def __init__(self):
        self.word2id={}
        self.id2word={}
        self.idx=1
    def fit(self,data):
        for line in data:
           tokenized=word_tokenize(line)
           for token in tokenized:
               self._insert(token)
    def _insert(self,word):
        if self.word2id.get(word) is None:
            self.word2id[word]=self.idx
            self.id2word[self.idx]=word
            self.idx+=1
    def get_word2id(self):
        return self.word2id
    def get_id2word(self):
        return self.id2word
    def convert_sentences(self,data):
        converted=[]
        for line in data:
            converted_line=[]
            tokenized=word_tokenize(line)
            for token in tokenized:
                converted_line.append(self.word2id[token])
            converted.append(converted_line)
        return np.array(converted)
    def pad_sequences(self,data):
        self.max_len=max([len(s) for s in data])
        for i,line in enumerate(data):
            data[i]=np.append(line,[0]*(self.max_len-len(line)))
    def preprocess(self,data):
        self.fit(data)
        processed=self.convert_sentences(data)
        self.pad_sequences(processed)
        return processed