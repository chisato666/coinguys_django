import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from binance.client import Client
client= Client()

symbol='BTCUSDT'
start_date='2022-01-01'
end_date='2023-01-01'
period='1h'

def getdata(symbol,start,end,period):
    frame = pd.DataFrame(client.get_historical_klines(symbol,period,start,end))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time','Open','High','Low','Close','Volume']
    frame.set_index('Time',inplace=True)
    frame.index = pd.to_datetime(frame.index,unit='ms')
    frame= frame.astype(float)
    return frame



df = getdata(symbol,start_date,end_date,period)

df['ret']= df.Close.pct_change()
df.ret.plot(kind='hist', bins=100)
df['price']=df.Open.shift(-1)
df['SMA200']=df.Close.rolling(200).mean()

in_position=False
profits=[]
buyprices=[]
#and row.Close>row.SMA200


for index, row in df.iterrows():
    if not in_position:
        if row.ret > 0.01 :
            buyprice=row.price
            bought_at = index
            tp= buyprice * 1.02
            sl= buyprice * 0.98
            in_position=True
    if in_position and index > bought_at:
        if row.High > tp:
            profit = (tp -buyprice)/buyprice
            profits.append(profit)
            line=[index,buyprice,row.High]
            buyprices.append(line)
            in_position = False
        if row.Low < sl:
            profit = (sl - buyprice)/buyprice
            profits.append(profit)
            in_position=False

# dd = pd.DataFrame(profit)
#
# monthly_profit = df.Close.resample('M').sum()
#
#print(pd.Series(monthly_profit))
# print(pd.Series(buyprices))
#
print((pd.Series(profits) > 0).value_counts())
print((pd.Series(profits) + 1).prod())
print((pd.Series(profits) + 1).cumprod())

 #plt.show()
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)

#print(df[['High','Close','ret']])