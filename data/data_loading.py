import pandas as pd
import os

def load_and_merge_data():
    dir1 = './raw/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16'
    dir2 = './raw/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16'

    # File names to load from each directory
    files_to_load = {
        "daily_activity": "dailyActivity_merged.csv",
        "heartrate": "heartrate_seconds_merged.csv",
        "hourly_calories": "hourlyCalories_merged.csv",
        "hourly_steps": "hourlySteps_merged.csv",
        "minute_sleep": "minuteSleep_merged.csv"
    }

    data_frames = {}

    for key, file_name in files_to_load.items():
        file_path_1 = os.path.join(dir1, file_name)
        file_path_2 = os.path.join(dir2, file_name)

        df1 = None
        df2 = None

        if os.path.exists(file_path_1) and os.path.getsize(file_path_1) > 0:
            df1 = pd.read_csv(file_path_1)

        if os.path.exists(file_path_2) and os.path.getsize(file_path_2) > 0:
            df2 = pd.read_csv(file_path_2)

        if df1 is not None and df2 is not None:
            combined_df = pd.concat([df1, df2], ignore_index=True)
        elif df1 is not None:
            combined_df = df1
        elif df2 is not None:
            combined_df = df2
        else:
            print(f"Warning: Both files for {file_name} are empty or missing. Skipping.")
            continue

        data_frames[key] = combined_df

    heartrate_part1 = pd.read_csv('./raw/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/heartrate_part1.csv')
    heartrate_part2 = pd.read_csv('./raw/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/heartrate_part2.csv')
    data_frames["heartrate"] = pd.concat([heartrate_part1, heartrate_part2], ignore_index=True)

    return data_frames
