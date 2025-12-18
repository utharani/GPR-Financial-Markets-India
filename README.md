# Impact of Geopolitical Risk on Indian Financial Markets (2020–2025)

## 📘 Objective
To examine the impact of Geopolitical Risk (GPR) on:
- Gold prices
- Nifty 50 index
- USD/INR exchange rate

using monthly data from January 2020 to December 2025.---

## 📊 Data Sources
| Variable | Source |
|---------|--------|
| Geopolitical Risk Index (GPR) | Official Geopolitical Risk Database |
| Gold Prices | World Gold Council |
| Nifty 50 Index | Investing.com |
| USD/INR Exchange Rate | Investing.com |

Data was downloaded and aligned to a common monthly frequency for consistent analysis.

## 🧠 Methodology
The analysis so far includes:

1. **Descriptive statistics of individual variables**  
   Trend behavior, seasonal patterns, spikes.

2. **Moving average analysis (Actual, 3-month MA, 6-month MA)**  
   To examine short-run vs long-run patterns.

3. **Correlation analysis**  
   Pearson correlation between GPR and each financial variable.

4. **Stationarity checks (ADF intuition in Excel)**  
   First differences and visual stationarity checks.

5. **Econometric framework (planned / conceptual)**  
   - Vector Autoregression (VAR)  
   - Cointegration analysis  
   - Granger causality  
   - Impulse response functions
-
## 🛠 Tools Used
- **Microsoft Excel**: Descriptive analysis, correlation, stationarity checks  
- **Python (planned)**: Formal ADF tests, VAR estimation, causality, IRF

 
## 📁 Repository Structure

/data
/excel
/python
/report
/media

- All analyses and charts are saved in the `excel` and `media` folders.  
- Final scripts will be available in Python notebooks under `/python`.
