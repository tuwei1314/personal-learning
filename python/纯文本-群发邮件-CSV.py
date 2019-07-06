import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
import csv

# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = 'tuwei_tom@163.com'
password = input('请输入授权码:')

# 收信方邮箱
data = [['tuwei','1530213847@qq.com'],['tuwei','tuwei1314@yeah.net']]
# 发信服务器
smtp_server = 'smtp.163.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text='''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
with open('test.txt','r',encoding='utf-8') as file:
	text1=file.read()
#写入收件人数据,可以现在电脑上整理后需要发送的人员名单，便于后续复用
#with open('to_addrs.csv', 'w', newline='') as f:
#	writer = csv.writer(f)
#	for row in data:
#		writer.writerow(row)
#读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		to_addrs=row[1]
		print(to_addrs)
		msg = MIMEText(text1,'plain','utf-8')
		# 邮件头信息
		msg['From'] = Header(from_addr)
		msg['Subject'] = Header('python test')
		msg['To'] = Header(to_addrs)
		# 开启发信服务，这里使用的是加密传输
		try:
			server = smtplib.SMTP_SSL()
			server.connect(smtp_server,465)
			# 登录发信邮箱
			server.login(from_addr, password)
			# 发送邮件
			server.sendmail(from_addr, to_addrs, msg.as_string())
			print("邮件发送成功")
		except smtplib.SMTPException:
			print("Error: 无法发送邮件")
# 关闭服务器
server.quit()