### 6.2 Lunch Type Impact on Performance
lunch_performance = df.groupby("lunch")["total_score"].mean()
print("Average Total Score by Lunch Type:")
print(lunch_performance)

# Visualization
plt.figure(figsize=(8, 5))
lunch_performance.plot(kind='bar', color=['lightcoral', 'lightgreen'])
plt.title('Average Total Score by Lunch Type')
plt.xlabel('Lunch Type')
plt.ylabel('Average Total Score')
plt.xticks(rotation=0)
plt.show()