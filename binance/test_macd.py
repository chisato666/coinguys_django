
import os
from binance.client import Client
import pandas as pd
import ta

# set up Binance API client
api_key = 'VLQd7y0l2OQhtWZz3TWCjSyV3m7Yuip095BbAjrEZuzcUGl3aSgqR5JkUTbblGrX'
api_secret = '4vXfyk8L2mdH62mKahTzD0CCVt9dgjlIWgeBUZYfN0kMTVofAoUg48CJzZjMFTuP'

client = Client(api_key, api_secret)

# get 4-hour candlestick data for BTCUSDT
candles = client.futures_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_4HOUR)

# convert data to pandas DataFrame
df = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

# drop unnecessary columns
df = df.drop(['close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'], axis=1)

# convert timestamps to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# set timestamp as index
df.set_index('timestamp', inplace=True)

# convert strings to floats
df['open'] = df['open'].astype(float)
df['high'] = df['high'].astype(float)
df['low'] = df['low'].astype(float)
df['close'] = df['close'].astype(float)

# calculate MACD indicator
macd = ta.trend.MACD(df['close'])
df['macd'] = macd.macd()
df['macd_signal'] = macd.macd_signal()
df['macd_hist'] = macd.macd_diff()

# check for MACD cross
if df['macd'].iloc[-2] < df['macd_signal'].iloc[-2] and df['macd'].iloc[-1] > df['macd_signal'].iloc[-1]:
    print("MACD just had a bullish cross on the 4-hour chart for BTCUSDT")
elif df['macd'].iloc[-2] > df['macd_signal'].iloc[-2] and df['macd'].iloc[-1] < df['macd_signal'].iloc[-1]:
    print("MACD just had a bearish cross on the 4-hour chart for BTCUSDT")
else:
    print("No MACD cross on the 4-hour chart for BTCUSDT")
#and calculates the MACD indicator using the `ta` library. It then checks for a MACD cross and prints a message indicating whether there was a bullish cross, a bearish cross, or no cross at all. Note that you will need to have the `binance` and `pandas` libraries installed, as well as the `ta` library for the MACD calculation. Also, you will need to set your Binance API key and secret as environment variables named `BINANCE_API_KEY` and `BINANCE_API_SECRET`, respectively.