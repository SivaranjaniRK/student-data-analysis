## 6. Additional Insights

### 6.1 Performance by Parental Education
parental_performance = df.groupby("parental_level_of_education")["total_score"].mean().sort_values(ascending=False)
print("Average Total Score by Parental Education:")
print(parental_performance)

# Visualization
plt.figure(figsize=(10, 6))
parental_performance.plot(kind='bar', color='skyblue')
plt.title('Average Total Score by Parental Education')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Total Score')
plt.xticks(rotation=45)
plt.show()