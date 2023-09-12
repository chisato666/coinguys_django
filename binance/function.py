import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from binance.client import Client
client= Client()

# symbol='ETHUSDT'
# start_date='2023-07-10'
# end_date='2023-08-02'
# period='1h'


def plot_chart(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df.Close)
    plt.scatter(self.buy_arr.index, self.buy_arr.values, marker='^', c='g')
    plt.scatter(self.sell_arr.index, self.sell_arr.values, marker='v', c='r')


def getdata(symbol,start_date,end_date,period):

    if (period !=""):
        df = pd.DataFrame(client.get_historical_klines(symbol,period,start_date,end_date))
    else:
        df = pd.DataFrame(client.get_historical_klines(symbol,start_date,end_date))
    df = df.iloc[:,:6]
    df.columns = ['Time','Open','High','Low','Close','Volume']
    df.set_index('Time',inplace=True)
    df.index = pd.to_datetime(df.index,unit='ms')
    df= df.astype(float)

    df['ret']= df.Close.pct_change()
    #df.ret.plot(kind='hist', bins=100)
    df['price']=df.Open.shift(-1)
#   df['SMA200']=df.Close.rolling(200).mean()

    return df

def get_rules1(df):
    in_position=False
    profits=[]
    all_arr=[]
    buy_arr=[]
    sell_arr=[]
    signalBuy=[]
    #and row.Close>row.SMA200


    for index, row in df.iterrows():
        if not in_position:
            if row.ret > 0.01:
                buyprice=row.price
                bought_at = index
                tp= buyprice * 1.02
                sl= buyprice * 0.98
                in_position=True
        if in_position and index > bought_at:
            if row.High > tp:
                profit = (tp -buyprice)/buyprice
                profits.append(profit)
                line=[index,buyprice,row.High,profit]
                buy_arr.append(line)
                all_arr.append(line)

                signalBuy.append(buyprice)

                in_position = False
            if row.Low < sl:
                profit = (sl - buyprice)/buyprice
                line=[index,buyprice,row.Low,profit]
                all_arr.append(line)
                sell_arr.append(line)

                profits.append(profit)
                in_position=False

    # dd = pd.DataFrame(profit)
    #
    # monthly_profit = df.Close.resample('M').sum()
    #
    #print(pd.Series(monthly_profit))
    # print(pd.Series(buyprices))
    #print(profits)
    pro_count=((pd.Series(profits) > 0).value_counts())
    pro_list=((pd.Series(profits) + 1).cumprod())
   # total=((pd.Series(profits) + 1).cumprod())
    pro_total=(pd.Series(profits) +1).prod()

    #plt.show()
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 10)

    df['signal']=pd.Series([signalBuy])


    #plt.scatter(self.sell_arr.index, self.sell_arr.values, marker='v', c='r')
    return pro_total,pro_list,pro_count,all_arr,df
 #   return buy_arr,sell_arr,df


#data=getdata(symbol, start_date, end_date, period)
# data=getdata(symbol, "1h", "50 hour ago UTC","")
#
# print(data)
#buy_arr,sell_arr,df=get_rules1(data)
# print(buy_arr)
#
# print(sell_arr)
# print(data)
#print(df[['High','Close','ret']])