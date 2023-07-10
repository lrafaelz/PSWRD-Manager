import os
import smtplib
from email.message import EmailMessage
import multiprocessing as mp

class Email():
    # processes = []
    # def sendEmail(self, email_address_recipient):
    #     p = mp.Process(target=self.sendEmail2, args=(str(email_address_recipient)))
    #     p.start()
    #     self.processes.append(p)
    #     for p in self.processes:
    #         p.join()


    def sendEmail(self, email_address_recipient):
        file_path = os.path.abspath("authentication")
        with open(file_path + '/password.txt') as f:
            senha = f.readlines()
            f.close

        EMAIL_ADDRESS_SENDER = 'pswrdmanager.unipampa@gmail.com'
        EMAIL_PASSWORD_SENDER = senha[0]

        SUBJECT_EMAIL = 'Alerta de Segurança'
        BODY_EMAIL = 'Foram detectadas 3 tentativas de acesso sem sucesso ao seu banco de senhas.\n\n\nCaso tenham sido realizadas por você, por favor, desconsidere este e-mail.\n\nEste é um e-mail automático. Não é necessário respondê-lo.'

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

