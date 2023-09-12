
import time
from binance.client import Client
import pandas as pd
import ta

# Initialize the Binance API client
api_key = 'VLQd7y0l2OQhtWZz3TWCjSyV3m7Yuip095BbAjrEZuzcUGl3aSgqR5JkUTbblGrX'
api_secret = '4vXfyk8L2mdH62mKahTzD0CCVt9dgjlIWgeBUZYfN0kMTVofAoUg48CJzZjMFTuP'

client = Client(api_key, api_secret)

def check_cond(symbol,interval,period):

    message=f"Symbol: {symbol}, Interval: {interval}, Period: {period} \n"
    cond_count=0
    threshold=0.05
    # Get the Klines data for the last 2 hours
    klines = client.get_historical_klines(symbol, interval, period)

    # Convert the Klines data to a pandas DataFrame
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

    # Convert the timestamp to a datetime object
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Set the timestamp column as the index
    df.set_index('timestamp', inplace=True)

    # Calculate the RSI using the ta library
    close=pd.to_numeric(df['close'],errors='coerce')

    rsi = ta.momentum.RSIIndicator(close, window=14)

    # Calculate the Bollinger Bands using the ta library
    bb = ta.volatility.BollingerBands(df['close'], window=20, window_dev=2)

    max_threshold = threshold
    min_threshold = -threshold
    # Get the current price of the cryptocurrency
    last_price = float(df['close'].iloc[-1])

    prev_price = float(df['close'].iloc[-2])
    ma_30 = float(df['close'].rolling(30).mean().iloc[-1])
    last_high = float(df['high'].max())
    last_low = float(df['low'].min())
    # Calculate the percentage increase
    percent_increase = (last_price - prev_price) / prev_price * 100

    percent_near_high=( last_high - last_price) / last_high * 100
    percent_near_low=(  last_price - last_low) / last_price * 100

    # Get the last RSI and Bollinger Band values
    last_rsi = rsi.rsi()[-1]
    last_bb_upper = bb.bollinger_hband()[-1]
    last_bb_lower = bb.bollinger_lband()[-1]

    # Get the last price from the Klines data


    print(f"last_price {last_price} last_rsi {last_rsi} last_bb_upper {last_bb_upper} last_bb_lower {last_bb_lower}\n ma30 {ma_30} last_low {last_low} last_high {last_high}")
    print(f"percent_increase {percent_increase} percent_near_high {percent_near_high} percent_near_low {percent_near_low}")
    # Check if the conditions are met
    if last_rsi > 70:
        message= message + "RSI is great than 70 \n"
        cond_count=cond_count+1
    if last_rsi < 30:
        message = message + "RSI is less than 30 \n"
        cond_count=cond_count+1
    if last_price < last_bb_lower:
        message = message + "Current price is less than the lower Bollinger Band. \n"
        cond_count=cond_count+1
    if last_price > last_bb_upper:
        message = message + "Current price is greater than the upper Bollinger Band. \n"
        cond_count=cond_count+1
    if percent_near_high < max_threshold:
        message = message + "Current price is near the highest price. \n"
        cond_count = cond_count + 1
    if percent_near_low < max_threshold:
        message = message + "Current price is near the lowest price. \n"
        cond_count = cond_count + 1

    if  cond_count==0:
        message= message + "Conditions not met."

    return cond_count,message

count,message= check_cond('BTCUSDT',"1h","50 hour ago UTC")

print(count,message)