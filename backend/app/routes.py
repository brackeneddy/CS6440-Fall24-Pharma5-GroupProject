from flask import Blueprint, render_template, request, jsonify
from app.models.predictor import predict_sleep_quality

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello World!" 

@main.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json

    # Extract necessary features
    steps = data.get('steps')
    exercise = data.get('exercise')
    sedentary_time = data.get('sedentary_time')
    heart_rate = data.get('resting_heart_rate')
    calories = data.get('calories_burned')

    # Make the prediction using the machine learning model
    prediction = predict_sleep_quality(steps, exercise, sedentary_time, heart_rate, calories)

    # Return the prediction as JSON
    return jsonify({'predicted_sleep_quality': prediction})
