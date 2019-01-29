import os
import utilities
import random
class Generation:
    def __init__(self,root):
        self.root=root
    def _generateReply(self,analysis_wrapper,context_wrapper):
        self.analysis_info=analysis_wrapper.percept
        self.context=context_wrapper.context
        print(self.context)
        if self.context.get('name'):
            return self.context['name']
        if self.analysis_info.get('opener') is not None:
            reply=open(os.path.join(self.root,'datasets/raw/conversation_opener_queries')).readlines()[1].rstrip('\n').split('\t')
            return random.choice(reply)
        elif self.analysis_info.get('close') is not None:
            reply=open(os.path.join(self.root,'datasets/raw/conversation_end_queries')).readlines()[1].rstrip('\n').split('\t')
            return random.choice(reply)
        elif self.analysis_info.get('bmi') is not None:
            return utilities.CalculateBMI(self.analysis_info['bmi']['height'],self.analysis_info['bmi']['weight'])