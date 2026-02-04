import pandas as pd
import numpy as np
import sys
from statsmodels.tsa.api import VAR

# -----------------------------
# AUTO-SAVE OUTPUT
# -----------------------------
sys.stdout = open("VAR_Results.txt", "w")

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
# Lag order selection
# -----------------------------
print("===== VAR LAG ORDER SELECTION =====")
model = VAR(var_data)
lag_selection = model.select_order(maxlags=6)
print(lag_selection.summary())

# -----------------------------
# Estimate VAR(1)
# -----------------------------
print("\n===== VAR(1) ESTIMATION RESULTS =====")
var_model = model.fit(1)
print(var_model.summary())

# -----------------------------
# Stability check
# -----------------------------
print("\n===== VAR STABILITY CHECK =====")
stability = var_model.is_stable(verbose=True)
print("VAR Stability:", stability)

# -----------------------------
# CLOSE OUTPUT FILE
# -----------------------------
sys.stdout.close()
