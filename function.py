import requests

import math
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def isvalid(url):
	return requests.head(url).status_code < 400

def isRange(i,pp):

    if i >= len(pp):
        print("out")
        return ""
    else:
        #print(pp[i])
        print("Sell   i {} pp {} len{}".format(i, pp[i], len(pp)))
        return pp[i]


def send_email(toaddrs):
    smtp_name = "smtp.gmail.com"
    login_name = 'bitcontrol2018'
    pwd = 'xgvgtothglqfqhag'

    server = smtplib.SMTP(smtp_name, 587)
    server.starttls()
    server.login(login_name, pwd)
    cc = ['kenji_so@yahoo.com']
    fromaddr = 'kenji_so@yahoo.com'

    subject = "The RSI is under 30 or above 75"
    msg="Please check"

    body = f"Subject: {subject}\nFrom: {fromaddr}\nTo: {toaddrs}\nContent-Type: text/html\n\n{msg}"  # This is where the stuff happens

    message_text = " "
    message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddrs + "CC: %s\r\n" % ",".join(
        cc) + "Subject: %s\r\n" % subject + "\r\n" + msg
    server.sendmail(fromaddr, toaddrs, body)

# Calculate the price is in a high or low position,  base on the ratio of the current price is higher than SMA
# For rank return 10 is highest price, 0 is lowest price
def price_sma_rank(price, sma):
    ranking = 0
    ratio = 0
    print(sma)

    if sma is not None:
        sma=price

    if price > sma:
        ranking = 6
        ratio = (price - sma) / sma
        if ratio < 0.1:
            ranking = ranking + 1
        elif ratio < 0.2:
            ranking = ranking + 2
        elif ratio < 0.3:
            ranking = ranking + 3
        elif ratio < 0.4:
            ranking = ranking + 4
        else:
            ranking = ranking + 5

    else:
        ranking = 4
        ratio = (sma - price) / sma
        if ratio < 0.1:
            ranking = ranking - 1
        elif ratio < 0.2:
            ranking = ranking - 2
        elif ratio < 0.3:
            ranking = ranking - 3
        elif ratio < 0.4:
            ranking = ranking - 4
        else:
            ranking = ranking - 5

    return ranking
