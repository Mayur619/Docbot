
# coding: utf-8

# In[8]:


import pandas as pd

disease = input("Enter Disease : ")

disease_to_symptoms(disease)


def disease_to_symptoms(disease):
    data = pd.read_csv('ds.csv')
    print('\n Possible Symptons are : \n',data[data.Disease==disease].Symptom.item())
    
    
    


# In[ ]:




