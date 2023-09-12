import yfinance as yf
import pandas_ta as ta
import pandas as pd
import matplotlib.pyplot as plt

# Request historic pricing data via finance.yahoo.com API
df = yf.Ticker('BTC-USD').history(period='2y')[['Close', 'Open', 'High', 'Volume', 'Low']]

# # Calculate MACD values using the pandas_ta library
# df.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)

# Get the 26-day EMA of the closing price
k = df['Close'].ewm(span=12, adjust=False, min_periods=12).mean()

# Get the 12-day EMA of the closing price
d = df['Close'].ewm(span=26, adjust=False, min_periods=26).mean()

# Subtract the 26-day EMA from the 12-Day EMA to get the MACD
macd = k - d

# Get the 9-Day EMA of the MACD for the Trigger line
macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()

# Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
macd_h = macd - macd_s

# Add all of our new values for the MACD to the dataframe
df['macd'] = df.index.map(macd)
df['macd_h'] = df.index.map(macd_h)
df['macd_s'] = df.index.map(macd_s)

#print(df.index)
df.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)


fig, axs = plt.subplots(2)
fig.suptitle('BTCUSD vs MACD')
#axs[0].axhline(y = 70, color = 'r', linestyle = 'dashed')

axs[0].axhline(y = 0, color = 'r', linestyle = 'dashed')

axs[0].plot(df.index, df['macd'],color='C2')
axs[0].bar(df.index, df['macd_h'],color='red')
axs[0].plot(df.index, df['macd_s'],color='C4')



axs[1].plot(df.index,df['Close'])
# axs[1].plot(df.TT,df.SMA50, color='C2')
# axs[1].plot(df.TT,df.SMA200, color='C3')


plt.show()



# View our data
pd.set_option("display.max_columns", None)
#print(df)

