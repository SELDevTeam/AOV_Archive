import pandas as pd

# Input CSV file path
input_csv = "./Unique_Funding_Agencies_2024-05021_abbrevColumn.csv"

# Output CSV file path
output_csv = "./unique_agencies_sorted.csv"

# Read the CSV file with UTF-8 encoding
df = pd.read_csv(input_csv, encoding='utf-8')

# Sort the DataFrame alphabetically by "Proj_Institution_Revised" column
df_sorted = df.sort_values(by="Proj_Funding_Agency_Normalized", key=lambda col: col.str.lower())

# Write the sorted DataFrame to a new CSV file with UTF-8 encoding
df_sorted.to_csv(output_csv, index=False, encoding='utf-8')

print(f"CSV file sorted by 'Proj_Funding_Agency_Normalized' and saved as '{output_csv}'")