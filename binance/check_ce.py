
import ccxt
import pandas as pd
import ta
import time

# Set up the Binance exchange
exchange = ccxt.binance()

# Set up the symbol and timeframe
symbol = 'BTC/USDT'
timeframe = '1d'

# Calculate the Chandelier Exit
def chandelier_exit(high, low, close, n=22, k=3):
    atr = ta.volatility.AverageTrueRange(high=high, low=low, close=close, window=n)
    return max(high[-n:]) - atr[-1]*k

# Continuously check the Chandelier Exit and alert the user if the price falls below it
while True:
    # Get the Bitcoin price data
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df.set_index('timestamp', inplace=True)

    # Calculate the Chandelier Exit
    df['chandelier_exit'] = chandelier_exit(df['high'], df['low'], df['close'])

    # Get the current Bitcoin price
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']

    # Get the Chandelier Exit
    exit_point = df['chandelier_exit'].iloc[-1]

    # Alert the user if the price falls below the Chandelier Exit
    if price < exit_point:
        print(f"ALERT: Bitcoin price ({price}) is below the Chandelier Exit ({exit_point})")
        # You can also add code here to send an email or a text message to alert the user
        # For example, you can use the Twilio API to send text messages: https://www.twilio.com/docs/sms/send-messages
    else:
        print(f"Bitcoin price ({price}) is above the Chandelier Exit ({exit_point})")

    # Wait for 5 minutes before checking again
    time.sleep(300)
