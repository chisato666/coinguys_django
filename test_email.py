import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

s= smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
pwd='2018bitcontrol'
s.login("bitcontrol2018",pwd)

#s.set_debuglevel(1)
msg = MIMEMultipart('alternative')

body = """
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
      <th height="357" scope="row"><img align="center" src="http://hkwaishing.com/trendyground1.png" alt="" width="900" height="1988" usemap="#Map"/>
</th>
    </tr>
  </tbody>
</table>
<map name="Map"><area shape="rect" coords="533,1558,637,1678" href="https://www.etsy.com/hk-en/shop/Trendyground"><area shape="rect" coords="569,963,756,1179" href="https://trendyground.com/collections/electronic" alt="TrendyGround"><area shape="rect" coords="320,965,565,1180" href="https://trendyground.com/collections/bag" alt="TrendyGround"><area shape="rect" coords="129,969,322,1178" href="https://trendyground.com/collections/wallet" alt="TrendyGround"><area shape="rect" coords="569,737,745,949" href="https://trendyground.com/collections/antique" alt="TrendyGround"><area shape="rect" coords="319,733,564,948" href="https://trendyground.com/collections/scarf" alt="TrendyGround"><area shape="rect" coords="260,1562,369,1674" href="mailto:kenji_so@yahoo.com">
  <area shape="rect" coords="127,736,314,944" href="https://trendyground.com/collections/perfume" alt="TrendyGround">
  <area shape="rect" coords="396,1558,507,1679" href="https://facebook.com/trendyground2009">
  <area shape="rect" coords="659,1556,763,1676" href="https://api.whatsapp.com/send?phone=85296516506">
<area shape="rect" coords="90,4,807,407" href="https://trendyground.com">
  <area shape="rect" coords="110,1562,253,1679" href="https://carousell.app.link/JYeSrW8c1nb">
</map>
</body>
</html>

"""

from1='kenji_so@yahoo.com'
toaddr = 'kenji_so@yahoo.com'
cc = ['kenji_so@yahoo.com']
fromaddr = 'kenji_so@yahoo.com'
send_list=['chisato666@gmail.com,usebay2019@gmail.com']
subject="Thank you for your purchased before, this is trendyground"
toaddrs = [toaddr] + cc + send_list

body = f"Subject: {subject}\nFrom: {from1}\nTo: {toaddrs}\nContent-Type: text/html\n\n{body}"  # This is where the stuff happens


part1 = MIMEText(body,'html')

sender = 'kenji_so@yahoo.com'
to = ['kenji_so@yahoo.com']

cc = ['kenji_so@yahoo.com']

bcc = ['chisato666@gmail.com', 'usebay2019@gmail.com']
msg['Subject'] = "Thank you for your purchased before, this is trendyground"

msg['From'] = sender
msg['To'] = ", ".join(to)
msg['cc'] = ', '.join(cc)
#msg['bcc'] = ', '.join(bcc)

msg.attach(part1)
list=to+cc+bcc

print(list)
s.sendmail(sender, list, body)

s.quit()