import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

# 发信的邮箱SMTP配置
smtp_server = 'smtp.qq.com'
port = '465'
# 发信的邮箱和授权码
username = '6973858@qq.com'
password = 'zntuizltafjjbhjg'
from_addr = username

# 收信地址
to_addrs = ['hah007@126.com','6973858@qq.com']

## 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = ''' 亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！
人生苦短，我用Python
'''
msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs)) 
msg['Subject'] = Header('python自动发送')


# server = smtplib.SMTP_SSL()   
# server.connect(smtp_server,port)
#以上两个都不行，按下面这个可以通过
server = smtplib.SMTP_SSL(smtp_server)

# 登陆发信邮箱
server.login(username, password)
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()
