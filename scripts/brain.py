import spacy
import random
import os
nlp=spacy.load('en')
class Brain:
    def __init__(self,root_dir):
        self.root=root_dir
    def __analyzeQuery(self):
        analysis={}
        file=open(os.path.join(self.root,'datasets/raw/conversation_opener_queries')).readlines()[0].rstrip('\n').split('\t')
        if self.query in file:
            analysis['opener']=True
        file=open(os.path.join(self.root,'datasets/raw/conversation_end_queries')).readlines()[0].rstrip('\n').split('\t')
        if self.query in file:
            analysis['close']=True
        if self.query.find('calculate')!=-1 and self.query.find('bmi')!=-1:
            analysis['bmi']=True
        return analysis
    def predict(self,query):
        self.query=query.lower()
        self.query_info=self.__analyzeQuery()
        return self.__generateReply()
    def __generateReply(self):
        if self.query_info.get('opener') is not None:
            reply=open(os.path.join(self.root,'datasets/raw/conversation_opener_queries')).readlines()[1].rstrip('\n').split('\t')
            return random.choice(reply)
        elif self.query_info.get('close') is not None:
            reply=open(os.path.join(self.root,'datasets/raw/conversation_end_queries')).readlines()[1].rstrip('\n').split('\t')
            return random.choice(reply)
        #elif self.query_info['bmi'] is not None:
            
