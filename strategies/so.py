import math
import backtrader as bt
import requests
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import csv
import talib
import function

# Calculate the number of percentage to buy base on the buy in price below average and how depth of the price
# And buy more depends on the depth of the price
# Calculate the average of the years

class so(bt.Strategy):
    params = (('fast',50),('slow',200),('order_percentage',0.1),('ticker','BTC'))
    global last_price, total,count,vol
    last_price=0
    total=0
    def __init__(self):
        self.fast_moving_average= bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='50 day moving average'
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='200 day moving average'
        )
        self.last_price=0
        self.total=0
        self.count=0
        self.vol=0
        self.crossover=bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)



    def rank(self,price,sma):
        ranking=0
        ratio=0
        if sma==0:
            sma=price
        if price>sma:
            ranking=6
            ratio=(price-sma)/sma
            if ratio<0.1:
                ranking=ranking+1
            elif ratio<0.2:
                ranking=ranking+2
            elif ratio<0.3:
                ranking=ranking+3
            elif ratio<0.4:
                ranking=ranking+4
            else:
                ranking=ranking+5

        else:
            ranking=4
            ratio = (sma-price) / sma
            if ratio<0.1:
                ranking=ranking-1
            elif ratio<0.2:
                ranking=ranking-2
            elif ratio<0.3:
                ranking=ranking-3
            elif ratio<0.4:
                ranking=ranking-4
            else:
                ranking=ranking-5

        return ranking, ratio

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        self.count=self.count + 1
        self.total=self.total+self.data.close
        self.vol= self.vol + self.data.volume
        sma= self.total / self.count

        ranking=self.rank(self.data.close,sma)

        if self.tog['buy_ranking']==2:
            self.log('BUY CREATE, %.2f' % self.data.close[0])

            # Keep track of the created order to avoid a 2nd order
            self.order = self.buy()

        # if not self.position:
        #
        #     # Not yet ... we MIGHT BUY if ...
        #     if ranking[0] < 2:
        #         # current close less than previous close
        #
        #
        #             # BUY, BUY, BUY!!! (with default parameters)
        #         self.log('BUY CREATE, %.2f' % self.data.close[0])
        #
        #         # Keep track of the created order to avoid a 2nd order
        #         self.order = self.buy()
        #
        # else:
        #
        #     # Already in the market ... we might sell
        #     if ranking[0] > 7:
        #         # SELL, SELL, SELL!!! (with all possible default parameters)
        #         self.log('SELL CREATE, %.2f' % self.data.close[0])
        #
        #         # Keep track of the created order to avoid a 2nd order
        #         self.order = self.sell()



        print("time {} count {} close  {} sma {} vol {} ranking {} ratio {}".format(self.datas[0].datetime.date(0),self.count, self.data.close[0], sma, self.vol, ranking[0], ranking[1]))


