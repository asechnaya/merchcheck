#!/usr/bin/python -tt
import smtplib
import os
from datetime import date, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD

EMAIL_TO = ["юзер@ух.ru"]
EMAIL_FROM = "robot@ух.ru"
EMAIL_SUBJECT = "Test notification from УХ: "

# open the file to be sent
dir_path = u"D:\merchwebsites"
filenothing = r"monday_empty.txt"
fileerr = r"monday_err.txt"

files = [filenothing, fileerr]

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


    for f in files:  # add files to the message
        file_path = os.path.join(dir_path, f)
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename=f)
        msg.attach(attachment)

    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()


if __name__ == '__main__':
    send_email()
    print('email send!')
