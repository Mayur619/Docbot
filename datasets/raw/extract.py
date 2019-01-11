import json
import pandas as pd
qa_list=[]
def extract(json_obj,que_str,ans_str):
    for record in json_obj:
        question_ans={}
        question_ans['question']=record[que_str]
        question_ans['answer']=record[ans_str]
        qa_list.append(question_ans)

obj=json.load(open('ehealthforumQAs.json','r'))
extract(obj,'question','answer')
obj=json.load(open('healthtapQAs.json','r'))
extract(obj,'question','answer')
obj=json.load(open('icliniqQAs.json','r'))
extract(obj,'question_text','answer')
obj=json.load(open('questionDoctorQAs.json','r'))
extract(obj,'question','answer')
obj=json.load(open('webmdQAs.json','r'))
extract(obj,'question','answer')
import pandas as pd
df=pd.read_excel('Who QnA.xlsx')
qa=[]
temp={}
for i in range(len(df)):
    if type(df.iloc[i,0])==str:
        #temp['answer']=''.join(temp['answer'])
        if i!=0:
            qa.append(temp)
        temp={}
        temp['question']=df.iloc[i,0]
    if type(df.iloc[i,1])==str:
        if temp.get('answer') is None:
            temp['answer']=[]
        temp['answer'].append(df.iloc[i,1])
qa.append(temp)
for obj in qa:
    obj['answer']=''.join(obj['answer'])
qa_list=qa_list+qa
datawriter=open('question_answers.json','w')
json.dump(qa_list,datawriter,indent=4)