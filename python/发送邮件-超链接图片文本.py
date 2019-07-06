import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender = 'tuwei_tom@163.com'
passwd = input('请输入邮箱授权码：') #发送人邮箱授权码
#receivers = 'tuwei1314@yeah.net'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['1530213847@qq.com','tuwei1314@yeah.net']
#或者将收件人写在excle中通过csv模块操作
msgRoot = MIMEMultipart('related')
msgRoot['From'] = sender
msgRoot['To'] =  ",".join(receivers)
subject = '邮件签名'
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)


mail_msg = """
<p>**********************************************</p>
<p>公司:深圳市零壹移动互联系统有限公司</p>
<p>职位:运维工程师</p>
<p>联系方式:tuwei_tom@163.com</p>
<p>***********************************************</p>
<p><a href="https://blog.51cto.com/tuwei">51CTO博客链接</a></p>
<p>个人51cto博客二维码如下</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('3.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
	smtpObj = smtplib.SMTP('smtp.163.com')
	smtpObj.login(sender,passwd)
	smtpObj.sendmail(sender, receivers, msgRoot.as_string())
	print("邮件发送成功")
except smtplib.SMTPException:
	print("Error: 无法发送邮件")
# 关闭服务器
smtpObj.quit()