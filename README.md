
# Employee Customer Data Analysis

## 1. Project Overview

This project analyses employee data using Python.

The main objectives are:

- Data cleaning
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data visualisation
- Business insights and recommendations

## 2. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 3. Project Structure

```text
ai-training-repo/
│
├── data/
│   ├── employee_raw.csv
│   └── department_budget.csv
│
├── notebooks/
│   └── employee_analysis.ipynb
│
├── reports/
│   ├── clean_data.csv
│   ├── cleaning_summary.csv
│   ├── eda_summary.csv
│   ├── project_report.md
│   ├── project_report.html
│   └── figures/
│       ├── bar_chart.png
│       ├── histogram.png
│       ├── scatter_plot.png
│       ├── line_chart.png
│       └── box_plot.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 4. Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project directory:

```bash
cd ai-training-repo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 5. How to Run the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/employee_analysis.ipynb
```

Run all notebook cells.

## 6. Analysis Performed

### Data Cleaning

- Handled missing values
- Removed duplicate records
- Fixed data types
- Standardised text
- Detected outliers using IQR

### Exploratory Data Analysis

- Summary statistics
- Department-wise analysis
- City-wise analysis
- Gender-wise analysis
- Correlation analysis
- Department budget merging
- Pivot table analysis

### Data Visualisation

- Bar chart
- Histogram
- Scatter plot
- Line chart
- Box plot

## 7. Business Questions

1. Which employee receives the highest salary?
2. Which department has the highest average salary?
3. Which city has the most employees?
4. Which department has the best average performance?
5. What is the average employee experience?

## 8. Project Reports

Reports are available inside the reports folder.

## 9. Limitations

This project uses synthetic practice data.
The findings should not be treated as actual
organisational employee statistics.

## 10. Conclusion

This project demonstrates the application of
Python-based data cleaning, EDA, visualisation
and reporting techniques.
