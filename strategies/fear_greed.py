import math
import backtrader as bt
import requests
import pandas as pd
import numpy as np


# Caluclate the number of percentage to buy base on the buy in price below average and how depth of the price
# And buy more depends on the depth of the price
# Caluclate the average of the years

class fear_greed(bt.Strategy):
    params = (('fast',50),('slow',200),('order_percentage',0.1),('ticker','BTC'))
    global last_price
    last_price=0

    def __init__(self):
        r = requests.get('https://api.alternative.me/fng/?limit=0')

        self.df = pd.DataFrame(r.json()['data'])
        self.df.value = df.value.astype(int)

        self.df.timestamp = pd.to_datetime(df.timestamp, unit='s')

        self.df.set_index('timestamp', inplace=True)

    def next(self):
        if self.position.size == 0:
            if self.crossover >0:
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.buy(size=self.size)
                self.last_price=self.data.close[0]

        if self.position.size>0:
            print("last {} now {}".format(self.last_price,self.data.close[0]))
            if self.crossover <0 and self.last_price<self.data.close[0]:
                print("Sell {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.close()