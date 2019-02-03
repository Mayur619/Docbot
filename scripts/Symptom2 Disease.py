
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np 
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def Symptom2Diseases(s):
    data= pd.read_csv("Scraped-Data/df_pivoted.csv")     # Cleaned Data
    cols = data.columns
    values = cols[2:]
    x = data[cols[2:]]
    y = data['Source']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

    mnb_tot = MultinomialNB()
    mnb_tot = mnb_tot.fit(x, y)

    
    to_predict = x_test[1:2]

    
    temp = np.zeros(values.size)

    for j in range(len(s)):
        for i in range(404):
            if s[j]== values[i]:
                temp[i]=1;

    to_predict.values[0]=temp
    #predict
    disease_pred = mnb_tot.predict(to_predict)

    print("Possible Disease is : ",disease_pred[0])
    
    
#data1= pd.read_csv('ds.csv')
#data1[15:16].values
# User Input 
s=['dysarthria', 'asthenia', 'speech slurred', 'facial paresis', 'hemiplegia', 'unresponsiveness', 'seizure', 'numbness']   
Symptom2Diseases(s)


# In[ ]:




