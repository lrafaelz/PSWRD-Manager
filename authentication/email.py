import os
import smtplib
from email.message import EmailMessage

#https://www.youtube.com/watch?v=pJP6ruTiKX4&ab_channel=DevAprender 


with open('password.txt') as f:
    senha = f.readlines()
    f.close

EMAIL_ADDRESS_SENDER = 'pswrdmanager@gmail.com'
EMAIL_PASSWORD_SENDER = senha[0]

SUBJECT_EMAIL = 'Teste de envio de email'
BODY_EMAIL = 'Este email é do PSWRD Manager.'

class Email():
    def sendEmail(email_address_recipient):
        #create_email
        msg = EmailMessage()
        msg['Subject'] = SUBJECT_EMAIL
        msg['From'] = EMAIL_ADDRESS_SENDER
        msg['To'] = email_address_recipient
        msg.set_content(BODY_EMAIL)

        #send file
        #with open('nome_do_arquivo.formato', 'rb') as content_file:
        #    content = content_file.read()
        #    msg.add_attachment(content, maintype='application', subtype='formatosemponto', filename='nome_do_arquivo.formato')

        #send_email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS_SENDER, EMAIL_PASSWORD_SENDER)
            smtp.send_message(msg)

