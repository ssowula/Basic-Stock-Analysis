# Basic Stock Analysis

A Python script for analyzing stock data using the `yfinance` package.  
It analyzes selected companies, calculates returns and risk (VaR), and generates comparison plots.

## Features

-Downloads daily historical data from Yahoo Finance  
-Calculations:  
    -Daily returns (based on open and close prices)  
    -Cumulative returns (only for dates common across all tickers)  
-Visualizations:  
    -Open vs Close price plot (for META)  
    -Histogram of daily returns with Value at Risk (VaR) markers  
    -Line plot comparing cumulative returns for multiple tickers  
-Value at Risk (VaR) metrics:  
    -Historical VaR  
    -Parametric VaR

## Analyzed Tickers

`META`  full analysis (statistics, plots, risk)  
`TSLA`, `AAPL`, `GOOGL`, `MSFT` — analyzed for return comparison

## Requirements

Install required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Run the script in terminal:

```bash
python Program.py
```

## Notes

-Date range: **2024-01-01 to 2025-01-01**  
-Only dates that are common across all tickers are included in cumulative return calculations
