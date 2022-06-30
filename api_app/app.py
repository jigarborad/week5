import pandas as pd
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('illnesstrainer.pkl', 'rb'))


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return jsonify({'data': 'hello'})


@app.route('/predict')
def predict():
    city = str(request.args.get('city'))
    gender = str(request.args.get('gender'))
    age = int(request.args.get('age'))
    income = float(request.args.get('income'))
    input_features = pd.DataFrame({'City': [city], 'Gender': [gender], 'Age': [age], 'Income': [income]})
    prediction = model.predict(input_features)
    if prediction[0] == 0:
        output = 'You are not ill'
    else:
        output = 'You are ill'

    return jsonify({'Prediction': output})


if __name__ == "__main__":
    app.run(debug=True)
