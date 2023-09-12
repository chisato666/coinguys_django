import backtrader as bt
import datetime
from strategies.so import so
from strategies.GoldenCross import GoldenCross

import yfinance as yf

df = yf.Ticker('BTC-USD').history(period='4y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]

cerebro = bt.Cerebro()
cerebro.broker.set_cash(10000000)

data = bt.feeds.YahooFinanceCSVData(
    dataname='btcusdt4y.csv',
    datetime=0,
    # Do not pass values before this date
   # fromdate=datetime.datetime(2019, 1, 1),
    # Do not pass values after this date
  #  todate=datetime.datetime(2022, 1, 31),
    timeframe=bt.TimeFrame.Days,
    dtformat=('%d-%m-%Y %H:%M'),
    open=1,
    high=2,
    low=3,
    close=4,
    volume=5,
    reverse=False)

cerebro.adddata(data)
cerebro.addstrategy(so)
print('Starting : %.2f' % cerebro.broker.getvalue())
cerebro.run()
cerebro.plot()

print('Ending : %.2f' % cerebro.broker.getvalue())
