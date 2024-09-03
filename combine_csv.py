import os
import pandas as pd

# Combine single csv file
def combine_single_csv(file_source, output_file):
    
# Combine all csv files in the folder
def combine_csv(folder_path, output_file):
    # Get all csv files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    print(f'Found {len(csv_files)} csv files in {folder_path}')
    # Read all csv files and concatenate them
    df = pd.concat([pd.read_csv(os.path.join(folder_path, f)) for f in csv_files])
    # Save the combined dataframe to a csv file
    df.to_csv(output_file, index=False)
    print(f'Combined {len(csv_files)} csv files into {output_file}')

# Combine all csv files in the folder 'data' and save the result to 'combined_data.csv'
combine_csv('tableau_challenge/2023-data', 'tableau_challenge/Resources/combined_2023-citibike-tripdata.csv')

