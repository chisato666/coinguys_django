from pybit import usdt_perpetual
import config

session_auth= usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",api_key=config.api_key, api_secret=config.api_secret
)
# print(session_auth.cancel_all_conditional_orders(
#     symbol="ETHUSDT"
# ))

symbol="ETHUSDT"


order=(session_auth.query_conditional_order(
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
    time_in_force= order['result'][i]['time_in_force']

    print(
        f" stop_order_id {stop_order_id} trigger_price {trigger_price} side {side} stop_loss {stop_loss} take_profit {take_profit} order_status {order_status}")
    if time_in_force=='GoodTillCancel':
        print(session_auth.cancel_conditional_order(
            symbol=symbol,
            stop_order_id=stop_order_id
        ))


print(order)