import pandas as pd
from binance.client import Client
import numpy as np

client = Client()

def getdata(symbol, start):
    frame = pd.DataFrame(client.get_historical_klines(symbol, '1h', start))

    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Time', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame


def get_levels(date):
    values = [-0.618, 0.618, 1.618]
    series_ = df.loc[date:][1:2].squeeze()
    diff = series_.High - series_.Low
    levels = [series_.Close + i * diff for i in values]
    return levels


df = getdata('BTCUSDT', '2022-01-01')

df['price'] = df.Open.shift(-1)

dates = np.unique(df.index.date)

buys,sells= [],[]
trade_dates = []

in_position = False

# for date in dates:
#     for index,row in df[date:][2:].iterrows():
#         if not in_position:
#             sl,entry,tp = get_levels(date)
#             if row.Close >= entry:
#                 buys.append(row.price)
#                 trade_dates.append(date)
#                 in_position = True
#         if in_position:
#             if row.Close >= tp or row.Close <= sl:
#                 sells.append(row.price)
#                 in_position=False
#                 break

trades=pd.DataFrame([buys,sells])
trades.columns=trade_dates
trades.index = ['Buy','Sell']


trades=trades.T
trades['PnL'] = trades.Sell - trades.Buy
trades['PnL_rel'] = trades.PnL/trades.Buy
print((trades.PnL_rel + 1).cumprod())