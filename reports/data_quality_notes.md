
# Day 1 – Data Quality Report

## 1. CSV Dataset Inspection
- Inspected 10 source CSV datasets using Pandas.
- Recorded row counts, column counts, and data types.
- Reviewed the first five records of each dataset.
- Checked missing values and duplicate rows.

## 2. Data Quality Findings

### monthly_sip_inflows.csv
- Total rows: 48
- Total columns: 6
- Missing cells: 12
- Duplicate rows: 0
- Further investigation is required to identify the affected columns and records.

### Other Source Datasets
- Missing values and duplicate rows were checked.
- No missing cells or exact duplicate rows were detected in the initial summary for the other eight datasets.

## 3. NAV Data Ingestion
- Retrieved NAV data from MFAPI for the requested mutual fund schemes.
- Saved API responses as CSV files in data/raw/.
- API failures, if any, should be documented.

## 4. Fund Master Validation
- Compared scheme codes in fund_master.csv with NAV history data.
- Validation results should be recorded based on the output of validate_funds.py.

## 5. Next Actions
- Investigate the 12 missing cells in monthly_sip_inflows.csv.
- Review any scheme codes absent from NAV history.
- Document any additional anomalies identified during validation.
