

import requests
from datetime import datetime, timedelta
import time
from plyer import notification

def check_price_decrease(symbol):
    url = f"https://contract.mexc.com/api/v1/contract/kline/{symbol}"
    interval = "Min60"
    candle_limit = 2
    seen_candles = set()
    params = {
        "interval": interval,
        "limit": candle_limit
    }

    response = requests.get(url, params=params)
    data = response.json()

    previous_close = float(data['data']['close'][0])
    current_close = float(data['data']['close'][1])

    print(data,previous_close,current_close)


def get_highest_price(symbol):
    url = f'https://contract.mexc.com/api/v1/contract/kline/{symbol}?interval=Min60&limit=10'
    response = requests.get(url)
    data = response.json()
    highest_price = None
    for kline in data['data']['close']:
        print(str(kline))
        # timestamp = int(kline[0]) / 1000  # Convert milliseconds to seconds
        # kline_datetime = datetime.fromtimestamp(timestamp)
        # if kline_datetime >= datetime.now() - timedelta(hours=10):
        #     price = float(kline['close'])
        #     if highest_price is None or price > highest_price:
        #         highest_price = price_change_percentage
    return highest_price

# Example usage
# symbols = ['BTC_USDT', 'ETH_USDT']
# check_price_decrease("BTC_USDT")

dt = datetime.now()
dt = dt.strftime("%Y-%m-%d %H:%M:%S")
print(dt)
# for symbol in symbols:
#     highest_price = get_highest_price(symbol)
#     print(f"The highest price for symbol {symbol} in the past 10 hours is: ")
