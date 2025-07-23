import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def main():
    df = data_fetch("TSLA")

def data_fetch(ticker : str):
    data = yf.download(ticker,start='2025-06-01',end='2025-07-01')
    df=pd.DataFrame(data)
    return df

if __name__ == "__main__":
    main()