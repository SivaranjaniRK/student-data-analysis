### 6.3 Performance Category Distribution by Gender
performance_by_gender = pd.crosstab(df["gender"], df["performance_category"], normalize='index') * 100
print("Performance Category Distribution by Gender (%):")
print(performance_by_gender)

# Visualization
performance_by_gender.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Performance Category Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Percentage')
plt.xticks(rotation=0)
plt.legend(title='Performance Category')
plt.show()