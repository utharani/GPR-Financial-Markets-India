import pandas as pd
import numpy as np
import sys
from statsmodels.tsa.api import VAR

# -----------------------------
# AUTO-SAVE OUTPUT
# -----------------------------
sys.stdout = open("Granger_Causality.txt", "w")

# -----------------------------
# Load monthly data
# -----------------------------
data = pd.read_excel("../data/merged_monthly_data.xlsx")

data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# -----------------------------
# Variable transformations
# -----------------------------
data['dlog_Gold'] = np.log(data['Gold']).diff()
data['d_Nifty'] = data['Nifty'].diff()
data['d_USDINR'] = data['USDINR'].diff()

var_data = data[['GPR', 'dlog_Gold', 'd_Nifty', 'd_USDINR']].dropna()

# -----------------------------
# Estimate VAR(1)
# -----------------------------
model = VAR(var_data)
var_model = model.fit(1)

print("===== GRANGER CAUSALITY TESTS (WALD) =====\n")

# GPR causing others
print("GPR -> Gold")
print(var_model.test_causality('dlog_Gold', ['GPR'], kind='wald').summary())

print("\nGPR -> Nifty")
print(var_model.test_causality('d_Nifty', ['GPR'], kind='wald').summary())

print("\nGPR -> USDINR")
print(var_model.test_causality('d_USDINR', ['GPR'], kind='wald').summary())

# Reverse causality
print("\nGold -> GPR")
print(var_model.test_causality('GPR', ['dlog_Gold'], kind='wald').summary())

print("\nNifty -> GPR")
print(var_model.test_causality('GPR', ['d_Nifty'], kind='wald').summary())

print("\nUSDINR -> GPR")
print(var_model.test_causality('GPR', ['d_USDINR'], kind='wald').summary())

# Cross-market causality
print("\nGold -> Nifty")
print(var_model.test_causality('d_Nifty', ['dlog_Gold'], kind='wald').summary())

print("\nGold -> USDINR")
print(var_model.test_causality('d_USDINR', ['dlog_Gold'], kind='wald').summary())

print("\nNifty -> USDINR")
print(var_model.test_causality('d_USDINR', ['d_Nifty'], kind='wald').summary())

# -----------------------------
# CLOSE OUTPUT FILE
# -----------------------------
sys.stdout.close()
