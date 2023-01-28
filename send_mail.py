"""This script is used to send mails"""

import smtplib
from email.message import EmailMessage
import os


def send_email(error_msg):
    """This function sends a mail to key
    stakeholdrs if the pipeline breaks at any point.

    Allows personnel to catch the error and fix"""

    EMAIL_ADDRESS = 'data@sendme.ng'
    EMAIL_PASSWORD = 'chvkobzwldwfxhtk'

    # New Email Message
    msg = EmailMessage()
    msg['Subject'] = 'BROKEN PIPELINE'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ['paulnwosu@sendme.ng']
    msg.set_content(f'Logged Error:/n {error_msg}')

    # Send the message
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__== '__main__':
    send_email('Just_testing')