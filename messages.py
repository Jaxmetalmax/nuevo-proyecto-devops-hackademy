#!/usr/bin/env python
#-*- encoding=UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException
from email.mime.application import MIMEApplication
from os import path, environ
import traceback
import argparse

def sendmail(to_user, subject, content):
    to_list = " ,".join(to_user)
    mail_host = environ.get("MAIL_HOST")
    mail_port = 465
    mail_user = environ.get("MAIL_USER")
    mail_pass = environ.get("MAIL_PASS")
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = "bot@hackademy.lat"
    message['To'] = str(to_user)
    body = MIMEText(content, 'plain')
    message.attach(body)

    try:
        with smtplib.SMTP_SSL(mail_host,mail_port) as server:
            server.login(mail_user,mail_pass)
            server.send_message(message)
            server.quit()
    except SMTPException:
        traceback.print_exc()

