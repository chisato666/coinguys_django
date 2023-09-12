from binance.client import Client
from binance import BinanceSocketManager
import config
import math

from decimal import Decimal as D, ROUND_DOWN, ROUND_UP
import decimal


client = Client(config.api_key, config.api_secret)

bsm = BinanceSocketManager(client)
socket= bsm.trade_socket('ONEUSDT')

await socket.__aenter__()
msg = await socket.recv()



pair="ONEUSDT"
quantity=50


info = client.get_symbol_info(symbol=pair)
price_filter = float(info['filters'][0]['tickSize'])
ticker = client.get_symbol_ticker(symbol=pair)
price = float(ticker['price'])
price = D.from_float(price).quantize(D(str(price_filter)))
minimum = float(info['filters'][2]['minQty']) # 'minQty'
quant = D.from_float(quantity).quantize(D(str(minimum))) # if quantity >= 10.3/price

info = client.get_account()

bal= info['balances']

info = client.get_symbol_info('ONEBTC')
#print(info)

print(info['filters'][2]['minQty'])




#qty = round_down(client,'ONE',12)
#print('QTY' . str(qty))
# from binance.enums import *
# order = client.create_order(
#     symbol='ONEUSDT',
#     side=SIDE_SELL,
#     type=ORDER_TYPE_LIMIT,
#     timeInForce=TIME_IN_FORCE_GTC,
#     quantity=quant,
#     price='0.3'
# )


orders = client.get_open_orders(symbol='ONEUSDT')
print(orders)

#for kline in client.get_historical_klines_generator("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"):
#    print(kline)

# for b in bal:
#     if float(b['free']) >0:
#         print(b)