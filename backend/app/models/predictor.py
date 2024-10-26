import pickle
import numpy as np

# Load the pre-trained model (replace 'model.pkl' with the actual model file)

    # model = pickle.load(model_file)

def predict_sleep_quality(steps, exercise, sedentary_time, heart_rate, calories):
    features = np.array([[steps, exercise, sedentary_time, heart_rate, calories]])
    prediction = model.predict(features)
    return prediction[0]