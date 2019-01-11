import spacy
nlp=spacy.load('en')
def parseQuery(query):
    parsed_info={}
    query=nlp(query)
    for token in query:
        if token.dep_=='attr':
            children=[str(child) for child in token.children]
            print(children[0])
            if 'weight' in children:
                parsed_info['weight']=children[0]
            elif 'height' in children:
                parsed_info['height']=children[0]
    return parsed_info