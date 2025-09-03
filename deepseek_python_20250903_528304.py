### 4.3 Ethnic group with highest average reading score
ethnicity_reading = df.groupby("race/ethnicity")["reading_score"].mean().sort_values(ascending=False)
print("Average Reading Score by Ethnicity:")
print(ethnicity_reading)

# Visualization
plt.figure(figsize=(10, 6))
ethnicity_reading.plot(kind='bar', color='lightgreen')
plt.title('Average Reading Score by Ethnicity')
plt.xlabel('Ethnicity')
plt.ylabel('Average Reading Score')
plt.xticks(rotation=45)
plt.show()