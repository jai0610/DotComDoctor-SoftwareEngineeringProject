from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

DTCModel = pickle.load(open('DTCmodel.pkl','rb'))
RFCModel = pickle.load(open('RFCmodel.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force = True)
    test_x = pd.read_json(data)
    DTCprediction = DTCModel.predict(test_x)
    RFCprediction = RFCModel.predict(test_x)
    DTCoutput = DTCprediction
    RFCoutput = RFCprediction
    output = {'RFC-result':RFCoutput,'DTC-result':DTCoutput,}
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000,debug=True)