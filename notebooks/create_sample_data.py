
import pandas as pd
import numpy as np
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Reproducible sample data
np.random.seed(42)

departments = ["IT", "HR", "Finance", "Sales", "Marketing"]
cities = ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi"]
genders = ["Male", "Female"]
contracts = ["Permanent", "Contract", "Temporary"]

n = 100

df = pd.DataFrame({
    "Employee_ID": [f"E{i:03d}" for i in range(1, n + 1)],
    "Employee_Name": [f"Employee {i}" for i in range(1, n + 1)],
    "Age": np.random.randint(22, 56, n),
    "Gender": np.random.choice(genders, n),
    "Department": np.random.choice(departments, n),
    "City": np.random.choice(cities, n),
    "Salary": np.random.randint(25000, 100001, n),
    "Experience_Years": np.random.randint(0, 21, n),
    "Performance_Rating": np.random.randint(1, 6, n),
    "Contract_Type": np.random.choice(contracts, n)
})

# Add a few missing values for practice
df.loc[5, "Salary"] = np.nan
df.loc[10, "Department"] = np.nan
df.loc[15, "City"] = np.nan

# Save raw employee dataset
df.to_csv(DATA_DIR / "employee_raw.csv", index=False)

# Create department budget dataset
budget = pd.DataFrame({
    "Department": departments,
    "Annual_Budget": [2500000, 1200000, 1800000, 3000000, 2000000]
})

budget.to_csv(DATA_DIR / "department_budget.csv", index=False)

print("Sample datasets created successfully!")
print("Employee records:", len(df))
print("\nEmployee dataset:")
print(df.head())

print("\nDepartment budget:")
print(budget)
