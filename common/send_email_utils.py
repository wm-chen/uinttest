# encoding: utf-8
# author: wm-chen
# send_email_utils.py
# 2021/3/12 5:01 下午
# desc:
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common import zip_utils
from common.config_utils import local_config


class SendEmail():

    def __init__(self, subject, body, smtp_file):
        self.smtp_server = local_config.get_smtp_server
        self.smtp_sender = local_config.get_smtp_sender
        self.smtp_senderpassword = local_config.get_smtp_senderpassword
        self.smtp_receiver = local_config.get_smtp_receiver
        self.smtp_subject = subject
        self.smtp_body = body
        self.smtp_file = smtp_file

    def mail_content(self):
        if self.smtp_file != None:
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__email_zip()
            # elif 扩展
        else:
            return self.__email_text()

    def mail_content_by_zip(self):
        dirname, file_path = os.path.split(self.smtp_file)
        report_zip_path = self.smtp_file + '/../../zip/' + file_path + '.zip'
        zip_utils.zip_dir(self.smtp_file, report_zip_path)
        self.smtp_file = report_zip_path  # 压缩后修改为压缩路径
        msg = self.mail_content()
        return msg

    def __email_text(self):
        #邮件消息题
        msg = MIMEText(self.stmp_body, 'html', 'utf-8')
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['subject'] = self.smtp_subject
        return msg

    def __email_zip(self):
       msg = MIMEMultipart()
       with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
            mime.add_header('Content-Disposition', 'attachment',
                            filename=('gb2312', '', self.smtp_file.split('/')[-1]))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
       msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
       msg['from'] = self.smtp_sender
       msg['to'] = self.smtp_receiver
       msg['subject'] = self.smtp_subject
       return msg

    def send_email(self):
        #发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_content = self.mail_content()
        smtp.sendmail(self.smtp_sender, self.smtp_receiver, mail_content.as_string())
        smtp.quit()

    def send_zip_email(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_content = self.mail_content_by_zip()
        smtp.sendmail(self.smtp_sender, self.smtp_receiver, mail_content.as_string())
        smtp.quit()


'''report_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'report/自动化测试报告V1.1')
SendEmail('测试', '测试', report_path).send_zip_email()'''

