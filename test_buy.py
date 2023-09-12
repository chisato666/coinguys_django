
# Import necessary packages
import csv
import yfinance as yf
import numpy as np
import talib

# Open file

buy_count=0
sell_count=0

buy_total=0
sell_total=0
row_count=0

balance=100000
buy_amount=0.4
sell_amount=0.4
stock_avg=0
stock_total=0

buy_ranking=14
sell_ranking=15
closing=2
in_position=False





df = yf.Ticker('BTC-USD').history(start="2021-01-01", end="2022-10-30",interval='1d')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]


df.index.name = 'timestamp'

#tog = df.merge(df1, on='timestamp')

tog=df

tog['change']= tog.Close.pct_change()
tog['RSI']= talib.RSI(tog['Close'])

tog['SMA200']=tog.Close.rolling(200).mean()
tog['SMA50'] =tog.Close.rolling(50).mean()

tog['SMA5'] =tog.Close.rolling(5).mean()

# tog['position']=np.where(tog.value>50,1,0)
# tog['fear']=np.where(tog.value<30,1,0)
# tog['greed']=np.where(tog.value>70,1,0)

tog['overbrough']=np.where(tog.RSI>70,1,0)
tog['oversell']=np.where(tog.RSI<30,1,0)
tog['10d_low']=tog.Close.rolling(10).min()

strategy= tog.change

tog['buy_ranking'] =  tog['oversell']
tog['sell_ranking'] =  tog['overbrough']

#df = df.reset_index()  # make sure indexes pair with number of rows
print(tog)
csvfile=open('so/output.csv', 'w', newline='')
candlestick_writer= csv.writer(csvfile, delimiter=',')
tog.to_csv('so/output.csv')

for index,row in tog.iterrows():
    if row_count > 0:
        # print("time {} buy_ranking {} sell_ranking {} ".format(row[0],row[20],row[21]))
        if (int(row['buy_ranking']) == 1):
            if in_position:
                print("It is overbought, but you already own it. time",index)

            elif balance > (buy_amount * float(row['Close'])):
                buy_total = buy_total + (buy_amount * float(row['Close']))
                buy_count = buy_count + buy_amount
                balance = balance - (buy_amount * float(row['Close']))
                stock_total = stock_total + (buy_amount * float(row['Close']))
                stock_avg = stock_total / buy_count
                print("BUY  time {} buy_count {} balance {} price {} stock_avg {} ".format(index, buy_count, balance,
                                                                                           float(row['Close']),
                                                                                           stock_avg))
                in_position = True

        if (int(row['sell_ranking']) == 1 and buy_count > 0 and float(row['Close']) > stock_avg):

            if (buy_count >= sell_amount) and in_position:

                sell_total = sell_total + (sell_amount * float(row['Close']))
                buy_count = buy_count - sell_amount
                stock_total = stock_avg * buy_count
                balance = balance + (sell_amount * float(row['Close']))
                sell_count = sell_count + 1
                in_position = False
                print("Sell  time {} buy_count {} balance {} price {} stock_avg {} ".format(index, buy_count, balance,
                                                                                            float(row['Close']),
                                                                                            stock_avg))
            else:
                print("It is overbought, but we don't own any. Time:",index)
    row_count = row_count + 1

print("buy_total {} buy_count {} sell_total {} sell_count{} balance {} price {} stock_avg {} ".format(buy_total,
                                                                                                      buy_count,
                                                                                                      sell_total,
                                                                                                      sell_count,
                                                                                                      balance, float(
        row['Close']), stock_avg))


