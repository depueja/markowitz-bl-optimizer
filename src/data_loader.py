import yfinance as yf
import pandas as pd

def load_data(tickers, start_date, end_date):
    """
    Download adjusted close prices for given tickers and compute daily returns.
    """
    data = yf.download(tickers, start=start_date, end=end_date)["Close"]
    returns = data.pct_change().dropna()
    return data, returns
