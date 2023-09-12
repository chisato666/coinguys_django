
import time
from binance.client import Client
from datetime import datetime

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
# Enter your Binance API key and secret

api_key = 'VLQd7y0l2OQhtWZz3TWCjSyV3m7Yuip095BbAjrEZuzcUGl3aSgqR5JkUTbblGrX'
api_secret = '4vXfyk8L2mdH62mKahTzD0CCVt9dgjlIWgeBUZYfN0kMTVofAoUg48CJzZjMFTuP'

# Create a Binance client object
client = Client(api_key, api_secret)

# Define the list of cryptocurrencies to monitor
symbols = ['ETHUSDT', 'BTCUSDT']

# Define the percentage increase threshold
max_threshold = 0.5
min_threshold = -0.5

# Define the time interval in seconds
interval = 60

def send_mail():
    email_address = 'bitcontrol2018'
    email_password = 'xgvgtothglqfqhag'
    recipient_address = 'waishing1977@gmail.com'
    message = MIMEText('Increase 0.5%  on BTC/ETH')
    message['From'] = email_address
    message['To'] = recipient_address
    message['Subject'] = 'Increase 0.5%  on BTC/ETH'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_address, email_password)
        smtp.send_message(message)

while True:
    for symbol in symbols:
        # Get the current price of the cryptocurrency
        ticker = client.get_ticker(symbol=symbol)
        price = float(ticker['lastPrice'])
        dt = datetime.now()
        # Get the price 1 minute ago
        klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
        prev_price = float(klines[-2][4])

        # Calculate the percentage increase
        percent_increase = (price - prev_price) / prev_price * 100

        print(dt, price,prev_price,percent_increase)
        # Check if the percentage increase is above the threshold
        if (percent_increase >= max_threshold) or (percent_increase <= min_threshold):
            print(f"ALERT: {symbol} price increased by {percent_increase:.2f}% within 1 minute")
            send_mail()


    # Wait for the next interval
    time.sleep(interval)
