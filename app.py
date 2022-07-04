from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('illnesstrainer.pkl', 'rb'))


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        my_dict = request.form
        try:
            city = str(my_dict['city'])
            gender = str(my_dict['gender'])
            age = int(my_dict['age'])
            income = float(my_dict['income'])
        except ValueError:
            return render_template('index.html')
        else:
            input_features = [[city, gender, age, income]]
            prediction = model.predict(input_features)
            if prediction[0] == 0:
                output = 'You are not ill'
            else:
                output = 'You are ill'

            return render_template('index.html', string=f"'prediction': {output}")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
