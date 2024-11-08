import numpy as np
from app.models.sleep_model import model, scaler_x, scaler_y

def predict_sleep_score(features):
    features_array = np.array([features]).reshape(1, -1)
    
    scaled_features = scaler_x.transform(features_array)
    raw_prediction = model.predict(scaled_features).reshape(-1, 1)
    sleep_score_raw = scaler_y.inverse_transform(raw_prediction)[0][0]
    
    # Custom mapping based on typical ranges observed in training
    if sleep_score_raw >= 5500:
        sleep_score = 10
    elif sleep_score_raw >= 5000:
        sleep_score = 9
    elif sleep_score_raw >= 4500:
        sleep_score = 8
    elif sleep_score_raw >= 4000:
        sleep_score = 7
    elif sleep_score_raw >= 3500:
        sleep_score = 6
    elif sleep_score_raw >= 3000:
        sleep_score = 5
    elif sleep_score_raw >= 2500:
        sleep_score = 4
    elif sleep_score_raw >= 2000:
        sleep_score = 3
    elif sleep_score_raw >= 1500:
        sleep_score = 2
    else:
        sleep_score = 1
    
    return sleep_score
