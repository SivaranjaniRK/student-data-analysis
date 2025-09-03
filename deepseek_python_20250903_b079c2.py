# Student Performance Analysis with Python and Pandas

## Problem Statement
Examination results are a crucial indicator of student learning outcomes.  
The aim of this project is to analyze **student exam scores** and identify factors that impact performance—such as **gender**, **ethnicity**, **parental education**, **and test preparation**.

### Dataset
- **Source**: Students Performance in Exams (Kaggle)
- **Size**: 1000 rows × 8 columns (lightweight, beginner-friendly)
- **Columns**: Gender, Ethnicity, Parental Education, Lunch, Test Preparation, Math Score, Reading Score, Writing Score

## 1. Import Libraries and Load Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display first few rows
print("Dataset Preview:")
df.head()