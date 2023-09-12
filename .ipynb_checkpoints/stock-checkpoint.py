import yfinance as yf
import pandas as pd
import numpy as np
import talib
from binance.client import Client
from binance import BinanceSocketManager
import config
import time
import datetime
import matplotlib.pyplot as plt
import math
import mysql.connector
import csv



mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)


mycursor = mydb.cursor()

client = Client(config.api_key,config.api_secret)
candles = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, "6 Jan, 2021" ,"9 May, 2022")
#dataframe= pd.DataFrame(candles)
#new_df=dataframe.iloc[:,0:3]
#re_df=pd.DataFrame(new_df,columns=['Time','Open','Low','Close'])
df= pd.DataFrame(candles,columns=['Time','Open','High','Low','Close','Volume','Close time','Quota',
                                        'Trade','buy_base','buy_quote','Ignore'])

# [
#   [
#     1499040000000,      // Open time
#     "0.01634790",       // Open
#     "0.80000000",       // High
#     "0.01575800",       // Low
#     "0.01577100",       // Close
#     "148976.11427815",  // Volume
#     1499644799999,      // Close time
#     "2434.19055334",    // Quote asset volume
#     308,                // Number of trades
#     "1756.87402397",    // Taker buy base asset volume
#     "28.46694368",      // Taker buy quote asset volume
#     "17928899.62484339" // Ignore
#   ]
# ]


#df = yf.download('NVDA',start='2021-01-01', end='2022-01-01')
#
timestamp=df.loc[4, "Time"]


df['TT']= [datetime.datetime.fromtimestamp(int(ts)/1000).date() for ts in df.Time]


#print(datetime.datetime.fromtimestamp(df.loc[4,'Time']/1000).strftime('%Y-%m-%d %H:%M:%S'))
#print([datetime.datetime.fromtimestamp(int(ts)/1000).date() for ts in df.TT])

df['SMA200']=df.Close.rolling(200).mean()
df['SMA50'] =df.Close.rolling(50).mean()

df['SMA5'] =df.Close.rolling(5).mean()
df['10d_low']=df.Close.rolling(10).min()
df['Buy']= np.where((df.Close.astype(float) > df.SMA200) & (df['10d_low'].diff() <0) & (0.98 * df.Close.astype(float) >= df.Low.shift(-1).astype(float)),1,0)
df['Sell']= np.where(df.Close.astype(float) >df.SMA5,1,0)
df['Buyprice']= 0.98 * df.Close.astype(float)
df['Sellprice']= df.Open.shift(-1)
df['RSI']= talib.RSI(df["Close"])
df['overbrough']=np.where(df.RSI>70,1,0)
df['oversell']=np.where(df.RSI<30,1,0)


df.to_csv('rsi.csv')
newdf = df.loc[(df.oversell == 1) | (df.overbrough == 1)]


#print(df)

df = df.reset_index()  # make sure indexes pair with number of rows

for index,row in df.iterrows():
    if row['oversell']==1:
        print("buy it now ",row[0],row[1],row[2])

# close_rsi = df[["Close","RSI"]]
# rslt_df = df[df['overbrough'] ==1]


#print(df.loc[0:100,['Close','RSI']])
x=df[(df.overbrough==1) | (df.oversell==1)]
#print(x.loc[:,['Close','RSI','TT']])

df['price']= [(float(ts)) for ts in df.Close]

#df['price']=round(df.Close)
#print(df.price)
#bars = plt.bar(df.TT, df.RSI, fc='crimson', ec='navy')

#df1 = pd.DataFrame(df.TT, columns=["Close", "RSI"])
# df.plot(x="TT", y=["RSI"], kind="bar")
# df.plot(x="TT", y=df.price, kind="bar")


dd=pd.DataFrame()

def buyBTC(symbol,price,qty):
    sql = 'INSERT INTO TX (SYMBOL,PRICE, QTY) VALUES ("' + symbol + '",' + str(price) + ',' + str(qty) + ")"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    df2= pd.DataFrame({
        "price": [price],
        "qty": [qty]
    })
    global dd
    if dd.empty:
        dd=df2
    else:
        dd=pd.concat([dd,df2])



# buyBTC('BTCUSDT',100,1)
# buyBTC('ETHUSDT',200,4.6)



fig, axs = plt.subplots(2)
fig.suptitle('BTCUSD vs RSI')
axs[0].axhline(y = 70, color = 'r', linestyle = 'dashed')

axs[0].axhline(y = 30, color = 'r', linestyle = 'dashed')

axs[0].plot(df.TT, df.RSI)
axs[1].plot(df.TT,df.price)
axs[1].plot(df.TT,df.SMA50, color='C2')
axs[1].plot(df.TT,df.SMA200, color='C3')


#plt.show()


# df.plot(x="X", y="B", kind="bar", ax=ax, color="C2")
# df.plot(x="X", y="C", kind="bar", ax=ax, color="C3")
# df.plot(x)

#print(df[df["overbrough"].isin([1]) | df["oversell"].isin([1])])

# frame= pd.DataFrame(df)
# print(rslt_df)