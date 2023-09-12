import backtrader as bt
import datetime 

class FearGreedStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.buy_ranking = self.datas[0].buy_ranking
        self.sell_ranking = self.datas[0].sell_ranking

        self.close = self.datas[0].close

    def next(self):
        self.size = int(self.broker.getcash() / self.close[0])

        print("time {} count {} close  ranking {} selling {}".format(self.datas[0].datetime.date(0), self.close[0],  self.buy_ranking[0], self.sell_ranking[0]))

        if int(self.buy_ranking[0]) == 2:
            print(self.close[0])

        if int(self.buy_ranking[0]) == 2:
            self.buy(size=self.size)
            self.log('BUY CREATE, %.2f , %.2f , %.2f' % (self.close[0],self.size,self.broker.getcash() ))
        if int(self.sell_ranking[0]) ==2:
            self.sell(size=self.position.size)
            self.log('Sell CREATE, %.2f , %.2f , %.2f' % (self.close[0],self.size,self.broker.getcash() ))
