#Sure, here's an example Python script that uses the Bybit API to place a conditional order based on the price movement of BTC over the last hour:

import decimal
import os
import json, requests
import pandas as pd
from time import sleep
import datetime as dt
import time
from datetime import datetime, timedelta
import bybit
import config
from pybit import usdt_perpetual

# Initialize Bybit API client
client=bybit.bybit(test=False,api_key=config.api_key, api_secret=config.api_secret)
session_auth= usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",api_key=config.api_key, api_secret=config.api_secret
)
# Define order parameters
symbol = 'BTCUSDT'
order_type = 'Limit'
qty = 0.001
price = None  # Will be set based on price movement
time_in_force = 'GoodTillCancel'
reduce_only = False
close_on_trigger = False
order_link_id = None

# Define price movement parameters
interval = 3600  # 1 hour in seconds
target_increase = 0.01  # 1%
tp = 0.02  # 2%
sl = -0.02  # -2%

def round_down(value,decimals):
    with decimal.localcontext() as ctx:
        d=decimal.Decimal(value)
        ctx.rounding=decimal.ROUND_DOWN
        return round(d, decimals)
rounding_precision={'CRVUSDT':3}
rounding_precision={'ETHUSDT':2}
rounding_precision={'BTCUSDT':2}


def get_price(symbol):
    url = "https://api.bybit.com/v2/public/tickers?symbol=" + symbol
    price=0
    # make GET request to the API endpoint
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        # retrieve the current price from the response JSON
        price = response.json()['result'][0]['last_price']
        print(f"The current BTCUSDT price on Bybit is {price}")
    else:
        print(f"Error: {response.status_code} - {response.reason}")

    return price
# Define function to calculate target price
def calculate_target_price(current_price, target_increase):
    return current_price * (1 + target_increase)

# Define function to place conditional order
def place_conditional_order(side, target_price, tp, sl):
    global price
    price= float(get_price(symbol))+1
    if side == 'Buy':
        take_profit = price * (1 + tp)
        stop_loss = price * (1 + sl)
    elif side == 'Sell':
        #price = target_price
        take_profit = price * (1 - tp)
        stop_loss = price * (1 - sl)
    else:
        raise ValueError(f"Invalid side '{side}'. Must be 'Buy' or 'Sell'.")

    print(float(round(price, rounding_precision[symbol])),float(round(take_profit, rounding_precision[symbol])),float(round(stop_loss, rounding_precision[symbol])))
    print(session_auth.place_conditional_order(
        symbol=symbol,
        order_type="Limit",
        side=side,
        qty=qty,
        price=float(round(price, rounding_precision[symbol])),
        stop_px=float(round(price, rounding_precision[symbol])),
        base_price=get_price(symbol),
        take_profit=float(round(take_profit, rounding_precision[symbol])),
        stop_loss=float(round(stop_loss, rounding_precision[symbol])),
        time_in_force="GoodTillCancel",
        trigger_by="LastPrice",
        order_link_id=order_link_id,
        reduce_only=False,
        close_on_trigger=False
    ))


    # response = session_auth.place_conditional_order(
    #     symbol=symbol,
    #     side=side,
    #     order_type=order_type,
    #     qty=qty,
    #     price=float(round(price, rounding_precision[symbol])),
    #     base_price=float(round(price, rounding_precision[symbol])),
    #     stop_px=stop_loss,
    #    # tp_price=take_profit,
    #     take_profit=float(round(take_profit, rounding_precision[symbol])),
    #     stop_loss=float(round(stop_loss, rounding_precision[symbol])),
    #
    #     time_in_force=time_in_force,
    #     reduce_only=reduce_only,
    #     close_on_trigger=close_on_trigger,
    #     order_link_id=order_link_id
    # )
    # print(f"Placed {side} order: {response}")


def get_bybit_bars(symbol, interval, startTime, endTime):
    url = "https://api.bybit.com/v2/public/kline/list"

    # startTime = str(int(startTime.timestamp()))
    # endTime = str(int(endTime.timestamp()))

    req_params = {"symbol": symbol, 'interval': interval, 'from': startTime, 'to': endTime}

    df = pd.DataFrame(json.loads(requests.get(url, params=req_params).text)['result'])

    if (len(df.index) == 0):
        return None

    df.index = [dt.datetime.fromtimestamp(x) for x in df.open_time]

    return df


def get_hr_price(symbol,pos):
    endpoint = 'https://api.bybit.com/v2/public/kline/list'
    interval = '1'  # 1-minute interval
    start_time = int(time.time()) - 3600  # start time is one hour ago
    end_time = int(time.time())
    print(end_time)
    # make the API call and retrieve the data
    params = {'symbol': symbol, 'interval': interval, 'from': start_time, 'to': end_time}
    response = requests.get(endpoint, params=params)
    price=0
    if response.status_code != 200:
        print(f'Error: {response.status_code} {response.reason}')
        price=0
    else:
        data = df = pd.DataFrame(response.json()['result'])
        if pos==0:
            price=data.head(1)['close']
        elif pos==1:
            price = data.tail(1)['close']

    return price.values
# Main loop
#while True:
    # Calculate start and end times for price data
first_price = float(get_hr_price("BTCUSD",0))

current_price=float(get_hr_price("BTCUSD",1))+500

print(first_price)
print(current_price)
print(target_increase)

# Calculate percentage change in price over the last hour
price_change = (current_price - first_price) / current_price
print(f"Price change over the last hour: {price_change:.2%}")

    # Determine whether to place a buy or sell order based on price change
if price_change >= target_increase:
    # If price increased by target amount, place buy order
    target_price = calculate_target_price(current_price, target_increase)
    place_conditional_order('Buy', current_price, tp, sl)
else:
    # Otherwise, do not place an order
    print("Price change did not meet target increase. No order placed.")

# Wait for next interval
next_interval = datetime.utcnow() + timedelta(seconds=interval)
print(f"Waiting until {next_interval}...")
    # sleep((next_interval - datetime.utcnow()).total_seconds())

#This script sets up an infinite loop that repeatedly gets the BTC price data from the Bybit API for the last hour, calculates the percentage change in price over that time period, and places a conditional order to buy BTC if the price increased by at least 1% during the last hour. The order has a take profit target of 2% and a stop loss of -2%.

#Note that this script assumes that you have set the `BYBIT_API_KEY` and `BYBIT_API_SECRET` environment variables to your Bybit API credentials. You can obtain these credentials by creating an API key in your Bybit account settings. Also note that this is just an example script and does not include error handling or other best practices that you would want to include in a production system.