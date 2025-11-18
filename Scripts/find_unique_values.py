import pandas as pd

def extract_unique_institutions(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file, encoding='utf-8')
    
    # Ensure the column exists
    if "Proj_Funding_Agency" not in df.columns:
        raise ValueError("The column 'Proj_Funding_Agency' was not found in the CSV file.")
    
    # Split values by " I ", flatten into a single list
    all_institutions = []
    for val in df["Proj_Funding_Agency"].dropna():
        parts = [p.strip() for p in val.split("|")]  # split by "|" and trim spaces
        all_institutions.extend(parts)
    
    # Get unique, sorted values
    unique_institutions = sorted(set(all_institutions))
    
    # Convert to DataFrame for export
    unique_df = pd.DataFrame(unique_institutions, columns=["Proj_Funding_Agency"])
    
    # Write to new CSV
    unique_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Unique separated values saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_csv = "./aov_data_revised3.csv"
    output_csv = "./unique_agencies_list.csv"
    extract_unique_institutions(input_csv, output_csv)