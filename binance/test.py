import config, function
import pandas as pd
import talib
import ta, os
from binance.client import Client
client= Client()



def getdata(symbol):

    df = pd.DataFrame(client.get_historical_klines(symbol, "1h", "2 day ago UTC"))
    df = df.iloc[:,:6]
    df.columns = ['Time','Open','High','Low','Close','Volume']
    df.set_index('Time',inplace=True)
    df.index = pd.to_datetime(df.index,unit='ms')
    df= df.astype(float)

    df['ret']= df.Close.pct_change()
    #df.ret.plot(kind='hist', bins=100)
    df['price']=df.Open.shift(-1)

    return df

def calc_indicators(df):

    df['ma_20'] =  df.Close.rolling(20).mean()
    df['vol'] =  df.Close.rolling(20).std()
    df['upper_bb'] =  df.ma_20 + (2 *  df.vol)
    df['lower_bb'] =  df.ma_20 - (2 *  df.vol)
    df['ret'] =  df.Close.pct_change()
    df['sl'] =  df.Close * 0.98
    df['tp'] =  df.Close * 1.02

    df['price'] =  df.Open.shift(-1)



    df['rsi'] = ta.momentum.RSIIndicator( df.Close, window=14).rsi()


    df['bb_upper'] = ta.volatility.BollingerBands(close=df.Close, window=20, window_dev=2).bollinger_hband()


    df.dropna(inplace=True)

    print(df['rsi'])
    print(df['bb_upper'])
    return df

def generate_signals():
    conditions = [(self.df.rsi < 30) & (self.df.Close < self.df.lower_bb),
                    (self.df.rsi > 70) & (self.df.Close > self.df.upper_bb)]

    conditions2 = [(self.df.ret > 0.01),
                    (self.df.High > self.df.tp) | (self.df.Low < self.df.sl)]



#print(os.path.abspath(ta.__file__))

df=getdata('BTCUSDT')
#calc_indicators(df)
print(calc_indicators(df))
