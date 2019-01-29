import parse_query
import os
import wrappers
import re
class Perception:
    def __init__(self,root):
        self.root=root
        self.context={}
        self.analysis={}
    def _analyzeQuery(self,query):
        self.query=query
        self.context={}
        regex_dict={'bmi':re.compile(r'.*calculate.*bmi.*')}
        if self.analysis.get('opener')==True:
            self.context['name']=parse_query.parseName(query)
            del self.analysis['opener']
        file=open(os.path.join(self.root,'datasets/raw/conversation_opener_queries')).readlines()[0].rstrip('\n').split('\t')
        if self.query in file:
            self.analysis['opener']=True
        file=open(os.path.join(self.root,'datasets/raw/conversation_end_queries')).readlines()[0].rstrip('\n').split('\t')
        if self.query in file:
            self.analysis['close']=True
        if regex_dict['bmi'].match(query):
            self.query=input('Can you please tell me your height and weight?').lower()
            self.analysis['bmi']=parse_query.parseBMIQuery(self.query)
        return wrappers.AnalysisWrapper(self.analysis),wrappers.ContextWrapper(self.context)

