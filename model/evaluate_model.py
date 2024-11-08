import pandas as pd
from sklearn.metrics import mean_squared_error
from load_model import load_model

def load_data():
    activity_df = pd.read_csv('data/processed/cleaned_daily_activity.csv')
    heartrate_df = pd.read_csv('data/processed/cleaned_daily_heartrate.csv')
    calories_df = pd.read_csv('data/processed/cleaned_daily_calories.csv')
    steps_df = pd.read_csv('data/processed/cleaned_daily_steps.csv')
    sleep_df = pd.read_csv('data/processed/cleaned_daily_sleep.csv')

    df = activity_df.merge(heartrate_df, on='date', how='inner')
    df = df.merge(calories_df, on='date', how='inner')
    df = df.merge(steps_df, on='date', how='inner')
    df = df.merge(sleep_df, on='date', how='inner')

    return df

def evaluate_model():
    # Load the trained model and scalers
    model = load_model("sleep_model.pkl")
    scaler_x = load_model("scaler_x.pkl")
    scaler_y = load_model("scaler_y.pkl")
    
    df = load_data()

    X = df[['TotalSteps', 'Calories', 'SedentaryMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'resting_heart_rate']]
    y_true = df['total_sleep_time'].values.reshape(-1, 1)

    X_scaled = scaler_x.transform(X)
    
    y_true_scaled = scaler_y.transform(y_true).ravel()

    # Predict using the scaled features
    y_pred_scaled = model.predict(X_scaled)

    # Calculate Mean Squared Error between scaled true and predicted values
    mse = mean_squared_error(y_true_scaled, y_pred_scaled)
    print(f"Evaluation Mean Squared Error: {mse}")

if __name__ == "__main__":
    evaluate_model()
