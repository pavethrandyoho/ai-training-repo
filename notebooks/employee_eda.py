
# ============================================
# PROJECT: EMPLOYEE CUSTOMER DATA ANALYSIS
# TASK 2: EXPLORATORY DATA ANALYSIS
# ============================================

# 1. IMPORT LIBRARIES

import pandas as pd
import numpy as np
from pathlib import Path

# 2. SET PROJECT PATHS

BASE_DIR = Path(__file__).resolve().parent.parent

CLEAN_DATA = BASE_DIR / "reports" / "clean_data.csv"
BUDGET_DATA = BASE_DIR / "data" / "department_budget.csv"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

# 3. LOAD DATASETS

df = pd.read_csv(CLEAN_DATA)
budget = pd.read_csv(BUDGET_DATA)

print("\n========== EMPLOYEE DATA ==========")

print(df.head())

print("\nDataset Shape:", df.shape)

print("\n========== BUDGET DATA ==========")

print(budget)

# ============================================
# 4. SUMMARY STATISTICS
# ============================================

print("\n========== SUMMARY STATISTICS ==========")

numeric_columns = [
    "Age",
    "Salary",
    "Experience_Years",
    "Performance_Rating"
]

summary = df[numeric_columns].agg(
    ["mean", "median", "min", "max", "std"]
)

print(summary.round(2))

# Save summary statistics
summary.to_csv(
    REPORT_DIR / "eda_summary.csv"
)

# ============================================
# 5. GROUPBY DEPARTMENT ANALYSIS
# ============================================

print("\n========== DEPARTMENT ANALYSIS ==========")

department_analysis = df.groupby(
    "Department"
).agg(
    Employee_Count=("Employee_ID", "count"),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median"),
    Total_Salary=("Salary", "sum"),
    Average_Experience=("Experience_Years", "mean"),
    Average_Performance=("Performance_Rating", "mean")
).round(2)

print(department_analysis)

department_analysis.to_csv(
    REPORT_DIR / "department_analysis.csv"
)

# ============================================
# 6. CITY-WISE ANALYSIS
# ============================================

print("\n========== CITY-WISE ANALYSIS ==========")

city_analysis = df.groupby("City").agg(
    Employee_Count=("Employee_ID", "count"),
    Average_Salary=("Salary", "mean"),
    Average_Experience=("Experience_Years", "mean")
).round(2)

print(city_analysis)

city_analysis.to_csv(
    REPORT_DIR / "city_analysis.csv"
)

# ============================================
# 7. GENDER-WISE ANALYSIS
# ============================================

print("\n========== GENDER ANALYSIS ==========")

gender_analysis = df.groupby("Gender").agg(
    Employee_Count=("Employee_ID", "count"),
    Average_Salary=("Salary", "mean"),
    Average_Performance=("Performance_Rating", "mean")
).round(2)

print(gender_analysis)

# ============================================
# 8. CONTRACT TYPE ANALYSIS
# ============================================

print("\n========== CONTRACT TYPE ANALYSIS ==========")

contract_analysis = df.groupby("Contract_Type").agg(
    Employee_Count=("Employee_ID", "count"),
    Average_Salary=("Salary", "mean"),
    Average_Experience=("Experience_Years", "mean")
).round(2)

print(contract_analysis)

# ============================================
# 9. CORRELATION ANALYSIS
# ============================================

print("\n========== CORRELATION MATRIX ==========")

correlation = df[numeric_columns].corr()

print(correlation.round(3))

# Extract top 3 unique relationships
correlation_pairs = correlation.where(
    np.triu(np.ones(correlation.shape), k=1).astype(bool)
).stack().reset_index()

correlation_pairs.columns = [
    "Variable_1",
    "Variable_2",
    "Correlation"
]

correlation_pairs["Absolute_Correlation"] = (
    correlation_pairs["Correlation"].abs()
)

top_3 = correlation_pairs.sort_values(
    by="Absolute_Correlation",
    ascending=False
).head(3)

print("\n========== TOP 3 CORRELATIONS ==========")

print(top_3.to_string(index=False))

top_3.to_csv(
    REPORT_DIR / "correlation_analysis.csv",
    index=False
)

# ============================================
# 10. BUSINESS QUESTIONS AND ANSWERS
# ============================================

print("\n========== BUSINESS QUESTIONS ==========")

# Question 1
highest_salary = df.loc[df["Salary"].idxmax()]

print("\nQ1. Which employee receives the highest salary?")

print(
    highest_salary["Employee_Name"],
    "- Salary:",
    highest_salary["Salary"]
)

# Question 2
highest_department = department_analysis[
    "Average_Salary"
].idxmax()

highest_department_salary = department_analysis[
    "Average_Salary"
].max()

print("\nQ2. Which department has the highest average salary?")

print(
    highest_department,
    "- Average Salary:",
    round(highest_department_salary, 2)
)

# Question 3
largest_city = city_analysis[
    "Employee_Count"
].idxmax()

largest_city_count = city_analysis[
    "Employee_Count"
].max()

print("\nQ3. Which city has the highest number of employees?")

print(
    largest_city,
    "- Employees:",
    largest_city_count
)

# Question 4
best_performance = df.groupby(
    "Department"
)["Performance_Rating"].mean().idxmax()

best_performance_score = df.groupby(
    "Department"
)["Performance_Rating"].mean().max()

print("\nQ4. Which department has the highest average performance?")

print(
    best_performance,
    "- Rating:",
    round(best_performance_score, 2)
)

# Question 5
most_experienced = df["Experience_Years"].mean()

print("\nQ5. What is the average employee experience?")

print(round(most_experienced, 2), "years")

# ============================================
# 11. MERGE EMPLOYEE AND BUDGET DATA
# ============================================

print("\n========== MERGING DATASETS ==========")

merged_df = pd.merge(
    df,
    budget,
    on="Department",
    how="left"
)

print(merged_df.head())

merged_df.to_csv(
    REPORT_DIR / "merged_employee_budget.csv",
    index=False
)

# ============================================
# 12. DEPARTMENT BUDGET ANALYSIS
# ============================================

print("\n========== DEPARTMENT BUDGET ANALYSIS ==========")

budget_analysis = merged_df.groupby(
    "Department"
).agg(
    Employee_Count=("Employee_ID", "count"),
    Total_Salary=("Salary", "sum"),
    Annual_Budget=("Annual_Budget", "first")
)

budget_analysis["Budget_Remaining"] = (
    budget_analysis["Annual_Budget"] -
    budget_analysis["Total_Salary"]
)

print(budget_analysis.round(2))

budget_analysis.to_csv(
    REPORT_DIR / "budget_analysis.csv"
)

# ============================================
# 13. FINAL OUTPUT
# ============================================

print("\n====================================")
print("EXPLORATORY DATA ANALYSIS COMPLETED")
print("====================================")

print("\nGenerated Reports:")

print("1. eda_summary.csv")
print("2. department_analysis.csv")
print("3. city_analysis.csv")
print("4. correlation_analysis.csv")
print("5. merged_employee_budget.csv")
print("6. budget_analysis.csv")


# ============================================
# 14. BONUS CHALLENGE - PIVOT TABLE
# ============================================

print("\n========== PIVOT TABLE ANALYSIS ==========")

# Compare Department and Gender
pivot_table = pd.pivot_table(
    df,
    values="Employee_ID",
    index="Department",
    columns="Gender",
    aggfunc="count",
    fill_value=0
)

print("\nEmployee Count by Department and Gender:")
print(pivot_table)

# Save pivot table
pivot_table.to_csv(
    REPORT_DIR / "department_gender_pivot.csv"
)

print("\nPivot table saved successfully!")

