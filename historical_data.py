#impots

import yfinance as yf
import pandas as pd
import os
import time


# COnfiguration
INPUT_CSV = "HistoricalData - Sheet1.csv"
DATA_DIR = "historical_data"
DELAY_SECONDS = 1  # To avoid rate-limiting

def fetch_historical_data():
    # Create data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Read tickers from CSV
    df = pd.read_csv(INPUT_CSV, header=None, names=["Ticker", "Company"])
    tickers = df["Ticker"].tolist()
    
    # Fetch data for each ticker
    for ticker in tickers:
        try:
            print(f"Fetching data for {ticker}...")
            stock = yf.Ticker(ticker)
            hist_data = stock.history(period="20y")  # Last 20 years
            
            if hist_data.empty:
                print(f"No data found for {ticker}. Skipping.")
                continue
            
            
      # Save to CSV
            filepath = os.path.join(DATA_DIR, f"{ticker}_historical.csv")
            hist_data.to_csv(filepath)
            print(f"Saved data for {ticker} to {filepath}")
            
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
        
        time.sleep(DELAY_SECONDS)  # Delay between requests

if __name__ == "__main__":
    fetch_historical_data()
