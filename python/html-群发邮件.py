import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = 'tuwei_tom@163.com'
password = input('请输入授权码:')

# 收信方邮箱
#to_addrs = ['1530213847@qq.com','tuwei1314@yeah.net']
to_addrs=[]
while True:
	a=input('请输入收件人邮箱地址:')
	to_addrs.append(a)
	b=input('请继续输入收件人地址，输入n退出:')
	if b=='n':
		break
	

# 发信服务器
smtp_server = 'smtp.163.com'
#text='''<html><h1>人生苦短，我用python</h1>
#<p>Python 邮件发送测试...</p>
#<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
#</html>
#'''
with open('test.html','r',encoding='utf-8') as file:
	content=file.read()
#msg = MIMEText(text,'plain','utf-8')
msg = MIMEText(content,'html','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
# 关闭服务器
server.quit()