
# ============================================
# PROJECT: EMPLOYEE CUSTOMER DATA ANALYSIS
# TASK 1: DATA CLEANING
# ============================================

# 1. IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# 2. SET PROJECT PATHS

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "employee_raw.csv"
REPORT_PATH = BASE_DIR / "reports"
FIGURE_PATH = REPORT_PATH / "figures"

# Create output folders if they don't exist
REPORT_PATH.mkdir(parents=True, exist_ok=True)
FIGURE_PATH.mkdir(parents=True, exist_ok=True)

# 3. LOAD DATASET

df = pd.read_csv(DATA_PATH)

print("\n========== ORIGINAL DATASET ==========")

print(df.head())

print("\nOriginal Shape:", df.shape)

# Keep original dataset for comparison
raw_df = df.copy()

# 4. INITIAL DATA INSPECTION

print("\n========== DATASET INFORMATION ==========")

df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# 5. BEFORE CLEANING SUMMARY

before_rows = len(df)
before_missing = int(df.isnull().sum().sum())
before_duplicates = int(df.duplicated().sum())

# 6. STANDARDISE EMPTY VALUES

# Convert empty strings and spaces into missing values
df = df.replace(r"^\s*$", np.nan, regex=True)

# 7. FIX DATA TYPES

# Employee ID as string
df["Employee_ID"] = df["Employee_ID"].astype("string")

# Employee name as string
df["Employee_Name"] = df["Employee_Name"].astype("string")

# Convert salary from text to numeric
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

print("\n========== DATA TYPES AFTER CONVERSION ==========")

print(df.dtypes)

# 8. REMOVE DUPLICATES

duplicate_count = df.duplicated().sum()

print("\nDuplicates Found:", duplicate_count)

df = df.drop_duplicates()

print("Duplicates After Removal:", df.duplicated().sum())

# 9. HANDLE MISSING VALUES

print("\n========== MISSING VALUE TREATMENT ==========")

# Remove records where Employee_ID is missing
df = df.dropna(subset=["Employee_ID"])

# Remove records where Employee_Name is missing
df = df.dropna(subset=["Employee_Name"])

# Fill missing Salary using median
salary_median = df["Salary"].median()

df["Salary"] = df["Salary"].fillna(salary_median)

print("Salary Median:", salary_median)

print("\nMissing Values After Treatment:")
print(df.isnull().sum())

# 10. STANDARDISE TEXT

# Remove leading and trailing spaces
df["Employee_Name"] = df["Employee_Name"].str.strip()

# Convert names to title case
df["Employee_Name"] = df["Employee_Name"].str.title()

# Remove unnecessary spaces between words
df["Employee_Name"] = df["Employee_Name"].str.replace(
    r"\s+", " ", regex=True
)

print("\n========== STANDARDISED EMPLOYEE NAMES ==========")

print(df["Employee_Name"])

# 11. DETECT OUTLIERS USING IQR

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit)
].copy()

print("\n========== OUTLIER DETECTION ==========")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nDetected Outliers:")

print(outliers[["Employee_ID", "Salary"]])

# Decision: Retain outliers and flag them
df["Outlier_Flag"] = np.where(
    (df["Salary"] < lower_limit) |
    (df["Salary"] > upper_limit),
    "Yes",
    "No"
)

# Save outlier report
outliers.to_csv(
    REPORT_PATH / "outlier_report.csv",
    index=False
)

# 12. CREATE BOXPLOT

plt.figure(figsize=(8, 5))

sns.boxplot(x=df["Salary"])

plt.title("Employee Salary - Outlier Detection")
plt.xlabel("Salary")

plt.tight_layout()

plt.savefig(
    FIGURE_PATH / "box_plot.png",
    dpi=300
)

plt.show()

# 13. AFTER CLEANING SUMMARY

after_rows = len(df)

after_missing = int(df.isnull().sum().sum())

after_duplicates = int(df.duplicated().sum())

# Create comparison table
summary = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Missing Values",
        "Duplicate Rows"
    ],

    "Before Cleaning": [
        before_rows,
        before_missing,
        before_duplicates
    ],

    "After Cleaning": [
        after_rows,
        after_missing,
        after_duplicates
    ]
})

print("\n========== BEFORE AND AFTER SUMMARY ==========")

print(summary.to_string(index=False))

# Save summary
summary.to_csv(
    REPORT_PATH / "cleaning_summary.csv",
    index=False
)

# 14. SAVE CLEANED DATASET

df.to_csv(
    REPORT_PATH / "clean_data.csv",
    index=False
)

# 15. FINAL VALIDATION

print("\n========== FINAL DATA VALIDATION ==========")

print("Final Shape:", df.shape)

print("Missing Values:", df.isnull().sum().sum())

print("Duplicate Rows:", df.duplicated().sum())

print("\nCleaned Dataset:")

print(df.to_string(index=False))

print("\n==========================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("==========================================")

print("\nGenerated Files:")

print("1. reports/clean_data.csv")
print("2. reports/cleaning_summary.csv")
print("3. reports/outlier_report.csv")
print("4. reports/figures/box_plot.png")

"""
PS C:\training_1\day_5\ai-training-repo> python .\notebooks\employee_cleaning.py

========== ORIGINAL DATASET ==========
  Employee_ID  Employee_Name   Salary
0        E001    arun kumar   45000.0
1        E002   PRIYA SHARMA  52000.0
2        E003         Ravi    48000.0
3        E004          Meena      NaN
4        E005     JOHN PETER  61000.0

Original Shape: (10, 3)

========== DATASET INFORMATION ==========
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Employee_ID    10 non-null     str    
 1   Employee_Name  9 non-null      str    
 2   Salary         9 non-null      float64
dtypes: float64(1), str(2)
memory usage: 372.0 bytes

Missing Values:
Employee_ID      0
Employee_Name    1
Salary           1
dtype: int64

Duplicate Rows:
1

Statistical Summary:
       Employee_ID Employee_Name         Salary
count           10             9       9.000000
unique           9             8            NaN
top           E008    Arun Kumar            NaN
freq             2             2            NaN
mean           NaN           NaN  145555.555556
std            NaN           NaN  283123.696956
min            NaN           NaN   39000.000000
25%            NaN           NaN   45000.000000
50%            NaN           NaN   48000.000000
75%            NaN           NaN   61000.000000
max            NaN           NaN  900000.000000

========== DATA TYPES AFTER CONVERSION ==========
Employee_ID       string
Employee_Name     string
Salary           float64
dtype: object

Duplicates Found: 1
Duplicates After Removal: 0

========== MISSING VALUE TREATMENT ==========
Salary Median: 52000.0

Missing Values After Treatment:
Employee_ID      0
Employee_Name    0
Salary           0
dtype: int64

========== STANDARDISED EMPLOYEE NAMES ==========
0      Arun Kumar
1    Priya Sharma
2            Ravi
3           Meena
4      John Peter
6         Kavitha
7      Arun Kumar
9          Suresh
Name: Employee_Name, dtype: string

========== OUTLIER DETECTION ==========
Q1: 47250.0
Q3: 64500.0
IQR: 17250.0
Lower Limit: 21375.0
Upper Limit: 90375.0

Detected Outliers:
  Employee_ID    Salary
9        E010  900000.0

========== BEFORE AND AFTER SUMMARY ==========
        Metric  Before Cleaning  After Cleaning
    Total Rows               10               8
Missing Values                2               0
Duplicate Rows                1               0

========== FINAL DATA VALIDATION ==========
Final Shape: (8, 4)
Missing Values: 0
Duplicate Rows: 0

Cleaned Dataset:
Employee_ID Employee_Name   Salary Outlier_Flag
       E001    Arun Kumar  45000.0           No
       E002  Priya Sharma  52000.0           No
       E003          Ravi  48000.0           No
       E004         Meena  52000.0           No
       E005    John Peter  61000.0           No
       E007       Kavitha  75000.0           No
       E008    Arun Kumar  45000.0           No
       E010        Suresh 900000.0          Yes

==========================================
DATA CLEANING COMPLETED SUCCESSFULLY!
==========================================

Generated Files:
1. reports/clean_data.csv
2. reports/cleaning_summary.csv
3. reports/outlier_report.csv
4. reports/figures/box_plot.png
"""