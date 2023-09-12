import math
import backtrader as bt


# Caluclate the number of percentage to buy base on the buy in price below average and how depth of the price
# And buy more depends on the depth of the price
# Caluclate the average of the years

class GoldenCross(bt.Strategy):
    params = (('fast',50),('slow',200),('order_percentage',0.9),('ticker','BTC'))
    global last_price
    last_price=0

    def __init__(self):
        self.fast_moving_average= bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='50 day moving average'
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='200 day moving average'
        )
        self.last_price=0
        self.crossover=bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

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