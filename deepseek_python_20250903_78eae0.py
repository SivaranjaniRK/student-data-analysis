### 4.5 Correlation among Math, Reading, and Writing scores
correlation_matrix = df[["math_score", "reading_score", "writing_score"]].corr()
print("Correlation Matrix:")
print(correlation_matrix)

# Visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Among Scores')
plt.show()