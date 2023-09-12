import requests, datetime, time
from decimal import Decimal
import pandas as pd
import numpy as np
import json_normalize


response= requests.get("https://api.mexc.com/api/v3/exchangeInfo")
result = response.json()['symbols']

#kline
response= requests.get("https://api.mexc.com/api/v3/klines?symbol=POGAIUSDT&interval=5m")
result = response.json()


response= requests.get("https://contract.mexc.com/api/v1/contract/detail")
result = response.json()['data']
frame = pd.DataFrame(result)
print(frame)


response= requests.get("https://contract.mexc.com/api/v1/private/position/open_positions")
result = response.json()
print(result)


def getdata(symbol,interval,start,end):
    #interval 间隔: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1，不填时默认Min1
    link="https://contract.mexc.com/api/v1/contract/kline/"+ symbol + "?interval="+ interval +"&start="+ str(start)+ "&end="+ str(end)
    print(link)
    response= requests.get(link)

    frame = response.json()['data']
    frame = pd.DataFrame(frame)
    frame = frame.iloc[:,:6]
    frame.columns = ['time','Open','Close','high','low','Volume']
    frame.set_index('time',inplace=True)
    frame.index = pd.to_datetime(frame.index,unit='s')
    #frame['date']=
    frame= frame.astype(float)
    return frame
#MA under
def ma_calc(df,n):
    df['sma'+str(n)]= df.Close.rolling(n).mean()

def backtest(df,n):
    ma_calc(df,n)
    ma_calc(df,100)

    in_position= False
    profits=[]
    dates=[]
    buyarr=[]
    sellarr=[]
    stop_loss_level=0.005
    gain_level=0.01

    for index,row in df.iterrows():
        if in_position:
              # 止蝕位步長

             #print(" index {} Open {} Close {} Stop loss {} ".format(index,row.Open, row.Close,stop_loss))

             if row.Close > stop_loss + (row.Close * stop_loss_level):
                #stop_loss += stop_loss_step
                stop_loss = row.Close - (row.Close * stop_loss_level)

                #print("index {} Open {} Close {}  Stop_loss {}  True".format(index,row.Open,row.Close, stop_loss))

            # If current price < stop loss , Close the contract
              # 如果現價小於等於止蝕位，則平倉

             if row.Close <= stop_loss:
                profit= (row.Close - buyprice)/buyprice
                #print("index {} Buy {} Open {} Close {}  Profit {}  Stop loss {} Gain ".format(index,buyprice,row.Open, row.Close, profit,stop_loss))
                #print((pd.Series(profits) + 1).prod())

                dates.append(index)
                sellarr.append(row.Close)
                profits.append(profit)

                in_position = False

        if not in_position:
            stop_loss = 0  # 止蝕位


            #if (row.Close > row['sma'+str(n)]) and (row.Close > row['sma100']):
            if (row.Close > row['sma' + str(n)]):
                buyprice = row.price
                stop_loss = (row.price * (1 - gain_level))
                current_index=index
                #print("Index {} Close {} Buy Price {}  SMA {} stop_loss {}  Gain ".format(index,row.Close,buyprice, row.sma,stop_loss))
                buyarr.append(row.price)

                in_position = True


    gain=(pd.Series(profits) +1).prod()
    campaign = pd.DataFrame(dict(date=dates, price=profits))

    return gain,campaign,buyarr,sellarr

start_date = '2019-03-01'
end_date = '2023-05-31'

# convert the start and end dates to Unix timestamp format
start_timestamp = int(time.mktime(time.strptime(start_date, '%Y-%m-%d')))
end_timestamp = int(time.mktime(time.strptime(end_date, '%Y-%m-%d')))

df=(getdata('BTC_USDT','Day1',start_timestamp,end_timestamp))
df['price']= df.Open.shift(-1)
ma_calc(df,10)

(g,p,buyarr,sellarr)=(backtest(df, 30))

campaign  = pd.DataFrame (dict (date = df.index, price=df['price']))


x=(p
.groupby(p['date'].dt.strftime('%y'))
.agg (sum_price = ('price' , 'sum')))

# print(x)
# print(g)
#
# print(p)
# print(df)
#
# print(buyarr)
# print(sellarr)

# for n in np.arange(10,205,5):
#     print('parameter: ' + str(n))
#     print(backtest(df,n))
# response= requests.get("https://contract.mexc.com/api/v1/contract/kline/BTC_USDT?interval=Min15&start=1609992674&end=1610113500")
# result = response.json()['data']
# print(pd.DataFrame(result))
# for i in result:
#     print(i['symbol'])