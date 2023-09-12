import decimal
from datetime import datetime
import bybit
from pybit import usdt_perpetual
import time
import config
import pandas as pd
import csv
import numpy
from collections import deque
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

previous_eth=0
counter=0
level_list=deque([1500,'UP','level-0'])


def rotate(l, n):
    return l[n:] + l[:n]



def round_down(value,decimals):
    with decimal.localcontext() as ctx:
        d=decimal.Decimal(value)
        ctx.rounding=decimal.ROUND_DOWN
        return round(d, decimals)
rounding_precision={'CRVUSDT':3}
rounding_precision={'ETHUSDT':2}

def Long(session_auth,Symbol):
    bal_usdt = session_auth.get_wallet_balance(coin='USDT')['result']['USDT']['available_balance']
    # print(bal_usdt)
    # value=bal_usdt['USDT']['available_balance']
    # print(value)
    Symbol_price = session_auth.latest_information_for_symbol(symbol=Symbol)
    print(Symbol_price)
    amount = float(bal_usdt)
    #/ float(Symbol_price) * 2.5
    amount = float(round_down(amount,rounding_precision[Symbol]))
    session_auth.place_active_order(
        symbol=Symbol,
        side="Buy",
        order_type="Market",
        qty=amount,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    )
    print(f" [Long] | {Symbol} | {amount}")

def Close_long(session_auth,Symbol):
    pos = session_auth.my_position(
        symbol=Symbol
    )
    session_auth.place_active_order(
        symbol=Symbol,
        side="Sell",
        order_type="Market",
        qty=pos['result'][0]['size'],
        time_in_force="GoodTillCancel",
        reduce_only=True,
        close_on_trigger=False

    )
    print(f"[ LONG ] | {Symbol} | Closed")

def check_level(current,previous,check_range):
    if (current - previous  >= 0.5) or (current - previous  <= -0.5):
        level = "level-0.5"
    if (current - previous  >= 1) or (current - previous  <= -1):
        level = "level-1"
    if (current - previous  >= 2) or (current - previous  <= -2):
        level = "level-2"
    if (current - previous  >= 3) or (current - previous  <= -3):
        level = "level-3"
    if (current - previous  >= 4) or (current - previous  <= -4):
        level = "level-4"
    if (previous  == 0):
        level = "0"

    if (current > previous ):
        position = "UP"
    else:
        position = "DOWN"

    if (current == previous ):
        position = ""

def get_price(symbol):
    global previous_eth,counter,level_list

    info = client.Market.Market_symbolInfo().result()
    keys = info[0]['result']
    # print(keys)
    dt = datetime.now()

    for i in range(0, len(keys)):
        if (keys[i]['symbol'] == symbol):
            print(f" {dt}  | {keys[i]['last_price']}")
            eth = float(keys[i]['last_price'])
            level=0
            num= counter % 10
            print(f" num= {num} ")

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
            if (previous_eth==0):
                level="0"

            if (eth>previous_eth):
                position="UP"
            else:
                position="DOWN"

            if (eth == previous_eth):
                position=""

            level_list.append([eth,position,level])
            if counter>9:
                level_list.popleft()

            with open('csv/eth_data_13062023.csv', 'a+', newline='') as a:
                writer = csv.writer(a)
                line = [dt, str(keys[i]['last_price']),level,position]
                writer.writerow(line)

            timestamp = int(time.time())

            db.execute("INSERT INTO CRYPTO_PRICE (PRICE, CREATED_DATE) VALUES (%s, %s)", (eth, timestamp))
            mydb.commit()

            previous_eth=eth
    print(level_list)
    counter=counter+1
    return eth

def check_order(symbol,check_range,count_second,count_list):

    order=(session_auth.query_conditional_order(
        symbol=symbol
    ))
    #print(order)

    current_price=float(get_price(symbol))
    a=current_price + check_range
    b=current_price - check_range

    #print(f" len order | {len(order['result'])}")
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    qty=0.01
    add_price=4
    take_profit_1=5
    take_profit_2=10
    take_profit_3=20
    stop_loss=2

    mini_range = 1

    if len(order['result'])==0:
        set_order(qty, add_price, take_profit_1,stop_loss)
        #set_order(qty, add_price, take_profit_2,stop_loss)


    for i in range(0, len(order['result'])):
        trigger_price=order['result'][i]['trigger_price']
        time_in_force= order['result'][i]['time_in_force']

        #print(f" Time: {dt} | stop_id: {order['result'][i]['stop_order_id']} [Trigger_price] | {trigger_price} [Current_price] | {current_price}")

        counter=0

        # IF the current price in the checking range

        if (min(a, b) <= trigger_price <= max(a, b)) and (time_in_force=="GoodTillCancel"):
            stop_id=(order['result'][i]['stop_order_id'])
            print(f"Time: {dt} Stop_id: {stop_id} Match Found  [Trigger_price] | {trigger_price} [Current_price] | {current_price}")

            found=0

            for i in range(0, len(count_list)):
                if (count_list[i][0] == stop_id):
                    print("Found")
                    found=1
                    created_time=count_list[i][1]
                    dt = datetime.now()
                    ts = datetime.timestamp(dt)
                    diff = ts - created_time

                #Check the time range in 2 seconds

                    if (0 <= diff <= 2):
                        count_list[i][2] = count_list[i][2] + 1
                        count_list[i][1] = ts

                    else:
                        count_list[i][2] = 1
                        count_list[i][1] = ts


            if found==0:
                dt = datetime.now()
                ts = datetime.timestamp(dt)
                line=[stop_id,ts,1]
                count_list.append(line)
                print("That item does not exist in the counter")



            print(count_list)

            current_price = float(get_price(symbol))
            x = current_price + mini_range
            y = current_price - mini_range
            # If count list > 0 and found , and in the minimum range and counter > 3 , cancel the order
            if (len(count_list)>0) and (found!=0):
                current_counter = count_list[i][2]

                if (min(x, y) <= trigger_price <= max(x, y)) and (current_counter>=2):
                    with open('csv/bybit_data.csv', 'a+', newline='') as f:
                        writer = csv.writer(f)
                        line = [dt,stop_id, trigger_price, current_price,current_counter]
                        writer.writerow(line)

                    try:
                        cancel_all(symbol)

                        with open('csv/bybit_data.csv', 'a+', newline='') as f:
                            writer = csv.writer(f)
                            line = [dt, "CANCEL ORDER", trigger_price, current_price]
                            writer.writerow(line)
                        print("CANCEL " + str(dt))
                    except:
                        print("Cannot cancel")
                    # print(session_auth.cancel_conditional_order(
                    #     symbol=symbol
                    #     #stop_order_id=order['result'][i]['stop_order_id']
                    # ))
                    dt = datetime.now()
                    ts = datetime.timestamp(dt)

                    # place_order(side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):
                    symbol = "ETHUSDT"
                    current_price = get_price(symbol)
                    with open('csv/bybit_data.csv', 'a+', newline='') as f:
                        writer = csv.writer(f)
                        line = [dt, "SET ORDER", trigger_price, current_price]
                        writer.writerow(line)
                    set_order(qty, add_price, take_profit_1,stop_loss)
                    #set_order(qty, add_price, take_profit_2,stop_loss)
                    #set_order(qty, add_price, take_profit_3,stop_loss)

                    print("SET ORDER " + str(dt))




def cancel_all(symbol):
    order = (session_auth.query_conditional_order(
        symbol=symbol
    ))

    for i in range(0, len(order['result'])):
        trigger_price = order['result'][i]['trigger_price']
        stop_order_id = order['result'][i]['stop_order_id']
        base_price = order['result'][i]['base_price']
        order_status = order['result'][i]['order_status']
        side = order['result'][i]['side']
        take_profit = order['result'][i]['take_profit']
        stop_loss = order['result'][i]['stop_loss']
        time_in_force = order['result'][i]['time_in_force']

        print(
            f" stop_order_id {stop_order_id} trigger_price {trigger_price} side {side} stop_loss {stop_loss} take_profit {take_profit} order_status {order_status}")
        if time_in_force == 'GoodTillCancel':
            print(session_auth.cancel_conditional_order(
                symbol=symbol,
                stop_order_id=stop_order_id
            ))

    print(order)

def replace_order(price,take_profit):
    print(session_auth.replace_conditional_order(
        symbol="ETHUSDT",
        order_link_id=ts,
        p_r_price=price + 2,
        take_profit=take_profit + 5,
        p_r_qty=10
    ))

def replace_ative_order(symbol,order_id,stop_loss,take_profit):
    print(session_auth.replace_active_order(
        symbol=symbol,
        order_id=order_id,
        stop_loss=stop_loss,
        take_profit=take_profit
    ))

def place_order(symbol,side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):

    if (side == "Buy"):
        price = float(current_price) + add_price
        take_profit = price + take_profit_amount
        stop_loss = price - stop_loss_amount

    if (side == "Sell"):
        price = float(current_price) - add_price
        take_profit = price - take_profit_amount
        stop_loss = price + stop_loss_amount

    dt = datetime.now()
    with open('csv/bybit_order.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        line = [dt, side, qty, price,  take_profit, stop_loss]
        writer.writerow(line)

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


def set_order(qty,add_price,take_profit, stop_loss):
    dt = datetime.now()
    ts = datetime.timestamp(dt)

    # place_order(side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):
    symbol = "ETHUSDT"
    current_price = get_price(symbol)

    place_order(symbol, "Buy", qty, add_price, current_price, take_profit, stop_loss, ts)
    dt = datetime.now()
    ts = datetime.timestamp(dt)



    place_order(symbol, "Sell", qty, add_price, current_price, take_profit, stop_loss, ts)

    dt = datetime.now()
    ts = datetime.timestamp(dt)

    # place_order(side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):
    # symbol = "ETHUSDT"
    # current_price = get_price(symbol)
    #
    # place_order(symbol, "Buy", qty, 2, current_price, 20, 0.05, ts)
    # dt = datetime.now()
    # ts = datetime.timestamp(dt)
    #
    # place_order(symbol, "Sell", qty, 2, current_price, 20, 0.05, ts)
    #
    #

# Start

session_auth= usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",api_key=config.api_key, api_secret=config.api_secret
)

ws = usdt_perpetual.WebSocket(
    test=False,
    ping_interval=30,  # the default is 30
    ping_timeout=29,  # the default is 10
    domain="bybit"  # the default is "bybit"

)
def handle_message(msg):
    #print(msg)
    print(msg['data']['last_price'])

def handle_orderbook(message):
    print(message)
def handle_position(message):
    print(message)

def cancel_order():
    order = (session_auth.query_conditional_order(
        symbol=symbol
    ))

    # order=(session_auth.query_active_order(
    #     symbol=symbol
    # ))
    print(order)

    for i in range(0, len(order['result'])):
        trigger_price = order['result'][i]['trigger_price']
        stop_order_id = order['result'][i]['stop_order_id']
        base_price = order['result'][i]['base_price']
        order_status = order['result'][i]['order_status']
        side = order['result'][i]['side']
        take_profit = order['result'][i]['take_profit']
        stop_loss = order['result'][i]['stop_loss']

        print(f" stop_order_id {stop_order_id} trigger_price {trigger_price} side {side} stop_loss {stop_loss} take_profit {take_profit} order_status {order_status}")




# MAIN START!!!!


#ws.instrument_info_stream(handle_message, "ETHUSDT")

client=bybit.bybit(test=False,api_key=config.api_key, api_secret=config.api_secret)
print('loggedin')

#Long(session_auth,"ETHUSDT")
#print(client.Order.Order_new(side="Buy",symbol="BTCUSD",order_type="Limit",qty=1,price=16000,time_in_force="GoodTillCancel").result())

dt = datetime.now()
ts = datetime.timestamp(dt)

# place_order(side,qty,add_price,current_price,take_profit_amount,stop_loss_amount,ts):
symbol="ETHUSDT"
current_price = get_price(symbol)

qty = 0.01
add_price = 4
take_profit_1 = 5
take_profit_2 = 10
take_profit_3 = 15
stop_loss=2

set_order(qty, add_price, take_profit_1,stop_loss)
set_order(qty, add_price, take_profit_2,stop_loss)
set_order(qty, add_price, take_profit_3,stop_loss)

order = (session_auth.query_conditional_order(
    symbol=symbol
))

# order=(session_auth.query_active_order(
#     symbol=symbol
# ))
print(order)

for i in range(0, len(order['result'])):
    trigger_price = order['result'][i]['trigger_price']
    stop_order_id = order['result'][i]['stop_order_id']
    base_price = order['result'][i]['base_price']
    order_status=order['result'][i]['order_status']
    side = order['result'][i]['side']
    take_profit = order['result'][i]['take_profit']
    stop_loss = order['result'][i]['stop_loss']

# for i in range(0, len(order['result']['data'])):
#     trigger_price = order['result']['data'][i]['trigger_price']
#     stop_order_id = order['result']['data'][i]['stop_order_id']
#     base_price = order['result']['data'][i]['base_price']
#     order_status=order['result']['data'][i]['order_status']
#     side = order['result']['data'][i]['side']
#     take_profit = order['result']['data'][i]['take_profit']
#     stop_loss = order['result']['data'][i]['stop_loss']


    print(f" stop_order_id {stop_order_id} trigger_price {trigger_price} side {side} stop_loss {stop_loss} take_profit {take_profit} order_status {order_status}")





    # stop_order_id = active_order['result'][i]['stop_order_id']

#cancel_all(symbol)

count_list=[]

# with open('bybit_data.csv', 'a+', newline='') as f:
#     writer = csv.writer(f)
#     line = [dt,"START ", symbol]
#     writer.writerow(line)

while True:
    #def check_order(symbol, check_range, count_second, count_list):

    check_order("ETHUSDT",3,2,count_list)
    get_price(symbol)
    time.sleep(1)

