from flask import Blueprint, request, jsonify
from app.models.predictor import predict_sleep_score

main = Blueprint('main', __name__)

@main.route('/predict-sleep-score', methods=['POST'])
def predict_sleep_score_route():
    data = request.json
    try:

        features = [
            data['TotalSteps'],
            data['Calories'],
            data['SedentaryMinutes'],
            data['FairlyActiveMinutes'],
            data['VeryActiveMinutes'],
            data['resting_heart_rate']
        ]

        prediction = predict_sleep_score(features)
        return jsonify({'sleep_score': prediction})

    except KeyError as e:
        return jsonify({'error': f'Missing input parameter: {e}'}), 400
