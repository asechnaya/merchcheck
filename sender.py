#!/usr/bin/python -tt
import smtplib
import os
from datetime import date, datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD


TXT_SAVE_TEMPLATE = '{}, Inv_id: {}, Summ: {}; OutSumCurrency: {},Date: {}\n'

EMAIL_TO = ["amakarovskaya@например.ru"] 
EMAIL_FROM = "robot@например.ru"
EMAIL_SUBJECT = "Test notification from ROBOKASSA: "
filepath = u"D:\merchwebsites\monday.txt"
filename = "monday.txt"

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

DATA_EMAIL = 'Посмотреть сайты по следующим мерчантам: во вложении. Емейл отослан {}'.format(datetime.now())


def send_email():
    #msg = MIMEText(DATA_EMAIL)
    msg = MIMEMultipart()

    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM


    # attach the body with the msg instance
    msg.attach(MIMEText(DATA_EMAIL, 'plain'))

    # open the file to be sent
    attachment = open('D:\merchwebsites\monday_empty.txt', "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)





    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()


if __name__ == '__main__':
    send_email()
    print('email send!')
