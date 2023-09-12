# To send an email alert when the MACD 4-hour crosses on BTC, you will need to use a cryptocurrency exchange API to retrieve the price data and a technical analysis library to calculate the MACD indicator. You will also need to set up an email account to send the alert.
#
# Here is an example Python code that uses the Binance API and TA-Lib library to check for MACD 4-hour crosses on BTC/USDT pair and sends an email alert using the `smtplib` library:
#
# ```python

import os
import time
import numpy as np
import talib as ta
import smtplib
from binance.client import Client
from email.mime.text import MIMEText


# Binance API credentials
# api_key = os.environ.get(api_key)
# api_secret = os.environ.get(api_secret)
api_key = 'VLQd7y0l2OQhtWZz3TWCjSyV3m7Yuip095BbAjrEZuzcUGl3aSgqR5JkUTbblGrX'
api_secret = '4vXfyk8L2mdH62mKahTzD0CCVt9dgjlIWgeBUZYfN0kMTVofAoUg48CJzZjMFTuP'

client = Client(api_key, api_secret)

# Email credentials
email_address = os.environ.get('chisato666@gmail.com')
email_password = os.environ.get('socool')
recipient_address = 'kenji_so@yahoo.com'

# MACD parameters
fast_period = 12
slow_period = 26
signal_period = 9

# Retrieve BTC/USDT 4-hour candle data
candles = client.futures_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_4HOUR)
# Extract close prices and calculate MACD
close_prices = [float(candle[4]) for candle in candles]
#output= ta.SMA(close_prices,timeperiod=30)

#macd = ta.MACD(close_prices, fast_period=fast_period, slow_period=slow_period, signal_period=signal_period)
#macd = ta.MACD(close_prices, fast_period, slow_period, signal_period)

macd = ta.trend.macd(np.array(close_prices), fastperiod=fast_period, slowperiod=slow_period, signalperiod=signal_period)

print(macd)

# Check if MACD crossed
if macd.macd[-2] < macd.signal[-2] and macd.macd[-1] > macd.signal[-1]:
    # Send email alert
    message = MIMEText('MACD 4h crossed on BTC/USDT')
    message['From'] = email_address
    message['To'] = recipient_address
    message['Subject'] = 'MACD 4h Cross Alert'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_address, email_password)
        smtp.send_message(message)
# ```
#
# In this example code, the `os.environ.get()` function is used to retrieve sensitive information like API keys and email credentials from environment variables, which are set up separately to avoid hard-coding them in the code. You will need to replace the placeholders in the variables `api_key`, `api_secret`, `email_address`, and `email_password` with your own values. The `recipient_address` variable should be set to the email address that you want to receive the alert.
#
# The code retrieves the 4-hour candle data for the BTC/USDT pair using the `futures_klines()` function from the Binance API. It extracts the close prices and calculates the MACD using the `MACD()` function from the TA-Lib library. The `[-2]` and `[-1]` indexing is used to access the last two values of the MACD and signal lines, which are used to check if they crossed.
#
# If the MACD crossed, the code composes an email message using the `MIMEText()` function. It sets the sender, recipient, and subject of the email message, and sends it using the `smtplib.SMTP()` function, which connects to the SMTP server of the email provider (in this case, Gmail) and authenticates using the email credentials.