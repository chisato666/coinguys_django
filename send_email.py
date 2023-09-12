import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import pandas as pd
import config
import mysql.connector
import re

regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

max_count=5

last_count=1
#This is the count for the last count number that send to the received.

def isValid(email):
    if re.fullmatch(regex, email):
        return True
    else:
        return False

mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    passwd=config.passwd,
    database=config.database
)

db = mydb.cursor()
sql = 'select * from EMAIL_LIST where send_count < ' + str(last_count) + ' order by row_num';


db.execute(sql)
rows = db.fetchall()

smtp_name="mail.hkwaishing.com"
login_name='trendyground@hkwaishing.com'
pwd='Socool666'


# smtp_name="smtp.gmail.com"
# login_name='bitcontrol2018'
# pwd='xgvgtothglqfqhag'


server= smtplib.SMTP(smtp_name,587)
server.starttls()
server.login(login_name,pwd)

msg = """
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>TrendyGround</title>
<style type="text/css">
body {
    margin-left: 0px;
    margin-top: 0px;
    background-color: #7F7F7F;
}
</style>
</head>

<body>
<table width="638" height="361" border="0" align="center">
  <tbody>
    <tr>
      <th height="357" scope="row"><img align="center" src="https://hkwaishing.com/trendyground1.png" alt="" width="900" height="1988" usemap="#Map"/>
</th>
    </tr>
  </tbody>
</table>
<map name="Map"><area shape="rect" coords="583,963,828,1178" href="https://trendyground.com/collections/electronic" alt="TrendyGround"><area shape="rect" coords="320,965,565,1180" href="https://trendyground.com/collections/bag" alt="TrendyGround"><area shape="rect" coords="58,965,303,1180" href="https://trendyground.com/collections/wallet" alt="TrendyGround"><area shape="rect" coords="583,732,828,947" href="https://trendyground.com/collections/antique" alt="TrendyGround"><area shape="rect" coords="319,733,564,948" href="https://trendyground.com/collections/scarf" alt="TrendyGround"><area shape="rect" coords="276,1560,419,1677" href="mailto:kenji_so@yahoo.com">
  <area shape="rect" coords="58,734,303,949" href="https://trendyground.com/collections/perfume" alt="TrendyGround">
  <area shape="rect" coords="458,1555,629,1678" href="https://facebook.com/trendyground2009">
  <area shape="rect" coords="659,1556,788,1675" href="https://api.whatsapp.com/send?phone=85296516506">
<area shape="rect" coords="4,8,898,412" href="https://trendyground.com">
  <area shape="rect" coords="82,1562,225,1679" href="https://carousell.app.link/JYeSrW8c1nb">
</map>
</body>
</html>


"""






from1= 'kenji_so@yahoo.com'
send_list=[]
count=1

for row in rows:
    send_count=int(row[2])+1
    row_count=row[0]
    print(row_count)


    to=row[1]

    if (send_count<=last_count) and (isValid(to)):
        #server.sendmail("kenji_so@yahoo.com", to, body)
        send_list.append(to)
        sql = 'update EMAIL_LIST set send_count='+ str(send_count) +' where row_num='+str(row_count)
        db.execute(sql)
        print(send_list)
        mydb.commit()

    if count > max_count:
        break

    count= count+1


# from_addr = 'kenji_so@yahoo.comm'
# to_addr = ['kenji_so@yahoo.com', 'chisato666@gmail.com']
#
# message = MIMEText(msg, 'html', 'UTF-8')
# message['From'] = Header("Trendyground", 'utf-8')  # 发送者
# message['To'] = Header("VIP customer", 'utf-8')  # 接收者
#
# subject = 'Thank you for your purchased from Trendyground'
# message['Subject'] = Header(subject, 'utf-8')
# server.sendmail(from_addr, to_addr, message.as_string())


# msg = MIMEMultipart()
# msg['From'] = from_addr
# msg['To'] = ','.join(to_addr)
# msg['Bcc'] = ", ".join(send_list)
# msg['Subject'] = "Thank you for your purchased before, this is trendyground"
#
# msg.attach(MIMEText(body, 'plain'))
#
# text = msg.as_string()
# server.sendmail(from_addr, to_addr, msg)



#msg="welcome to my life"

toaddr = '01partyroom@gmail.com'
cc = ['kenji_so@yahoo.com']
fromaddr = 'kenji_so@yahoo.com'

subject="Thank you for your purchased before, this is trendyground"
toaddrs = [toaddr] + cc + send_list



# body = f"Subject: {subject}\nFrom: {from1}\nTo: {toaddrs}\nContent-Type: text/html\n\n{msg}"  # This is where the stuff happens
#
# message_text = " "
# message = "From: %s\r\n" % fromaddr  + "To: %s\r\n" % toaddr + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % subject + "\r\n" + msg
#
# server.set_debuglevel(1)
# server.sendmail(from1, toaddrs, body)
# server.quit()



message = MIMEText(msg, 'html', 'utf-8')
message['From'] = Header("Trendyground", 'utf-8')  # 发送者
message['To'] = Header("trendyground", 'utf-8')  # 接收者

#subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    server.sendmail(fromaddr, toaddrs, message.as_string())
    print
    "邮件发送成功"
except smtplib.SMTPException:
    print
    "Error: 无法发送邮件"



print(send_list)