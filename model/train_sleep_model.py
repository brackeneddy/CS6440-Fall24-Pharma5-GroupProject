import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from save_model import save_model


def load_data():
    activity_df = pd.read_csv('../data/processed/cleaned_daily_activity.csv')
    heartrate_df = pd.read_csv('../data/processed/cleaned_daily_heartrate.csv')
    calories_df = pd.read_csv('../data/processed/cleaned_daily_calories.csv')
    steps_df = pd.read_csv('../data/processed/cleaned_daily_steps.csv')
    sleep_df = pd.read_csv('../data/processed/cleaned_daily_sleep.csv')

    # Ensure the 'date' column exists in all DataFrames
    if 'ActivityDate' in activity_df.columns:
        activity_df.rename(columns={'ActivityDate': 'date'}, inplace=True)
    if 'Time' in heartrate_df.columns:
        heartrate_df.rename(columns={'Time': 'date'}, inplace=True)
    if 'ActivityHour' in calories_df.columns:
        calories_df.rename(columns={'ActivityHour': 'date'}, inplace=True)
    if 'ActivityHour' in steps_df.columns:
        steps_df.rename(columns={'ActivityHour': 'date'}, inplace=True)
    if 'date' not in sleep_df.columns:
        sleep_df.rename(columns={'logId': 'date'}, inplace=True)  # Adjust if needed

    df = activity_df.merge(heartrate_df, on='date', how='inner')
    df = df.merge(calories_df, on='date', how='inner')
    df = df.merge(steps_df, on='date', how='inner')
    df = df.merge(sleep_df, on='date', how='inner')

    return df

def train_model():
    df = load_data()

    X = df[['TotalSteps', 'Calories', 'SedentaryMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'resting_heart_rate']]
    y = df['total_sleep_time']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    save_model(model, "sleep_model.pkl")

if __name__ == "__main__":
    train_model()
