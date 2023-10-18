import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('')

# Read the second CSV file
df2 = pd.read_csv('')

# Combine the DataFrames, keeping only unique rows
combined_df = pd.concat([df1, df2]).drop_duplicates()

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('combined.csv', index=False)
