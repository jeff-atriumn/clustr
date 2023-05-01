import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt

# Define the file path pattern for each dataset
self_rated_files = "data/self_rated_data_*.parquet"
measureables_files = "data/measureables_data_*.parquet"
sleep_files = "data/sleep_data_*.parquet"
osteology_files = "data/osteology_data_*.parquet"
hydration_files = "data/hydration_data_*.parquet"
oral_files = "data/oral_health_data_*.parquet"

# Read and concatenate all the files for each dataset
self_rated_data = pd.concat([pd.read_parquet(f) for f in glob.glob(self_rated_files)], ignore_index=True)
measureables_data = pd.concat([pd.read_parquet(f) for f in glob.glob(measureables_files)], ignore_index=True)
sleep_data = pd.concat([pd.read_parquet(f) for f in glob.glob(sleep_files)], ignore_index=True)
osteology_data = pd.concat([pd.read_parquet(f) for f in glob.glob(osteology_files)], ignore_index=True)
hydration_data = pd.concat([pd.read_parquet(f) for f in glob.glob(hydration_files)], ignore_index=True)
oral_data = pd.concat([pd.read_parquet(f) for f in glob.glob(oral_files)], ignore_index=True)

# Merge the datasets
merged_data = self_rated_data.merge(measureables_data, on=["participant_id", "date_measured"], how="outer")
merged_data = merged_data.merge(sleep_data, on=["participant_id", "date_measured"], how="outer")
merged_data = merged_data.merge(osteology_data, on=["participant_id", "date_measured"], how="outer")
merged_data = merged_data.merge(hydration_data, on=["participant_id", "date_measured"], how="outer")
merged_data = merged_data.merge(oral_data, on=["participant_id", "date_measured"], how="outer")

# Sort the merged data by participant_id and date_measured
merged_data = merged_data.sort_values(by=["participant_id", "date_measured"]).reset_index(drop=True)

print(merged_data)
print(merged_data.columns)


quality_mapping = {
    "Poor": 1,
    "Fair": 2,
    "Good": 3,
    "Very good": 4,
    "Excellent": 5
}

merged_data["status"] = merged_data["status"].map(quality_mapping)

# Split the blood pressure values into systolic and diastolic
merged_data[['systolic_bp', 'diastolic_bp']] = merged_data['blood_pressure'].str.split('/', expand=True)

# Convert the new columns to numeric values
merged_data['systolic_bp'] = pd.to_numeric(merged_data['systolic_bp'], errors='coerce')
merged_data['diastolic_bp'] = pd.to_numeric(merged_data['diastolic_bp'], errors='coerce')

# Drop the original blood pressure column
merged_data = merged_data.drop(columns=['blood_pressure'])
merged_data.fillna(method='ffill', inplace=True)

# Calculate summary statistics for each numerical column
print("Summary statistics:")
print(merged_data.describe())

# Visualize the distribution of each numerical column
# for col in merged_data.select_dtypes(include=['number']).columns:
#     plt.figure()
#     sns.histplot(data=merged_data, x=col, kde=True)
#     plt.title(f"Distribution of {col}")
#     plt.show()

# # Visualize the distribution of categorical variables (e.g., self-rated status)
# categorical_columns = ["status"]  # Add more categorical columns if needed
# for col in categorical_columns:
#     plt.figure()
#     sns.countplot(data=merged_data, x=col)
#     plt.title(f"Distribution of {col}")
#     plt.show()

print(merged_data.dtypes)

# Analyze correlations between numerical columns
plt.figure()
sns.heatmap(merged_data.select_dtypes(include=[float, 'int64']).corr(), annot=True, cmap="coolwarm", center=0)


plt.title("Correlation Matrix")
plt.show()

# Pairplot to visualize relationships between numerical columns (optional, can be slow for large datasets)
# sns.pairplot(merged_data)
# plt.show()
