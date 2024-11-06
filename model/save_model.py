import joblib
import os

def save_model(model, model_name):
    model_dir = '../model/saved_models'
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, os.path.join(model_dir, model_name))
    print(f"Model saved as {model_name}.")
