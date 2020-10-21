import requests
import pandas as pd
import random
import json
url = 'https://localhost:5000/api'
print('Enter symptoms as yes or no\n')
df = pd.read_csv('training_data.csv')
input_symptoms = {}
for i in df.columns:
    #symptom_predictor = input(f'Do you have {i} ?')
    input_symptoms[i] = random.randrange(0,2,1)
    # if(symptom_predictor[0].lower() == 'y'):
    #     input_symptoms[i] = 1
    # else:
    #     input_symptoms[i] = 0
#print(input_symptoms)
#r = requests.post(url,json=json.dumps(input_symptoms))
jsondict = {'symptoms':input_symptoms}
print(input_symptoms)
print(json.dumps(jsondict))
print(type(json.dumps(jsondict)))
test_x = pd.read_json(json.dumps([input_symptoms]))
print(test_x)
test_x.drop(columns=['prognosis','Unnamed: 133'],axis=1,inplace = True)
print(test_x)
#print(test_x['symptoms'])
# r = requests.post(url,json={json.dumps(input_symptoms)})
#print(r.json())