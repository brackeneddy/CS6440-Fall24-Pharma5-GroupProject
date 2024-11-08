import joblib
import os

MODEL_PATH = '../model/saved_models/sleep_model.pkl'
SCALER_X_PATH = '../model/saved_models/scaler_x.pkl'
SCALER_Y_PATH = '../model/saved_models/scaler_y.pkl'

def load_model():
    return joblib.load(MODEL_PATH)

def load_scaler_x():
    return joblib.load(SCALER_X_PATH)

def load_scaler_y():
    return joblib.load(SCALER_Y_PATH)

model = load_model()
scaler_x = load_scaler_x()
scaler_y = load_scaler_y()
