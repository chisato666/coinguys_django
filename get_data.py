import csv
import yfinance as yf

import config
from binance.client  import Client

client= Client(config.api_key, config.api_secret)

candles = yf.Ticker('BTC-USD').history(period='1mo',interval='1d')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]

#candles= client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY)
#candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, "6 Feb, 2018" ,"9 Feb, 2022")

df = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "BTC-USD",
        title=['open', 'close', 'low', 'high', 'volume'],
        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1mo",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1d",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )

print(df)

# print(len(candles))
#
# csvfile=open('new.csv','w',newline='')
# candlestick_writer= csv.writer(csvfile, delimiter=',')
candles.to_csv("new.csv")


# for candlestick in candles:
#      candlestick_writer.writerow(candles)

# print(len(candles))