
import pandas as pd

funds = pd.read_csv("data/raw/fund_master.csv")
nav = pd.read_csv("data/raw/nav_history.csv")

print("Fund Master columns:")
print(funds.columns.tolist())

print("\nNAV History columns:")
print(nav.columns.tolist())

# Find likely scheme-code columns
fund_code_col = "amfi_code"
nav_code_col = "amfi_code"

# Validate code coverage
fund_codes = set(funds[fund_code_col].dropna().astype(str))
nav_codes = set(nav[nav_code_col].dropna().astype(str))

missing_codes = fund_codes - nav_codes

print("\nTotal fund master codes:", len(fund_codes))
print("Total NAV history codes:", len(nav_codes))
print("Fund codes absent from NAV history:", len(missing_codes))
print("Missing codes:", sorted(missing_codes)[:20])
