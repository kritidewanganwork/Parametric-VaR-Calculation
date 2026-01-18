# ----------LIBRARIES-------------
from pickle import FALSE

import numpy as np
import yfinance as yf
from scipy.stats import norm

# ---------- USER INPUTS ----------
tickers = input("Enter tickers (comma-separated, e.g. AAPL,MSFT,GOOGL): ").split(",")
weights = np.array(
    list(map(float, input("Enter weights (comma-separated, sum to 1): ").split(",")))
)
confidence_level = float(input("Enter confidence level (e.g. 0.95 or 0.99): "))
holding_period_days = int(input("Enter holding period (days): "))
portfolio_value = float(input("Enter portfolio value: USD"))
lookback_window = int(input("Enter lookback window (days): "))

# --------DOWNLOAD DATA FROM YAHOO FINANCE----------
prices = yf.download(
    tickers,
    period="1y",
    interval="1d",
    auto_adjust=True,
    progress = False
)["Close"]

# ---------- RETURNS ----------
returns = np.log(prices / prices.shift(1)).dropna()
portfolio_returns = returns @ weights

# ---------- PARAMETER ESTIMATION ----------
recent_returns = portfolio_returns.tail(lookback_window)
mu = recent_returns.mean()
sigma = recent_returns.std()

# ---------- STATIC VAR ----------
z = norm.ppf(1-confidence_level)
var_1d = z * sigma - mu
var_hp = var_1d * np.sqrt(holding_period_days)
var_amount = abs(var_hp) * portfolio_value

# ---------- OUTPUT ----------
print("\nStatic Parametric VaR (Snapshot)")
print("--------------------------------")
print(f"Estimated mean return: {mu:.6f}")
print(f"Estimated volatility: {sigma:.6f}")
print(f"VaR amount: USD{var_amount:,.4f}")