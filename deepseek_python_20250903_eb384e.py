## 3. Data Cleaning

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Rename columns to snake_case for consistency
df.columns = [col.replace(" ", "_").lower() for col in df.columns]
print("\nRenamed Columns:", df.columns.tolist())

# Create total_score column
df["total_score"] = df["math_score"] + df["reading_score"] + df["writing_score"]

# Display cleaned data
print("\nCleaned Data Preview:")
df.head()