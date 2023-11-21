import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time,pytz
from datetime import datetime
import talib as ta

from binance.client import Client
client= Client()

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


def check_symbols_with_increased_5d(percent, interval, limit):
    url = "https://contract.mexc.com/api/v1/contract/ticker"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        symbols = []

        x = 1
        for ticker in data['data']:
            x = x + 1
            # if (x > 30):
            #     break
            symbol = ticker['symbol']
            try:
                print(symbol,interval,limit,percent)

                df = check_symbols_kline(symbol, interval, limit)
                print(df)
                size = len(df)
                print('size',size)

                start_price = df['open'][0]
                end_price = df['close'][size - 1]


                price_change = (end_price - start_price) / start_price * 100
                print(start_price,end_price,price_change)

                # line = [symbol, round(price_change_percentage*100,2)]
                if float(price_change) > float(percent):
                    price_change=round(float(price_change),2)
                    line = [symbol, price_change]

                    symbols.append(line)
                    print('symbol added',symbol)
            except Exception as error:
                print(symbol, error)

        symbols.sort(key=lambda element: element[1], reverse=True)

        return symbols
    else:
        print("Failed to retrieve data from MEXC API.")
        return None

def get_contract_info(symbol):
    url = "https://contract.mexc.com/api/v1/contract/ticker/"
    params = {'symbol': symbol}
    response = requests.get(url, params=params)
    data = response.json()
    return data['data']


def check_symbols_kline(symbol, interval, limit):
    url = f'https://contract.mexc.com/api/v1/contract/kline/{symbol}?interval={interval}&limit={limit}'

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data['data'], columns=['time', 'open', 'low', 'high', 'close'])

    df.index = pd.to_datetime(df.time, unit='s', utc=True).map(lambda x: x.tz_convert('Asia/Hong_Kong'))

    # df.index = pd.to_datetime(df.index, unit='s')

    # df.set_index('time', inplace=True)

    return df


# def check_symbols_kline(symbol, interval, limit):
#     url = f'https://contract.mexc.com/api/v1/contract/kline/{symbol}?interval={interval}&limit={limit}'
#     # time_step = 'Day1' # 合约的参数：间隔: Min1、Min5、Min15、Min30、Min60、Hour4、Hour8、Day1、Week1、Month1，不填时默认Min1
#
#     response = requests.get(url)
#     data = response.json()
#
#     df = pd.DataFrame(data['data'], columns=['time', 'open', 'low', 'high', 'close'])
#
#     df.index = pd.to_datetime(df.time, unit='s', utc=True).map(lambda x: x.tz_convert('Asia/Hong_Kong'))
#
#     # df.index = pd.to_datetime(df.index, unit='s')
#
#     # df.set_index('time', inplace=True)
#
#     return df




def check_symbols_with_hr_24high(symbol,high24,low24):
    isHigh=False
    isLow=False

    url = f'https://contract.mexc.com/api/v1/contract/kline/{symbol}?interval=Min60&limit=5'
    response = requests.get(url)
    data = response.json()
    highest_price = None

    try:
        for kline in data['data']['high']:
            if (kline>=high24):
                print(symbol,kline,high24)
                isHigh=True
                break
        for kline in data['data']['low']:
            if (kline<=low24):
                print(symbol,kline,low24)
                isLow=True
                break
    except:
        print(symbol, " 24 error")

    return isHigh, isLow



def check_symbols_with_high():
    url = "https://contract.mexc.com/api/v1/contract/ticker"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        symbols = []

        for ticker in data['data']:
            symbol = ticker['symbol']
            high24Price = float(ticker['high24Price'])

            if check_symbols_with_10hr_24high(symbol,high24Price):
                #line = [symbol, round(price_change_percentage*100,2)]
                symbols.append(symbol)

        symbols.sort(key=lambda element: element[0], reverse=False)

        return symbols
    else:
        print("Failed to retrieve data from MEXC API.")
        return None


def check_ema(symbol):
    # Logic to check if current price > 50EMA for the symbol
    # Replace this with your own implementation
    return True  # Placeholder value


def calculate_rsi(df, period=14):
    close_prices = df['close'].values
    rsi = ta.momentum.RSIIndicator(close_prices, n=period)
    rsi_values = rsi.rsi()
    return rsi_values

def check_rsi(df):
    # Logic to check if RSI > 70 for the symbol
    df['rsi'] = ta.RSI((df['close']))
    return df  # Placeholder value

def calculate_macd(df, fast_period=12, slow_period=26, signal_period=9):


    macd, signal, hist = ta.MACD(df['close'], fast_period=fast_period, slow_period=slow_period, signal_period=signal_period)

    return macd, signal




def check_up_trend(symbol):

    return


def get_symbols_with_price_increase(rate):
    url = "https://contract.mexc.com/api/v1/contract/ticker"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #symbol_list=['ING_USDT','YGG_USDT','SNX_USDT','FET_USDT','JASMY_USDT','XCN_USDT','BFC_USDT','MASK_USDT','C98_USDT','MC_USDT','ID_USDT','PYR_USDT','ACH_USDT','SSV_USDT','ARPA_USDT','RSS3_USDT','MXC_USDT','HIGH_USDT','BICO_USDT','APM_USDT','RACA_USDT','GOAL_USDT','MDT_USDT','SIS_USDT','QUICK_USDT','DREP_USDT','AUCTION_USDT','POND_USDT','BSW_USDT','DODO_USDT','BEL_USDT','CYBER_USDT','BRISE_USDT','FRONT_USDT']
        #symbol_list=['BTC_USDT','ETH_USDT','CLORE_USDT','ARKM_USDT','GFT_USDT','LUNANEW_USDT','TARA_USDT','ASTRA_USDT','AUCTION_USDT','BIGTIME_USDT', 'BNXNEW_USDT', 'LQTY_USDT', 'LOOM_USDT', 'TOMI_USDT']
        symbol_list=['1000PEPE2_USDT',
 '1000BONK_USDT',
 'AGLD_USDT',
 'CFX_USDT',
 'INJ_USDT',
 'LINK_USDT',
 'MINA_USDT',
 'PEPE_USDT',
 'TRB_USDT',
 'UNFI_USDT']
        symbols = []
        current_trend = {symbol: None for symbol in symbol_list}

        for ticker in data['data']:
            message=''
            message_24high=''
            isHigh=''
            isLow=''
            up_trend=''
            up_count=0
            down_count=0
            symbol = ticker['symbol']
            lastPrice= ticker['lastPrice']
            fundingRate= ticker['fundingRate']
            price_change_percentage = float(ticker['riseFallRate'])
            high24Price= float(ticker['high24Price'])
            lower24Price= float(ticker['lower24Price'])
            #dt = datetime.now()
            dt = datetime.utcnow()  # utcnow class method
            dtobj3 = dt.replace(tzinfo=pytz.UTC)  # replace method

            dtobj_hongkong = dtobj3.astimezone(pytz.timezone("Asia/Hong_Kong"))  # astimezone method

            #dtobj_hongkong = dtobj3.astimezone(pytz.timezone("Asia/Hong_Kong"))  # astimezone method



            #isHigh, isLow= check_symbols_with_hr_24high(symbol, high24Price, lower24Price)

            dt = dtobj_hongkong.strftime("%Y-%m-%d %H:%M:%S")

            if lastPrice >= high24Price:
                message_24high = dt  + '<br> Up trend > 24high '

            #if fundingRate <= -0.001:
            if symbol in symbol_list:
                rsi_down = False
                ma20_down = False
                ma40_down = False
                macd_down = False

                rsi_up = False
                ma20_up = False
                ma40_up = False
                macd_up = False
                interval = "Min60"  # 1-hour candlestick data
                limit = 40

                kline = check_symbols_kline(symbol, interval, limit)
                df = pd.DataFrame(kline, columns=['time','open', 'low', 'high', 'close'])

                df.set_index('time', inplace=True)
                df.index = pd.to_datetime(df.index, unit='s', utc=True).map(lambda x: x.tz_convert('Asia/Hong_Kong'))

                df['rsi'] = ta.RSI((df['close']))
                macd, signal, hist = ta.MACD((df['close']), fastperiod=12, slowperiod=26, signalperiod=9)

                df['ma20'] = df['close'].rolling(20).mean()
                df['ma40'] = df['close'].rolling(40).mean()
                df['ret'] = df['close'].pct_change()
                price_len=len(str(lastPrice))



                if (df["rsi"].iloc[-1] < 30):
                    down_count=down_count+1
                    rsi_down=True


                # if (lastPrice < df["ma20"].iloc[-1]):
                #     down_count = down_count + 1
                #     ma20_down=True


                if (lastPrice < df["ma40"].iloc[-1]):
                    down_count = down_count + 1
                    ma40_down=True


                if (macd.iloc[-1] < signal.iloc[-1]):
                    down_count = down_count + 1
                    macd_down=True




                if (df["rsi"].iloc[-1] > 70):
                    up_count = up_count + 1
                    rsi_up=True


                # if (lastPrice > df["ma20"].iloc[-1]):
                #     up_count = up_count + 1
                #     ma20_up=True


                if (lastPrice > df["ma40"].iloc[-1]):
                    up_count = up_count + 1
                    ma40_up=True

                if (macd.iloc[-1] > signal.iloc[-1]):
                    up_count = up_count + 1
                    macd_up=True

                print(symbol, " down - " , rsi_down,ma20_down,ma40_down,macd_down)
                print(symbol , " Up - " , rsi_up,ma20_up,ma40_up,macd_up)


                if up_count >= 2:
                    trend='Up'
                elif down_count >= 2:
                    trend='Down'
                else:
                    trend='Neutral'


                isHigh, isLow = check_symbols_with_hr_24high(symbol, high24Price, lower24Price)

                line = [symbol, round(price_change_percentage*100,2),lastPrice,round(fundingRate*100,3),high24Price,lower24Price,trend,message_24high,isHigh,isLow,round(df["rsi"].iloc[-1],2),up_count, down_count]
                symbols.append(line)

        symbols.sort(key=lambda element: element[1], reverse=True)
        print(symbols)
        return symbols
    else:
        print("Failed to retrieve data from MEXC API.")
        return None

interval = "Day1"  # 1-hour candlestick data
limit=5
percent=20
# Fetch historical data using an API or from a CSV file
# Assuming you have OHLCV (Open, High, Low, Close, Volume) data
# stored in a pandas DataFrame named 'data'

# Assuming 'data' DataFrame has columns: ['timestamp', 'open', 'high', 'low', 'close', 'volume']
#data = check_symbols_kline(symbol, interval,limit)  # Replace this with your own data fetching logic

# list=check_symbols_with_increased_5d(percent,interval,limit)
# print(list)
# data=get_contract_info('TARA_USDT')
# print(data['lastPrice'],data['symbol'])
#print(check_symbols_with_high())

# Example usage
# rate = 0.05
# symbol_list = get_symbols_with_price_increase(rate)
# print(symbol_list)
# list=[]
# if symbol_list:
#     print("Symbols with price increase over :" + str(rate * 100) + "%")
#     for symbol in symbol_list:
#         list.append(symbol[0])
#         #print(symbol[0])
#

#print(list)