from flask import Flask, render_template
import decimal
from datetime import datetime
import bybit
from pybit import usdt_perpetual
import time
import config
import pandas as pd
import csv
client=bybit.bybit(test=False,api_key=config.api_key, api_secret=config.api_secret)
previous_eth=0
session_auth= usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",api_key=config.api_key, api_secret=config.api_secret
)

def round_down(value,decimals):
    with decimal.localcontext() as ctx:
        d=decimal.Decimal(value)
        ctx.rounding=decimal.ROUND_DOWN
        return round(d, decimals)
rounding_precision={'CRVUSDT':3}
rounding_precision={'ETHUSDT':2}

def place_order(symbol,side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):

    if (side == "Buy"):
        price = float(current_price) + add_price
        take_profit = price + take_profit_amount
        stop_loss = price - stop_loss_amount

    if (side == "Sell"):
        price = float(current_price) - add_price
        take_profit = price - take_profit_amount
        stop_loss = price + stop_loss_amount

    print(session_auth.place_conditional_order(
        symbol=symbol,
        order_type="Limit",
        side=side,
        qty=qty,
        price=price,
        stop_px=price,
        base_price=current_price,
        take_profit=float(round(take_profit,rounding_precision[symbol])),
        stop_loss=float(round(stop_loss,rounding_precision[symbol])),
        time_in_force="GoodTillCancel",
        trigger_by="LastPrice",
        order_link_id=ts,
        reduce_only=False,
        close_on_trigger=False
    ))


def set_order(qty,add_price,take_profit):
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    # place_order(side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):
    symbol = "ETHUSDT"
    current_price = get_price(symbol)

    place_order(symbol, "Buy", qty, add_price, current_price, take_profit, 0.05, ts)
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    place_order(symbol, "Sell", qty, add_price, current_price, take_profit, 0.05, ts)

    dt = datetime.now()
    ts = datetime.timestamp(dt)

def get_price(symbol):
    global previous_eth

    info = client.Market.Market_symbolInfo().result()
    keys = info[0]['result']
    # print(keys)
    dt = datetime.now()

    for i in range(0, len(keys)):
        if (keys[i]['symbol'] == symbol):
            print(f" {dt}  | {keys[i]['last_price']}")
            eth = float(keys[i]['last_price'])
            level=0
            if (eth - previous_eth >= 0.5) or (eth - previous_eth  <= -0.5):
                level="level-0.5"
            if (eth - previous_eth >= 1) or (eth - previous_eth  <= -1):
                level="level-1"
            if (eth - previous_eth >= 2) or (eth - previous_eth  <= -2):
                level="level-2"
            if (eth - previous_eth >= 3) or (eth - previous_eth  <= -3):
                level="level-3"
            if (eth - previous_eth >= 4) or (eth - previous_eth  <= -4):
                level="level-4"

            with open('log_data.csv', 'a+', newline='') as a:
                writer = csv.writer(a)
                line = [dt, str(keys[i]['last_price']),level]
                writer.writerow(line)
            previous_eth=eth
    return eth
app = Flask(__name__)

@app.route("/create_order")
def create_order():
    symbol = "ETHUSDT"
    qty = 0.01
    add_price = 2
    take_profit_1 = 5
    take_profit_2 = 10
    take_profit_3 = 25

    set_order(qty, add_price, take_profit_1)
    return "<p>Order Created</p>"

@app.route("/get_price")
def get_eth_price():
    title="Eth Price"
    eth_price=get_price("ETHUSDT")
    return render_template('index.html',title=title,eth_price=eth_price)