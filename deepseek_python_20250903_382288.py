### 4.4 Comparison of average writing score (test-prep vs no test-prep)
test_prep_writing = df.groupby("test_preparation_course")["writing_score"].mean()
print("Average Writing Score by Test Preparation:")
print(test_prep_writing)

# Visualization
plt.figure(figsize=(8, 5))
test_prep_writing.plot(kind='bar', color=['lightcoral', 'lightseagreen'])
plt.title('Average Writing Score by Test Preparation')
plt.xlabel('Test Preparation Course')
plt.ylabel('Average Writing Score')
plt.xticks(rotation=0)
plt.show()