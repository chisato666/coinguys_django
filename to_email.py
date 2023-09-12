import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'kenji_so@yahoo.com'
receivers = ['kenji_so@yahoo.com','chisato666@gmail.com','bitcontrol2018@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

server= smtplib.SMTP("mail.hkwaishing.com",587)
server.starttls()
pwd='Socool666'
server.login("trendyground@hkwaishing.com",pwd)

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
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

message = MIMEText(msg, 'html', 'utf-8')
message['From'] = Header("kenji_so@yahoo.com", 'utf-8')  # 发送者
message['To'] = Header("trendyground", 'utf-8')  # 接收者

subject = 'Thank you for your purchased from Trendyground'
message['Subject'] = Header(subject, 'utf-8')

try:
    server.sendmail(sender, receivers, message.as_string())
    print
    "邮件发送成功"
except smtplib.SMTPException:
    print
    "Error: 无法发送邮件"