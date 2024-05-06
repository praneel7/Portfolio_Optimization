import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


def getStockData(ticker):
    # Define the time period (last six months from today)
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=180)

    # Fetch data from Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)

    # Adjust data for splits
    data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    # Add ticker and date columns
    data['Ticker'] = ticker
    data['Date'] = data.index

    # Save data to CSV (individual for each ticker)
    data.to_csv(f'{ticker}_data.csv', index=False)
    return data


def mergeCSVs(tickers):
    # Merge individual CSV files into a main CSV file
    frames = [pd.read_csv(f'{ticker}_data.csv') for ticker in tickers]
    result = pd.concat(frames)
    result.to_csv('stock_data.csv', index=False)


# Example usage
tickers = ['AAPL', 'MSFT', 'GOOGL', 'SQ']  # Define your list of tickers here
for ticker in tickers:
    getStockData(ticker)
mergeCSVs(tickers)