import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def main():
    df = data_fetch("TSLA")
    basic_statistics(df)
    open_close_plot(df)
    calculate_daily_returns(df)
    calculate_cumulative_returns(df)
    value_at_risk(df, percentile=5.00)

def data_fetch(ticker : str):
    data = yf.download(ticker,start='2025-06-01',end='2025-07-01')
    df=pd.DataFrame(data)
    df=df.dropna()
    return df

def basic_statistics(df: pd.DataFrame):
    stats = df.describe()
    print(stats)

def open_close_plot(df: pd.DataFrame):
    open_price = df['Open']
    close_price = df['Close']
    time = df.index

    plt.figure(figsize=(20, 10))
    plt.plot(time, open_price, label='Open', color='green')
    plt.plot(time, close_price, label='Close', color='blue')
    plt.title('Open and Close prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()

def calculate_daily_returns(df: pd.DataFrame):
    daily_returns = ((df['Close'] - df['Open']) / df['Open'] * 100).round(2)
    df['Daily_returns'] = daily_returns
    print(df)

def calculate_cumulative_returns(df: pd.DataFrame):
    df['Cumulative_returns'] = (1+df['Daily_returns']/100).cumprod()
    loss = 1 - df['Cumulative_returns'].iloc[-1]
    print(f"Cumulative loss in June: {round(loss * 100, 2)}%")
    plt.figure(figsize=(20, 10))
    plt.plot(df['Cumulative_returns'])
    plt.title('Cumulative returns')
    plt.xlabel('Date')
    plt.ylabel('Return')

    plt.show()

def value_at_risk(df: pd.DataFrame, percentile : float):
    returns = df['Daily_returns'].dropna()
    var_value = np.percentile(returns, percentile)

    confidence_level = 100 - percentile

    print(f"Value at Risk (VaR) at {confidence_level:.0f}% confidence level: {var_value:.2f}%")



if __name__ == "__main__":
    main()