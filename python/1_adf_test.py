import pandas as pd
import numpy as np
import sys
from statsmodels.tsa.stattools import adfuller

# -----------------------------
# AUTO-SAVE OUTPUT
# -----------------------------
sys.stdout = open("ADF_Results.txt", "w")

# -----------------------------
# Load data
# -----------------------------
df = pd.read_excel("../data/merged_monthly_data.xlsx")

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# -----------------------------
# ADF test function
# -----------------------------
def adf_test(series, name):
    result = adfuller(series.dropna(), autolag='AIC')
    print(f"\nADF Test for {name}")
    print(f"ADF Statistic : {result[0]}")
    print(f"p-value       : {result[1]}")
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"   {key} : {value}")

    if result[1] <= 0.05:
        print("Result: Stationary (Reject H0)")
    else:
        print("Result: Non-Stationary (Fail to Reject H0)")

# -----------------------------
# LEVEL TESTS
# -----------------------------
print("\n===== ADF TESTS AT LEVEL =====")
adf_test(df['GPR'], 'GPR Index (Level)')
adf_test(df['Gold'], 'Gold Price (Level)')
adf_test(df['Nifty'], 'Nifty 50 (Level)')
adf_test(df['USDINR'], 'USD/INR (Level)')

# -----------------------------
# FIRST DIFFERENCE TESTS
# -----------------------------
df_diff = df.diff()

print("\n===== ADF TESTS AT FIRST DIFFERENCE =====")
adf_test(df_diff['GPR'], 'GPR Index (1st Difference)')
adf_test(df_diff['Nifty'], 'Nifty 50 (1st Difference)')
adf_test(df_diff['USDINR'], 'USD/INR (1st Difference)')

# -----------------------------
# GOLD: LOG FIRST DIFFERENCE
# -----------------------------
df['Gold_log'] = np.log(df['Gold'])
df['Gold_log_diff'] = df['Gold_log'].diff()

adf_test(df['Gold_log_diff'], 'Gold Price (Log First Difference)')

# -----------------------------
# CLOSE OUTPUT FILE
# -----------------------------
sys.stdout.close()
