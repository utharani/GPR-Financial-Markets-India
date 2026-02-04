import pandas as pd
import numpy as np
import sys
from statsmodels.tsa.api import VAR

# -----------------------------
# AUTO-SAVE OUTPUT
# -----------------------------
sys.stdout = open("FEVD_Results.txt", "w")

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

print("===== FORECAST ERROR VARIANCE DECOMPOSITION (FEVD) =====")

# -----------------------------
# FEVD (12-month horizon)
# -----------------------------
fevd = var_model.fevd(12)

print(fevd.summary())

# -----------------------------
# CLOSE OUTPUT FILE
# -----------------------------
sys.stdout.close()
