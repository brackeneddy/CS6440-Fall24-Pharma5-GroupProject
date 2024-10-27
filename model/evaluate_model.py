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
    model = load_model("sleep_model.pkl")
    df = load_data()

    X = df[['TotalSteps', 'Calories', 'SedentaryMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'resting_heart_rate']]
    y_true = df['total_sleep_time']

    y_pred = model.predict(X)
    mse = mean_squared_error(y_true, y_pred)
    print(f"Evaluation Mean Squared Error: {mse}")

if __name__ == "__main__":
    evaluate_model()
