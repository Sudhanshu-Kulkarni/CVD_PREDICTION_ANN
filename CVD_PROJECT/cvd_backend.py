from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('models/heart_disease_model.pkl')  # Ensure model.pkl is in the correct directory
scaler = joblib.load('models/sc.pkl')  # Assuming you saved a scaler during training

@app.route('/')
def index():
    return render_template('index.html')  # Make sure to rename your HTML file as 'index.html'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON data from the frontend
    features = [
        data['age'], data['gender'], data['chestpain'], data['restingBP'],
        data['serumcholesterol'], data['fastingbloodsugar'], data['restingrelectro'],
        data['maxheartrate'], data['exerciseangina'], data['oldpeak'],
        data['slope'], data['noofmajorvessels']
    ]
    # Convert features to a numpy array and reshape for the scaler
    input_data = np.array(features).reshape(1, -1)
    print(input_data)
    
    # Scale the input data (if model was trained with scaling)
    scaled_data = scaler.transform(input_data) if scaler else input_data

    # Make prediction (binary classification output)
    prediction = model.predict(scaled_data)[0]  # Output will be either 0 or 1

    print("Raw Prediction: ", prediction)  # Add this to see the actual model output

    # Convert prediction to a probability (if needed, for example)
    prediction_percentage = prediction

    # Return the result as JSON
    return jsonify({'prediction': float(prediction_percentage)})

if __name__ == '__main__':
    app.run(debug=True)
