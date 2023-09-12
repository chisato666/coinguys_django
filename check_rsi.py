import requests
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import csv
import ta-lib
import ta
import function

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


df1 = yf.Ticker('BTC-USD').history(period='15m',interval='15m',start="2022-08-25", end="2022-08-26")[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]

df1.index.name = 'timestamp'

tog=df1

tog['change']= tog.Close.pct_change()
tog['RSI']= ta.rsi(tog['Close'])

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

#tog['rank']=function.price_sma_rank(tog.Close,tog.Close.rolling(5).mean())

#plt.figure(figsize=(20,10))
fig, axs = plt.subplots(2)
fig.suptitle('RSI vs BTC')
axs[0].axhline(y = 70, color = 'r', linestyle = 'dashed')

axs[0].axhline(y = 30, color = 'r', linestyle = 'dashed')
axs[0].plot(tog['RSI'])

axs[1].plot(tog['Close'])

plt.plot(tog['Close'], label='BTC')

#plt.legend()

tog = tog.reset_index()  # make sure indexes pair with number of rows
oversell=0
overbrough=0
for index,row in tog.iterrows():
    if row['oversell']==1:
        print("Oversell ",row[0],row[1],row[2])
        oversell=1
    if row['overbrough']==1:
        print("Overbrough ",row[0],row[1],row[2])
        overbrough=1

if (overbrough==1 or oversell==1):
    print(function.send_email('01partyroom@gmail.com'))


# smtp_name = "smtp.gmail.com"
# login_name = 'bitcontrol2018'
# pwd = 'xgvgtothglqfqhag'
#
# server = smtplib.SMTP(smtp_name, 587)
# server.starttls()
# server.login(login_name, pwd)
# cc = ['kenji_so@yahoo.com']
# fromaddr = 'kenji_so@yahoo.com'
#
# subject = "The RSI is under 30 or above 75"
# toaddrs ="01partyroom@gmail.com,kenji_so@yahoo.com"
# msg="Please check"
#
# body = f"Subject: {subject}\nFrom: {fromaddr}\nTo: {toaddrs}\nContent-Type: text/html\n\n{msg}"  # This is where the stuff happens
#
# message_text = " "
# message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddrs + "CC: %s\r\n" % ",".join(
#     cc) + "Subject: %s\r\n" % subject + "\r\n" + msg
# server.sendmail(fromaddr, toaddrs, body)
#plt.show()
