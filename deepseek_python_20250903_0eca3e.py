### 4.2 Top 5 students with highest total score
top_students = df.nlargest(5, "total_score")[["gender", "race/ethnicity", "parental_level_of_education", 
                                              "test_preparation_course", "math_score", "reading_score", 
                                              "writing_score", "total_score"]]
print("Top 5 Students by Total Score:")
top_students