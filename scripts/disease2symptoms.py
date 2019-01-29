import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

df = pd.read_excel('./raw_data.xlsx')
data = df.fillna(method='ffill')

data.head()


list(data)


def process_data(data):
    data_list = []
    data_name = data.replace('^','_').split('_')
    n = 1
    for names in data_name:
        if (n % 2 == 0):
            data_list.append(names)
        n += 1
    return data_list

disease_list = []
disease_symptom_dict = defaultdict(list)
disease_symptom_count = {}
count = 0

for idx, row in data.iterrows():
    if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
        disease = row['Disease']
        disease_list = process_data(data=disease)
        count = row['Count of Disease Occurrence']
    if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
        symptom = row['Symptom']
        symptom_list = process_data(data=symptom)
        for d in disease_list:
            for s in symptom_list:
                disease_symptom_dict[d].append(s)
            disease_symptom_count[d] = count


df1 = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom'])
df1.head()
df1[df1.Disease=='delusion'].Symptom.item()





