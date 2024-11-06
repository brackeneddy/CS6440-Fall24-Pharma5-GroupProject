import pandas as pd
import os

heartrate_file_path = 'raw/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv'

output_dir = os.path.dirname(heartrate_file_path)

if os.path.exists(heartrate_file_path):
    data = pd.read_csv(heartrate_file_path)

    chunk_size = len(data) // 2
    data_part1 = data.iloc[:chunk_size]
    data_part2 = data.iloc[chunk_size:]

    data_part1.to_csv(os.path.join(output_dir, 'heartrate_part1.csv'), index=False)
    data_part2.to_csv(os.path.join(output_dir, 'heartrate_part2.csv'), index=False)

    os.remove(heartrate_file_path)
    print("File split into heartrate_part1.csv and heartrate_part2.csv")
    print("Original file heartrate_seconds_merged.csv removed.")
else:
    print(f"Error: {heartrate_file_path} not found.")
