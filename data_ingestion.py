
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

csv_files = list(DATA_DIR.glob("*.csv"))

print("Total CSV files found:", len(csv_files))

quality_report = []

for file in csv_files:
    print("\n" + "=" * 50)
    print("File:", file.name)

    try:
        df = pd.read_csv(file)

        # 1. Rows and columns
        print("\nShape:", df.shape)

        # 2. Column data types
        print("\nData types:")
        print(df.dtypes)

        # 3. First five rows
        print("\nFirst five rows:")
        print(df.head())

        # 4. Missing values
        missing = df.isnull().sum()
        print("\nMissing values:")
        print(missing[missing > 0] if missing.any() else "None")

        # 5. Duplicate rows
        duplicates = df.duplicated().sum()
        print("\nDuplicate rows:", duplicates)

        # 6. Save summary
        quality_report.append({
            "file_name": file.name,
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_cells": int(df.isnull().sum().sum()),
            "duplicate_rows": int(duplicates)
        })

    except Exception as error:
        print("Error:", error)

# Save data quality report
report_df = pd.DataFrame(quality_report)
report_df.to_csv(REPORT_DIR / "data_quality_summary.csv", index=False)

print("\nData quality report saved in reports/data_quality_summary.csv")
