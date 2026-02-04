import pandas as pd
import numpy as np
import sys
from statsmodels.tsa.api import VAR
import matplotlib.pyplot as plt

# -----------------------------
# AUTO-SAVE OUTPUT
# -----------------------------
sys.stdout = open("IRF_Results.txt", "w")

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

print("===== IMPULSE RESPONSE FUNCTION (IRF) RESULTS =====")

# -----------------------------
# Generate IRF (12 months)
# -----------------------------
irf = var_model.irf(12)

# -----------------------------
# Plot orthogonalized IRFs
# -----------------------------
fig = irf.plot(orth=True)
fig.savefig("IRF_VAR1.png", dpi=300)

print("\nIRF plots generated and saved as IRF_VAR1.png")

# -----------------------------
# CLOSE OUTPUT FILE
# -----------------------------
sys.stdout.close()
