#!/usr/bin/env python
# encoding: utf-8

"""
@author: clover
@file: SendMail.py
@time: 2018/9/10 22:44
"""

import configparser
from testdata.getpath import GetTestConfig
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import os
import mimetypes


class MyMail:

    def __init__(self,mail_config_file):
        config = configparser.ConfigParser()
        config.read(mail_config_file)

        self.smtp = smtplib.SMTP_SSL()
        self.login_user = config.get("SMTP", 'login_user')
        self.login_pwd = config.get("SMTP", 'login_pwd')
        self.from_addr = config.get("SMTP", 'from_addr')
        self.to_addrs = config.get("SMTP", 'to_addrs')
        self.host = config.get("SMTP", 'host')
        self.port = config.get("SMTP", 'port')

    # 连接邮箱服务器
    def connect(self):
        # self.smtp.set_debuglevel(True)
        # self.smtp.starttls()
        self.smtp.connect(self.host, self.port)

    # 登陆邮箱服务器
    def login(self):
        try:
            self.smtp.login(self.login_user, self.login_pwd)
        except Exception as e:
            print('%s' % e)

    # 发送邮件
    def sendmail(self, mail_subject, mail_content, attachment_path_set):
        # 构造MIMEMultipart对象做为跟容器
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = ','.join(eval(self.to_addrs))
        # 注意，这里的msg['To']只能为逗号分隔的字符串，形如  'aa@163.com','bb@qq.com'
        msg['Subject'] = mail_subject

        # 添加邮件内容
        content = MIMEText(mail_content, "html", _charset='gbk')
        # 说明，这里的_charset必须为gbk，和 # -*- coding:GBK -*- 保持一致，否则邮件内容乱码

        msg.attach(content)

        for attachment_path in attachment_path_set:
            if os.path.isfile(attachment_path):   # 如果附件存在
                type, coding = mimetypes.guess_type(attachment_path)
            if type == None:
                type = 'application/octet-stream'
            major_type, minor_type = type.split('/')
            with open(attachment_path, 'rb') as file:
                if major_type == 'text':
                    attachment = MIMEText(file.read(), _subtype=minor_type, _charset='GB2312')
                elif major_type == 'image':
                    attachment = MIMEImage(file.read(), _subtype=minor_type)
                elif major_type == 'application':
                    attachment = MIMEApplication(file.read(), _subtype=minor_type)
                elif major_type == 'audio':
                    attachment = MIMEAudio(file.read(), _subtype=minor_type)

            # 修改附件名称
            attachment_name = os.path.basename(attachment_path)
            attachment.add_header('Content-Disposition', 'attachment', filename=('gbk','', attachment_name))
            # 说明：这里的('gbk','', attachment_name)解决了附件为中文名称时，显示不对的问题

            msg.attach(attachment)

        # 得到格式化后的完整文本
        full_text = msg.as_string()
        # 发送邮件
        self.smtp.sendmail(self.from_addr, eval(self.to_addrs), full_text)

    # 退出
    def quit(self):
        self.smtp.quit()

if __name__ == '__main__':
    mymail = MyMail(GetTestConfig('mail.conf'))
    mymail.connect()
    mymail.login()
    mail_content = 'hi,测试'
    mail_title = '[测试]报告'
    attachments = set([GetTestConfig('mail.conf')])
    mymail.sendmail(mail_title, mail_content, attachments)
    mymail.quit()




