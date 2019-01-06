# Docbot

# Create new conda environment using command:
```
conda create --no-default-packages -n docbot python
```

# Before committing changes :-
1)Update requirements.txt file:- ```pip freeze > requirements.txt```<br/>
2)Remove all raw datasets from datasets directory<br/>
3)Remove all pre_trained models from models directory<br/>
4)Update links.txt file to include all links of raw datasets<br/>

# After cloning project repository :-
1)Update environment requirements:- ```pip install -r requirements.txt```<br/>
2)Download and place all raw datasets in datasets/raw directory<br/>
3)Place all pre_trained models in models/pre_trained directory<br/>
