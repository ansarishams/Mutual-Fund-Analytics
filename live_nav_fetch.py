
import requests
import pandas as pd
from pathlib import Path

schemes = {
    "HDFC_Top_100_Direct": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841",
}

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

for fund_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        result = response.json()

        df = pd.DataFrame(result["data"])

        if df.empty:
            print(f"No data found: {fund_name}")
            continue

        output_file = output_dir / f"{fund_name}_nav.csv"
        df.to_csv(output_file, index=False)

        print(f"\nFund: {fund_name}")
        print("Shape:", df.shape)
        print("Saved:", output_file)

    except (requests.RequestException, ValueError, KeyError) as error:
        print(f"Failed: {fund_name} - {error}")
