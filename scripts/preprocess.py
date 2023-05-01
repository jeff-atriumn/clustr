import pandas as pd
import glob

# Define the file path pattern for each dataset
self_rated_files = "data/self_rated_data_*.parquet"
measureables_files = "data/measureables_data_*.parquet"
sleep_files = "data/sleep_data_*.parquet"

# Read and concatenate all the files for each dataset
self_rated_data = pd.concat([pd.read_parquet(f) for f in glob.glob(self_rated_files)], ignore_index=True)
measureables_data = pd.concat([pd.read_parquet(f) for f in glob.glob(measureables_files)], ignore_index=True)
sleep_data = pd.concat([pd.read_parquet(f) for f in glob.glob(sleep_files)], ignore_index=True)

# Merge the datasets
merged_data = self_rated_data.merge(measureables_data, on=["participant_id", "date_measured"], how="outer")
merged_data = merged_data.merge(sleep_data, on=["participant_id", "date_measured"], how="outer")

# Sort the merged data by participant_id and date_measured
merged_data = merged_data.sort_values(by=["participant_id", "date_measured"]).reset_index(drop=True)

print(merged_data)