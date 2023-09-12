from datetime import date, datetime, timedelta
import dateparser
import time
import hmac
import json
import config
from pybit import usdt_perpetual

# Apply for API keys and secrets at  https://testnet.bybit.com/
api_key="xxx"
api_secret="xxx"

# Initialize web socket connection instance
ws = usdt_perpetual.WebSocket(
    test=True,
    api_key=config.api_key,
    api_secret=config.api_secret,
)

# Initialize http connection instance
session = usdt_perpetual.HTTP(endpoint="https://api-testnet.bybit.com", api_key=api_key, api_secret=api_secret)

# Define a target price that you want to enter your position
target_price = 40000

# handle_position is a callback that will be triggered on every new websocket event (push frequency can be 1-60s)
def handle_position(message):
    data = message["data"][0]
    if data:
        # check for target_price for entering position, if confirm=True, the data is the final tick for the interval. Otherwise, it is a snapshot.
        if data['close'] >= target_price and data['confirm'] == True:
            print("Buy Order | {} | {}".format(data['close'], time.strftime("%m/%d/%y, %H:%M:%S", time.localtime())))
            tp = target_price + (target_price * 0.05)
            sl = target_price - (target_price * 0.05)
            # Buy at market price to enter Long position
            ret = session.place_active_order(
                symbol="BTCUSDT",
                side="Buy",
                order_type="Market",
                qty=0.001, # amount to buy
                time_in_force="GoodTillCancel",
                reduce_only=False,
                close_on_trigger=False,
                take_profit=tp,
                tp_trigger_by="LastPrice",
                stop_loss=sl,
                sl_trigger_by="LastPrice",
                position_idx=0,
            )
            print("Buy Order Id | {}".format(ret["result"]["order_id"], time.strftime("%m/%d/%y, %H:%M:%S", time.localtime())))

# start kline stream here and pass in callback, symbol and desired kline interval
print(ws.kline_stream(callback=handle_position, symbol="BTCUSDT", interval="5"))

