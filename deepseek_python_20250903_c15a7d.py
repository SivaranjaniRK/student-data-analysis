## 2. Data Exploration

# Basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
df.info()
print("\nColumn Names:", df.columns.tolist())
print("\nSummary Statistics:")
df.describe()