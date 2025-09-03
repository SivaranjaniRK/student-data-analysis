## 5. Feature Engineering

# Create performance_category based on total_score
def categorize_performance(score):
    if score >= 240:
        return "Excellent"
    elif score >= 180:
        return "Good"
    else:
        return "Needs Improvement"

df["performance_category"] = df["total_score"].apply(categorize_performance)

# Display the new column
print("Performance Category Distribution:")
print(df["performance_category"].value_counts())

# Visualization
plt.figure(figsize=(8, 5))
df["performance_category"].value_counts().plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Student Performance Categories')
plt.xlabel('Performance Category')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()