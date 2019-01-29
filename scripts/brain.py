import spacy
import perception
import generation
nlp=spacy.load('en')
class Brain:
    def __init__(self,root_dir):
        self.root=root_dir
        self.percept=perception.Perception(self.root) 
        self.generate=generation.Generation(self.root)
    
    def predict(self,query):
        self.query=query.lower()
        understanding,context=self.percept.__analyzeQuery(self.query)
        return self.generate.__generateReply(understanding,context)
    
    def print(self):
        print(self.percept)
        print(self.generate)