from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        country = request.form['country']
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        annual_salary = float(request.form['annual_salary'])
        credit_card_debt = float(request.form['credit_card_debt'])
        net_worth = float(request.form['net_worth'])

        # Prepare input for model prediction
        features = np.array([[gender, age, annual_salary, credit_card_debt, net_worth]])
        
        # Make prediction
        prediction = model.predict(features)

        return render_template('result.html', name=name, prediction=prediction[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501)


