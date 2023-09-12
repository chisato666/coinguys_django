# Certainly! Here's an example of a Python script that uses the Binance API to check the conditions you specified every minute:
#
# ```python
import time
import requests

import mysql.connector


database= "waishing_binance"
host=	"hkwaishing.com"
user ="waishing_trendy"
passwd="Socool666"

# Replace with your Binance API key


# Connect to PostgreSQL database
mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

db = mydb.cursor()

def get_current_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {'symbol': symbol}
    response = requests.get(url, params=params)
    data = response.json()
    return float(data['price'])

def get_24hr_high(symbol):
    url = "https://api.binance.com/api/v3/ticker/24hr"
    params = {'symbol': symbol}
    response = requests.get(url, params=params)
    data = response.json()
    return float(data['highPrice'])

def get_rsi():
    return 71
    # Implement your RSI calculation logic here
    # This may involve retrieving historical data and performing calculations

def get_macd_cross():
    return True
    # Implement your MACD cross logic here
    # This may involve retrieving historical data and performing calculations

def check_conditions(symbol):
    price = get_current_price(symbol)
    high_price = get_24hr_high(symbol)
    rsi = get_rsi()
    macd_cross = get_macd_cross()

    print(symbol,price,high_price,rsi,macd_cross)
    timestamp = int(time.time())

    db.execute("INSERT INTO CRYPTO_PRICE (PRICE, CREATED_DATE) VALUES (%s, %s)", (high_price, timestamp))
    mydb.commit()
    if rsi > 70 and macd_cross and price == high_price:
        prev_price = price
          # Sleep for 1 minute
        price = get_current_price()

        if price > prev_price * 1.01:
            print("Conditions met: RSI > 70, MACD crossed, current price is 24hr highest, and BTCUSDT increased 1% within one minute.")

            # Do something here, such as triggering an action or sending a notification

while True:

    symbols = ['ETHUSDT', 'BTCUSDT','SHIBUSDT']

    for symbol in symbols:
        check_conditions(symbol)


    time.sleep(5)
# ```
#
# Please note that the implementation of `get_rsi()` and `get_macd_cross()` functions would depend on your preferred method of calculating the RSI and MACD cross. You would need to replace the placeholder comments with your own logic to calculate those indicators.
#
# Also, make sure to install the `requests` library if you haven't already by running `pip install requests` in your terminal.