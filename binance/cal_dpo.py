
import requests

def calculate_dpo(data):
    # Calculate DPO
    period = 20  # Adjust the period as needed
    dpo = data['close'] - data['close'].rolling(window=period).mean().shift(int(period/2) + 1)
    return dpo

def check_dpo_indicator(symbol):
    # Fetch historical price data
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract the close and open prices from the data
        close_prices = [float(entry[4]) for entry in data]
        open_prices = [float(entry[1]) for entry in data]
        # Create a Pandas DataFrame from the prices
        import pandas as pd
        df = pd.DataFrame({'close': close_prices, 'open': open_prices})
        # Calculate DPO
        dpo = calculate_dpo(df)
        print(dpo)
        # Check if close price is higher than open price
        close_higher_than_open = dpo[dpo > 0]
        if not close_higher_than_open.empty:
            print(f"The DPO indicator shows that the close price is higher than the open price for {symbol}.")
        else:
            print(f"The DPO indicator does not show that the close price is higher than the open price for {symbol}.")
    else:
        print("Error fetching price data.")

# Usage
symbol = "BTCUSDT"
check_dpo_indicator(symbol)
# e fetches the historical price data for the BTCUSDT pair from the Binance API, calculates the DPO using a specified period (in this case, 20), and checks if the DPO values where the close price is higher than the open price exist. Adjust the period and customize the code further as per your requirements.