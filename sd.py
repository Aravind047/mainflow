import pandas as pd

# Read the CSV file
df = pd.read_csv('your_file.csv')

# Display initial data
print("Initial Data:")
print(df.head())

# Handling Missing Values
# Option 1: Drop rows with any missing values
df.dropna(inplace=True)

# Option 2: Fill missing values with a specific value
# df.fillna(value, inplace=True)

# Option 3: Fill missing values with the mean of the column
# df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Display cleaned data
print("Cleaned Data:")
print(df.head())

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_data.csv', index=False)