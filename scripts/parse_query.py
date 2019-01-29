import re
import spacy
nlp=spacy.load('en')
def parseBMIQuery(query):
    parsed_info={}
    parsed_numbers=[int(num) for num in re.findall(r'\d+',query)]
    ht_wt=re.findall(r'(weight|height)',query)
    parsed_units=re.findall(r'(cm|m|kg)',query)
    if 'cm' in parsed_units:
        parsed_numbers[parsed_units.index('cm')]/=100
    parsed_info[ht_wt.pop()]=parsed_numbers.pop()
    parsed_info[ht_wt.pop()]=parsed_numbers.pop()
    return parsed_info

def parseName(query):
    doc=nlp(query)
    name=None
    for token in doc:
        if token.tag_=='NN':
            if len([child for child in token.children])==0:
                name=str(token)
    return name.capitalize()