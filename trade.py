import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
import config
import math

client = Client(config.api_key, config.api_secret)

bsm = BinanceSocketManager(client)
socket= bsm.trade_socket('BTCUSDT')



def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:,['s','E','p']]
    df.columns =['symbol','Time','Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time,unit='ms')
    return df

createframe(msg)