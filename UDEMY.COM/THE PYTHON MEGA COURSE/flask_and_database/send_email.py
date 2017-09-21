# coding=utf-8
from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "tomasz.kluczkowski@gmail.com"
    from_password = "Silvare123!)"
    to_email = email
    subject = "Height data"
    message = "Hey there your height is <strong>%s</strong>. " \
              "Average height is <strong>%s</strong>. " \
              "This is calculated out of <strong>%s</strong> users."\
              % (height, average_height, count)
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

