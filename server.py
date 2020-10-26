from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

import random
import json
df = pd.read_csv('training_data.csv')
input_symptoms = {}
for i in df.columns:
    input_symptoms[i] = random.randrange(0,2,1)
app = Flask(__name__)

DTCModel = pickle.load(open('DTCmodel.pkl','rb'))
RFCModel = pickle.load(open('RFCmodel.pkl','rb'))
test_x = pd.read_json(json.dumps([input_symptoms]))
test_x.drop(columns=['prognosis','Unnamed: 133'],axis=1,inplace = True)
DTCprediction = DTCModel.predict(test_x)
RFCprediction = RFCModel.predict(test_x)
DTCoutput = DTCprediction
#print(df.iloc[DTCoutput[0],-2])
RFCoutput = RFCprediction
output = {'RFC-result':df.iloc[RFCoutput[0],-2],'DTC-result':df.iloc[DTCoutput[0],-2],}
# @app.route('/api',methods=['POST'])
@app.route('/')
def symptomGiver():
    # data = request.get_json(force = True)
    # print(data)
#    test_x = pd.DataFrame.read_json(json.dumps(input_symptoms))
    #print(test_x)
    symptomsList = list(test_x.columns)
    #print(output)
    #return output['DTC-result']
    return render_template('index.html',variable = symptomsList)
    #return jsonify(output)
@app.route('/predicted')
def predict():
    return "aight"
if __name__ == '__main__':
    app.run(port=5000,debug=True)