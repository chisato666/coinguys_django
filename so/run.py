import backtrader as bt
from FearGreedStrategy import FearGreedStrategy

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

class SPYPutCallFearGreedVixData(bt.feeds.GenericCSVData):
    lines = ('value', 'buy_ranking', 'sell_ranking')

    params = (
        ('dtformat', '%d/%m/%Y %H:%M'),
        ('date', 0),
        ('value', 1),
        ('value_classification', 2),
        ('time_until_update', 3),
        ('Close', 4),
        ('change', 5),
        ('RSI', 6),
        ('SMA200', 7),
        ('SMA50', 8),
        ('SMA5', 9),
        ('position', 10),
        ('fear', 11),
        ('greed', 12),
        ('overbrough', 13),
        ('oversell', 14),
        ('10d_low', 15),
        ('buy_ranking', 16),
        ('sell_ranking', 17)
    )




class FearGreedData(bt.feeds.GenericCSVData):

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('fear_greed', 4),
        ('volume', -1),
        ('openinterest', -1)
    )



spy_combined_csv_file = "fear.csv"
fear_greed_csv_file = "fear-greed.csv"


spyCombinedFeed = SPYPutCallFearGreedVixData(dataname=spy_combined_csv_file)

fearGreedFeed = FearGreedData(dataname=fear_greed_csv_file)

cerebro.adddata(spyCombinedFeed)
#cerebro.adddata(putCallFeed)
cerebro.adddata(fearGreedFeed)
#cerebro.adddata(vixFeed)

cerebro.addstrategy(FearGreedStrategy)
#cerebro.addstrategy(PutCallStrategy)
#cerebro.addstrategy(VIXStrategy)
print('Starting : %.2f' % cerebro.broker.getvalue())

cerebro.run()
print('Ending : %.2f' % cerebro.broker.getvalue())

#cerebro.plot(volume=False)
