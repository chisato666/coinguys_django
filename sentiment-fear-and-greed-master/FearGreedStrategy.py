import backtrader as bt
import datetime 

class FearGreedStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.fear_greed = self.datas[0].fear_greed
        self.close = self.datas[0].close

    def next(self):
        self.size = int(self.broker.getcash() / self.close[0])

        if self.fear_greed[0] < 15 and not self.position:
            self.buy(size=self.size)
            self.log('BUY CREATE, %.2f , %.2f , %.2f' % (self.close[0],self.size,self.broker.getcash() ))
        if self.fear_greed[0] > 94 and self.position.size > 0:
            self.sell(size=self.position.size)
            self.log('Sell CREATE, %.2f , %.2f , %.2f' % (self.close[0],self.size,self.broker.getcash() ))
