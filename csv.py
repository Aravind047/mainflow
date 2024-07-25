import pandas as pd

# Read the CSV file
df = pd.read_csv('your_file.csv')

# View the first few rows
print(df.head())

# Filter the data
filtered_df = df[df['age'] > 30]

# Add a new column
filtered_df['age_times_two'] = filtered_df['age'] * 2

# Group by a column and sum another column
grouped_df = filtered_df.groupby('gender').agg({'salary': 'sum'})

# Save the modified DataFrame to a new CSV file
grouped_df.to_csv('filtered_grouped_data.csv', index=False)