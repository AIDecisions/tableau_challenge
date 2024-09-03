import os
import pandas as pd

# Combine all csv files in the folder
def combine_csv(folder_path, output_file, sample_size):
    # Get all csv files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    print(f'Found {len(csv_files)} csv files in {folder_path}')
    
    # Read and sample each csv file
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(folder_path, file))
        sample_df = df.sample(n=sample_size, random_state=42)  # Modify the sample size as needed
        dfs.append(sample_df)
    
    # Concatenate all sampled dataframes
    combined_df = pd.concat(dfs)
    
    # Save the combined dataframe to a csv file
    combined_df.to_csv(output_file, index=False)
    print(f'Combined {len(csv_files)} csv files into {output_file}')

# Combine all csv files in the folder 'data' and save the result to 'combined_data.csv'
combine_csv('tableau_challenge/2023-data', 'tableau_challenge/Resources/combined_2023-citibike-tripdata.csv', 1000)

