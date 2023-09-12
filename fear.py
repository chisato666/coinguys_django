import requests
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import csv
import talib
import function




r= requests.get('https://api.alternative.me/fng/?limit=0')


df= pd.DataFrame(r.json()['data'])
df.value = df.value.astype(int)

df.timestamp= pd.to_datetime(df.timestamp, unit='s')

df.set_index('timestamp',inplace=True)
df= df[::-1]

#df1=yf.download('BTC-USD')[['Close']]
#df1 = yf.Ticker('BTC-USD').history(period='1mo',interval='1d')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]
df1 = yf.Ticker('BTC-USD').history(interval='1h',start="2023-04-22", end="2023-04-29")[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]


df1.index.name = 'timestamp'

print(df)

tog = df.merge(df1, on='timestamp')


tog['change']= tog.Close.pct_change()
tog['RSI']= talib.RSI(tog['Close'])


tog['SMA200']=tog.Close.rolling(200).mean()
tog['SMA50'] =tog.Close.rolling(50).mean()

tog['SMA5'] =tog.Close.rolling(5).mean()

tog['position']=np.where(tog.value>50,1,0)
tog['fear']=np.where(tog.value<30,1,0)
tog['greed']=np.where(tog.value>70,1,0)

tog['overbrough']=np.where(tog.RSI>70,1,0)
tog['oversell']=np.where(tog.RSI<30,1,0)
tog['10d_low']=tog.Close.rolling(10).min()

strategy=tog.position * tog.change

tog['buy_ranking'] = tog['fear']+ tog['oversell']
tog['sell_ranking'] = tog['greed']+ tog['overbrough']

#tog['rank']=function.price_sma_rank(tog.Close,tog.Close.rolling(5).mean())

#plt.figure(figsize=(20,10))
fig, axs = plt.subplots(2)
fig.suptitle('F&G vs BTC')
axs[0].axhline(y = 80, color = 'r', linestyle = 'dashed')

axs[0].axhline(y = 20, color = 'r', linestyle = 'dashed')

axs[0].plot(df['value'])
axs[1].plot(tog['Close'])

#plt.plot(df['value'], label='F&G')
plt.plot(tog['Close'], label='BTC')

#plt.plot((strategy+1).cumprod(),label='F&G')
#plt.plot((tog.change +1).cumprod(),label='BTC')
plt.legend()
plt.show()
(strategy +1).cumprod().plot(figsize=(20,10))

print(tog)
csvfile=open('so/fear_1y.csv', 'w', newline='')
candlestick_writer= csv.writer(csvfile, delimiter=',')
tog.to_csv('so/fear_1y.csv')