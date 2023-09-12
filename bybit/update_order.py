import decimal
from datetime import datetime
import bybit
from pybit import usdt_perpetual
import time
import config
import pandas as pd
import csv

def get_price(symbol):
    info = client.Market.Market_symbolInfo().result()
    keys = info[0]['result']
    # print(keys)

    for i in range(0, len(keys)):
        if (keys[i]['symbol'] == symbol):
            #print(keys[i]['last_price'])
            eth = keys[i]['last_price']
    return eth

session_auth= usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",api_key=config.api_key, api_secret=config.api_secret
)

symbol="ETHUSDT"
client=bybit.bybit(test=False,api_key=config.api_key, api_secret=config.api_secret)

# order = (session_auth.query_conditional_order(
#     symbol=symbol
# ))
# print(order)

# order=(session_auth.query_active_order(
#     symbol=symbol
# ))
# print(order)
#
# print(session_auth.get_active_order(
#     symbol=symbol
# ))

while True:
    order = (session_auth.query_conditional_order(
        symbol=symbol
    ))
    #print(order)
    for i in range(0, len(order['result'])):
        trigger_price = float(order['result'][i]['trigger_price'])
        stop_order_id = order['result'][i]['stop_order_id']
        base_price = float(order['result'][i]['base_price'])
        order_status=order['result'][i]['order_status']
        side = order['result'][i]['side']
        take_profit = order['result'][i]['take_profit']
        stop_loss = order['result'][i]['stop_loss']
        reduce_only = order['result'][i]['reduce_only']
        time_in_force = order['result'][i]['time_in_force']

        # for i in range(0, len(order['result']['data'])):
    #     trigger_price = order['result']['data'][i]['trigger_price']
    #     stop_order_id = order['result']['data'][i]['stop_order_id']
    #     base_price = order['result']['data'][i]['base_price']
    #     order_status=order['result']['data'][i]['order_status']
    #     side = order['result']['data'][i]['side']
    #     take_profit = order['result']['data'][i]['take_profit']
    #     stop_loss = order['result']['data'][i]['stop_loss']

        current_price = float(get_price(symbol))
        distance=3
        #This is the Short and stop loss condition
        if ((trigger_price>current_price+distance) and (side=="Buy") and (current_price<base_price)) and (time_in_force!='GoodTillCancel'):
            print(session_auth.replace_conditional_order(
                symbol=symbol,
                stop_order_id=stop_order_id,
                p_r_trigger_price=current_price+distance
            ))
            with open('csv/bybit_update_order.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                line = [f"update Buy success ID {stop_order_id}  Trigger Price {trigger_price} to New Price {current_price+distance}" ]
                writer.writerow(line)
            print(f"update Buy success ID {stop_order_id}  Trigger Price {trigger_price} to New Price {current_price+distance}" )

        if ((trigger_price<current_price-distance) and (side=="Sell") and (current_price>base_price)) and (time_in_force!='GoodTillCancel'):
            print(session_auth.replace_conditional_order(
                symbol=symbol,
                stop_order_id=stop_order_id,
                p_r_trigger_price=current_price-distance
            ))
            print("update Sell success" +stop_order_id)
            with open('csv/bybit_update_order.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                line = [f"update Sell success ID {stop_order_id}  Trigger Price {trigger_price} to New Price {current_price+distance}" ]
                writer.writerow(line)
            print(f"update Buy success ID {stop_order_id}  Trigger Price {trigger_price} to New Price {current_price+distance}" )


    #print(f" stop_order_id {stop_order_id} trigger_price {trigger_price} side {side} stop_loss {stop_loss} take_profit {take_profit} order_status {order_status}")



