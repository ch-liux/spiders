'''
Created on 2018年8月20日

@author: Administrator
'''

"""SMTP发送邮件
"""

# from email.mime.text import MIMEText
# msg = MIMEText('Hello, send by python eamil test.', 'plain', 'utf-8')
# 
# import smtplib
# server = smtplib.SMTP('smtp.qq.com', 25) # SMTP协议默认端口是25
# # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
# server.set_debuglevel(1)
# server.login('343134072@qq.com', 'LIUXuan720.')
# server.sendmail('343134072@qq.com', ['18283042497@163.com'], msg.as_string())
# server.quit()

# coding=utf-8
import smtplib
from email.mime.text import MIMEText
# 发送纯文本格式的邮件
msg = MIMEText('hello，send by python_test...','plain','utf-8')
#发送邮箱地址
sender = '343134072@qq.com'
#邮箱授权码，非登陆密码
password = 'LIUXuan720.'
#收件箱地址
receiver = '18283042497@163.com'
#smtp服务器
smtp_server = 'smtp.163.com'
#发送邮箱地址
msg['From'] = sender
#收件箱地址
msg['To'] = receiver
#主题
msg['Subject'] = 'from IMYalost'
server = smtplib.SMTP(smtp_server,25)

server.login(sender, password)
server.sendmail(sender,receiver,msg.as_string())
server.quit()


