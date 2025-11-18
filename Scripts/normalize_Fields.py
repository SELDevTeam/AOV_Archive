import pandas as pd

# File paths
aov_file = "./aov_data_revised2.csv"
unique_file = "./proj_institution_sorted.csv"
output_file = "./AOV_Data_Revised3.csv"

# Load CSVs
aov_df = pd.read_csv(aov_file, dtype=str).fillna('')  # fill NaN with empty string
unique_df = pd.read_csv(unique_file, dtype=str).fillna('')

# Preprocess unique institutions to make lookup easier
# We'll create a dictionary mapping each individual "Other" value to the "Proj_Institution_Revised"
lookup = {}
for _, row in unique_df.iterrows():
    other_entries = [x.strip() for x in row['Other'].split('|')]
    revised_name = row['Proj_Institution_Revised']
    for entry in other_entries:
        lookup[entry] = revised_name

# Process AOV_Data
def replace_institution(proj_institution):
    # Split the string by '|'
    entries = [x.strip() for x in proj_institution.split('|')]
    # Replace each entry if it's in the lookup
    replaced_entries = [lookup.get(entry, entry) for entry in entries]
    # Join back into a single string
    return '|'.join(replaced_entries)

# Apply replacement row by row
aov_df['Proj_Institution'] = aov_df['Proj_Institution'].apply(replace_institution)

# Save the revised CSV
aov_df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Revised CSV saved to {output_file}")