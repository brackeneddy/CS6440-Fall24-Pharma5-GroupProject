import pandas as pd
from data_loading import load_and_merge_data
import os

def clean_data(data_frames):
    processed_dir = 'data/processed'
    os.makedirs(processed_dir, exist_ok=True)
    
    daily_activity_df = data_frames.get("daily_activity")
    if daily_activity_df is not None:
        daily_activity_df['ActivityDate'] = pd.to_datetime(daily_activity_df['ActivityDate'])
        daily_activity_df = daily_activity_df.drop_duplicates()
        daily_activity_df.to_csv(os.path.join(processed_dir, 'cleaned_daily_activity.csv'), index=False)
        print("Cleaned and saved daily activity data")
    
    heartrate_df = data_frames.get("heartrate")
    if heartrate_df is not None:
        heartrate_df['datetime'] = pd.to_datetime(heartrate_df['Time'], format="%m/%d/%Y %I:%M:%S %p")
        heartrate_df = heartrate_df.drop_duplicates()
        daily_resting_hr = heartrate_df.groupby(heartrate_df['datetime'].dt.date)['Value'].min().reset_index()
        daily_resting_hr.columns = ['date', 'resting_heart_rate']
        daily_resting_hr.to_csv(os.path.join(processed_dir, 'cleaned_daily_heartrate.csv'), index=False)
        print("Cleaned and saved daily heartrate data")
    
    hourly_calories_df = data_frames.get("hourly_calories")
    if hourly_calories_df is not None:
        hourly_calories_df['ActivityHour'] = pd.to_datetime(hourly_calories_df['ActivityHour'], format="%m/%d/%Y %I:%M:%S %p")
        hourly_calories_df = hourly_calories_df.drop_duplicates()
        daily_calories = hourly_calories_df.groupby(hourly_calories_df['ActivityHour'].dt.date)['Calories'].sum().reset_index()
        daily_calories.columns = ['date', 'total_calories']
        daily_calories.to_csv(os.path.join(processed_dir, 'cleaned_daily_calories.csv'), index=False)
        print("Cleaned and saved daily calories data")

    hourly_steps_df = data_frames.get("hourly_steps")
    if hourly_steps_df is not None:
        hourly_steps_df['ActivityHour'] = pd.to_datetime(hourly_steps_df['ActivityHour'], format="%m/%d/%Y %I:%M:%S %p")
        hourly_steps_df = hourly_steps_df.drop_duplicates()
        daily_steps = hourly_steps_df.groupby(hourly_steps_df['ActivityHour'].dt.date)['StepTotal'].sum().reset_index()
        daily_steps.columns = ['date', 'total_steps']
        daily_steps.to_csv(os.path.join(processed_dir, 'cleaned_daily_steps.csv'), index=False)
        print("Cleaned and saved daily steps data")

    minute_sleep_df = data_frames.get("minute_sleep")
    if minute_sleep_df is not None:
        minute_sleep_df['date'] = pd.to_datetime(minute_sleep_df['date'])
        minute_sleep_df = minute_sleep_df.drop_duplicates()
        daily_sleep = minute_sleep_df.groupby(minute_sleep_df['date'].dt.date).agg(
            total_sleep_time=('value', 'sum')
        ).reset_index()
        daily_sleep.columns = ['date', 'total_sleep_time']
        daily_sleep.to_csv(os.path.join(processed_dir, 'cleaned_daily_sleep.csv'), index=False)
        print("Cleaned and saved daily sleep data")

    print("Data cleaning and daily aggregation complete for all datasets. Files saved in data/processed")

if __name__ == "__main__":
    data_frames = load_and_merge_data()

    clean_data(data_frames)
