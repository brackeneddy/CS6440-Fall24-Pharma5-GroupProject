import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from save_model import save_model
import glob

def load_data():
    def load_processed_data(filename_base):
        files = glob.glob(f'../data/processed/{filename_base}_part*.csv')
        dataframes = [pd.read_csv(file) for file in files]
        return pd.concat(dataframes, ignore_index=True)

    activity_df = load_processed_data('cleaned_daily_activity.csv')
    heartrate_df = load_processed_data('cleaned_daily_heartrate.csv')
    calories_df = load_processed_data('cleaned_daily_calories.csv')
    steps_df = load_processed_data('cleaned_daily_steps.csv')
    sleep_df = load_processed_data('cleaned_daily_sleep.csv')

    if 'ActivityDate' in activity_df.columns:
        activity_df.rename(columns={'ActivityDate': 'date'}, inplace=True)
    if 'Time' in heartrate_df.columns:
        heartrate_df.rename(columns={'Time': 'date'}, inplace=True)
    if 'ActivityHour' in calories_df.columns:
        calories_df.rename(columns={'ActivityHour': 'date'}, inplace=True)
    if 'ActivityHour' in steps_df.columns:
        steps_df.rename(columns={'ActivityHour': 'date'}, inplace=True)
    if 'date' not in sleep_df.columns:
        sleep_df.rename(columns={'logId': 'date'}, inplace=True)

    df = activity_df.merge(heartrate_df, on='date', how='inner')
    df = df.merge(calories_df, on='date', how='inner')
    df = df.merge(steps_df, on='date', how='inner')
    df = df.merge(sleep_df, on='date', how='inner')

    return df

def train_model():
    df = load_data()

    # Select features and target variable
    X = df[['TotalSteps', 'Calories', 'SedentaryMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'resting_heart_rate']]
    y = df['total_sleep_time'].values.reshape(-1, 1)

    # Scale X and y separately
    scaler_x = MinMaxScaler()
    X_scaled = scaler_x.fit_transform(X)

    scaler_y = MinMaxScaler(feature_range=(0, 1))  # Scale target within 0-1 range
    y_scaled = scaler_y.fit_transform(y).ravel()

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    feature_importances = model.feature_importances_
    feature_names = ['TotalSteps', 'Calories', 'SedentaryMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes', 'resting_heart_rate']
    importance_dict = dict(zip(feature_names, feature_importances))
    
    print("Feature importances:")
    for feature, importance in importance_dict.items():
        print(f"{feature}: {importance}")

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    save_model(model, "sleep_model.pkl")
    save_model(scaler_x, "scaler_x.pkl")
    save_model(scaler_y, "scaler_y.pkl")

if __name__ == "__main__":
    train_model()
