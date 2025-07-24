import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as st

def main():
    df = data_fetch("TSLA")
    basic_statistics(df)
    open_close_plot(df)
    calculate_daily_returns(df)
    calculate_cumulative_returns(df)
    h_var=historical_var(df, percentile=5.00)
    p_var=parametric_var(df, confidence_level=0.95)

    var_plot(df,h_var,p_var)

    print(df)

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

def historical_var(df: pd.DataFrame, percentile : float):
    returns = df['Daily_returns'].dropna()
    var_value = float(np.percentile(returns, percentile))

    confidence_level = 100 - percentile

    print(f"Historical Value at Risk (VaR) at {confidence_level:.0f}% confidence level: {var_value:.2f}%")
    return var_value

def parametric_var(df:pd.DataFrame,confidence_level : float):
    mu = df['Daily_returns'].mean()
    sigma = df['Daily_returns'].std()
    z=st.norm.ppf(1-confidence_level)
    var_value = mu + z*sigma
    print(f"Parametric Value at Risk (VaR) at {confidence_level*100:.0f}% confidence level: {var_value:.2f}%")
    return var_value

def var_plot(df: pd.DataFrame, h_var : float,p_var :float):
    daily_returns = df['Daily_returns']
    plt.figure(figsize=(12, 6))
    plt.hist(daily_returns, bins=40, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(h_var, color='red', linestyle='--', linewidth=2, label=f'Historical VaR: {h_var:.2f}%')
    plt.axvline(p_var, color='orange', linestyle='--', linewidth=2, label=f'Parametric VaR: {p_var:.2f}%')

    plt.title('Histogram of Daily Returns with Historical and Parametric VaR')
    plt.xlabel('Daily Return (%)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()