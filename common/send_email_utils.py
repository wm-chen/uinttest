# encoding: utf-8
# author: wm-chen
# send_email_utils.py
# 2021/3/12 5:01 下午
# desc:
import smtplib
from email.mime.text import MIMEText


class SendEmail():

    def __init__(self):
        self.smtp_server = 'smtp.qq.com'
        self.smtp_sender = '1033705945@qq.com'
        self.smtp_senderpassword = 'zrgexgpdvujgbfeb'
        self.smtp_receiver = '2646300133@qq.com'
        self.smtp_subject = '邮件测试'
        self.stmp_body = '邮件测试'

    def send_email(self):
        #邮件消息题
        msg = MIMEText(self.stmp_body, 'html', 'utf-8')
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['subject'] = self.smtp_subject
        #发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        smtp.sendmail(self.smtp_sender, self.smtp_receiver, msg.as_string())

SendEmail().send_email()