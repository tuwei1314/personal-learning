#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
#通过服务器postifx服务发送，先在收件方设置白名单，通过第三方发送，需要授权码
#sender = 'tuwei_tom@163.com'
sender = 'root@localhost'
#passwd = '' #发送人邮箱授权码
receivers = 'tuwei1314@yeah.net'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = sender
msgRoot['To'] =  receivers
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)


mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
	smtpObj = smtplib.SMTP('localhost')
	#smtpObj.login(sender,passwd)
	smtpObj.sendmail(sender, receivers, msgRoot.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")
