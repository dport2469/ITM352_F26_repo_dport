import csv
import os
from pathlib import Path


csv_path = Path(__file__).with_name("my_custom_sheet.csv")

if csv_path.is_file() and os.access(csv_path, os.R_OK):
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        employees = csv.DictReader(csv_file)
        annual_salaries = [
            float(row["Annual_Salary"].replace("$", "").replace(",", ""))
            for row in employees
            if row["Annual_Salary"]
        ]

    average_salary = sum(annual_salaries) / len(annual_salaries)
    maximum_salary = max(annual_salaries)
    minimum_salary = min(annual_salaries)

    print(f"Average Annual Salary: ${average_salary:,.2f}")
    print(f"Maximum Annual Salary: ${maximum_salary:,.2f}")
    print(f"Minimum Annual Salary: ${minimum_salary:,.2f}")
else:
    print(f"Cannot read file: {csv_path}")