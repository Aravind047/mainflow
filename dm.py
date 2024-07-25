import pandas as pd

# Read the CSV file
df = pd.read_csv('your_file.csv')

# Display initial data
print("Initial Data:")
print(df.head())

# Filtering Data
# Example: Filter rows where 'age' is greater than 30
filtered_df = df[df['age'] > 30]
print("\nFiltered Data (age > 30):")
print(filtered_df.head())

# Sorting Data
# Example: Sort by 'salary' in descending order
sorted_df = df.sort_values(by='salary', ascending=False)
print("\nSorted Data by salary (descending):")
print(sorted_df.head())

# Grouping Data
# Example: Group by 'gender' and calculate the mean of 'salary'
grouped_df = df.groupby('gender').agg({'salary': 'mean'}).reset_index()
print("\nGrouped Data by gender with mean salary:")
print(grouped_df)

# Save the filtered, sorted, and grouped DataFrames to new CSV files
filtered_df.to_csv('filtered_data.csv', index=False)
sorted_df.to_csv('sorted_data.csv', index=False)
grouped_df.to_csv('grouped_data.csv', index=False)