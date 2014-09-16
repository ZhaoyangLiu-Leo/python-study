# -*- coding: utf-8 -*-

#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

from email.mime.text import MIMEText


#注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，
#最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')
# 输入收件人地址:
to_addr = raw_input('To: ')


#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
#login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，
#邮件正文是一个str，as_string()把MIMEText对象变成str。
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

