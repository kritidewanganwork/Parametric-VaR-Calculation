# Parametric Value at Risk (VaR) Calculation

This project implements a **Static Parametric (Variance–Covariance) VaR model**
to estimate potential losses of an equity portfolio under the assumption of
normally distributed returns.

The model is designed for **snapshot risk estimation** and is not intended for
backtesting or regulatory capital calculations.

## Objective
To calculate portfolio VaR using volatility, correlation, and confidence levels.

## Methodology

1. User inputs portfolio constituents, weights, confidence level,
   holding period, portfolio value, and lookback window.
2. Historical adjusted prices are downloaded from Yahoo Finance.
3. Log returns are calculated for each asset.
4. Portfolio returns are computed using user-defined weights.
5. Mean and volatility are estimated from a fixed historical lookback window.
6. Parametric VaR is computed using the normal distribution assumption.
7. Multi-day VaR is scaled using the square-root-of-time rule.

## Assumptions and Limitations

- Returns are assumed to be normally distributed.
- Volatility is assumed constant over the estimation window.
- Square-root-of-time scaling assumes i.i.d. returns.
- The model is **static** and does not include rolling recalibration or backtesting.

## Example Usage

Assets: AAPL, MSFT, GOOGL  
Weights: 0.40, 0.25, 0.35  
Confidence Level: 95%  
Holding Period: 10 days  
Lookback Window: 100 days  
Portfolio Value: $ 1,000,000 

Output:
Estimated mean return: 0.001964
Estimated volatility: 0.010352
VaR (95%, 10-day): ~ $60,000k

## Key Concepts

- Value at Risk (VaR)
- Holding Period
- Portfolio volatility
- Z-score and confidence levels

## Tools & Libraries

- Python
- NumPy
- SciPy

## Status

Initial version – input-based VaR calculation.

## Planned Enhancements

- Rolling-window VaR estimation
- VaR backtesting and exception analysis
- Comparison with Expected Shortfall
