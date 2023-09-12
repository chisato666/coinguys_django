import mysql.connector
import config
import requests
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)


url = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html'
req = requests.get(url)

soup = BeautifulSoup(req.text, features='html.parser')
mycursor = mydb.cursor()

count=0
foo=0
col = [[foo for i in range(6)] for j in range(10)]
max_count=72

for t in soup.find_all():
     if t.name=='td':
          count = count + 1
          if count<=max_count:
              #print(t.text)
              row = count % 6
              col[row]=(t.text)
              #print("row  % s" % row)
              if row==0:
                  #print(col[0] + " " + col[1])
                  #params = ['?' for item in col]
                  #sql = 'INSERT INTO table (Col1, Col2. . .) VALUES (%s %s);' %  ','.join(col[0] + ','.join(col[1])
                  btc =col[4].replace(" BTC","")
                  btc = btc.replace(",","")
                  sql ='INSERT INTO BTC_TOP100 (BAL_BTC,COINS) VALUES ("' + str(col[1]) + '",' + btc + ")"
                  print(sql)
                  mycursor.execute(sql)
                  mydb.commit()

# mycursor.execute("INSERT INTO BTC_TOP100 (BAL_BTC, COINS) VALUES (%s,%s)",("0-0.001",12021))
# mydb.commit()

