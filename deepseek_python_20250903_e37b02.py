## 4. Data Analysis

### 4.1 Average Math Score by Gender
gender_math = df.groupby("gender")["math_score"].mean()
print("Average Math Score by Gender:")
print(gender_math)

# Visualization
plt.figure(figsize=(8, 5))
gender_math.plot(kind='bar', color=['lightpink', 'lightblue'])
plt.title('Average Math Score by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Math Score')
plt.xticks(rotation=0)
plt.show()