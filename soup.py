import requests
import config
from bs4 import BeautifulSoup
from lxml import etree
import mysql.connector
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)


mycursor = mydb.cursor()

url = 'https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html'
req = requests.get(url)

soup = BeautifulSoup(req.text, features='html.parser')
dom = etree.HTML(str(soup))
# res= (dom.xpath('/html/body/div[5]/table[1]/tbody/tr[1]/td[4]'))
# print(res[0].tag)

# for i in res:
#     print(i[1].attrib)
count=0
foo=0
col = [[foo for i in range(6)] for j in range(10)]

def get_btc_top100(connection,label):
    with connection:
#        btc_sql = 'select sum(COINS), DATE_FORMAT(CREATED_DATE, \'%d-%m\') from BTC_TOP100 group by DATE_FORMAT(CREATED_DATE, \'%d-%m\') order by CREATED_DATE';

        btc_sql = 'select sum(COINS)/(count(DATE_FORMAT(CREATED_DATE, \'%m\'))/12), count(DATE_FORMAT(CREATED_DATE, \'%m\'))/12, DATE_FORMAT(CREATED_DATE, \'%m\') from BTC_TOP100 group by DATE_FORMAT(CREATED_DATE, \'%m\') order by CREATED_DATE'

        mycursor.execute(btc_sql)

        rows = mycursor.fetchall()
        str(rows)[0:300]
        print(rows)
        btc = []
        d_date = []
        r_count=[]
        percent = 0
        for row in rows:
            btc.append(row[0])
            r_count.append(row[1])
            d_date.append(row[2])

        first=btc[0]
        count=0
        print(len(btc))

        while count < len(btc):
            if (count>0):
                percent = (btc[count]-btc[count-1])/btc[count] * 100
            print(str(percent) +"% ")
            count = count + 1


        # x axis values
        y = btc
        # corresponding y axis values
        x = d_date

        bars = plt.bar(x, y, fc='crimson', ec='navy')

        plt.bar_label(bars, [''] + [f'{(y1 - y0) / y0 * 100:+.2f}%' for y0, y1 in zip(y[:-1], y[1:])])

        #plt.plot(x, y, label=label)




#get_btc_top100(mycursor,"(0 - 0.001)")


mycursor = mydb.cursor()
#get_btc_top100(mycursor,"[100 - 1,000)")

mycursor = mydb.cursor()
get_btc_top100(mycursor,"[1,000 - 10,000)")

mycursor = mydb.cursor()
#get_btc_top100(mycursor,"[100,000 - 1,000,000)")

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('BTC')

# giving a title to my graph
plt.title('BTC top 100')

# function to show the plot
plt.show()



