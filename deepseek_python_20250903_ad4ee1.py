## 7. Key Findings and Conclusions

print("="*50)
print("KEY FINDINGS AND CONCLUSIONS")
print("="*50)

# 1. Gender differences
math_gap = gender_math['male'] - gender_math['female']
print(f"1. Gender Difference in Math: Males score {math_gap:.2f} points higher on average")

# 2. Test preparation impact
prep_benefit = test_prep_writing['completed'] - test_prep_writing['none']
print(f"2. Test Preparation Benefit: Completing test prep improves writing scores by {prep_benefit:.2f} points")

# 3. Top performing ethnicity
top_ethnicity = ethnicity_reading.index[0]
print(f"3. Highest Reading Performance: Group {top_ethnicity} has the highest average reading score")

# 4. Performance category distribution
excellent_pct = (df["performance_category"] == "Excellent").sum() / len(df) * 100
print(f"4. Excellence Rate: {excellent_pct:.1f}% of students perform excellently")

# 5. Correlation between subjects
max_corr = correlation_matrix.unstack().sort_values(ascending=False)[3:6].mean()
print(f"5. Subject Correlation: Math, reading, and writing scores are highly correlated (avg r = {max_corr:.3f})")

print("\nRECOMMENDATIONS:")
print("- Address gender gap in math performance through targeted interventions")
print("- Encourage test preparation course completion to improve scores")
print("- Develop support programs for underperforming student groups")
print("- Consider socioeconomic factors (lunch type) in educational support planning")