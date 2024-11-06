import joblib
import os

def load_model(model_name):
    model_path = os.path.join('model/saved_models', model_name)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file {model_name} not found in 'model/saved_models' directory.")
    return joblib.load(model_path)
