import re
#from email import Email

MAX_ATTEMPT = 3

class Login():

    def __init__(self):
        self.inputEmail = ''
        self.inputKey = ''
        self.attempt = 0
        self.messageState = False

    def setInputEmail(self, inputEmail):
        self.inputEmail = inputEmail
    
    def setInputKey(self, inputKey):
        self.inputKey = inputKey

    def getInputEmail(self):
        return self.inputEmail

    def getInputKey(self):
        return self.inputKey

    def updateData(self, inputEmail, inputKey):
        self.updateAttempt(inputEmail)
        if not self.inputEmail == inputEmail:
            self.inputEmail = inputEmail 
        self.inputKey = inputKey

    
    #FALTA VERIFICAR SE EMAIL É VALIDO, OU SEJA, VERIFICAR NA BASE DE DADOS PARA NAO MANDAR EMAILSDESNECESSARIOS
    def updateAttempt(self, inputEmail):
        if self.attempt < MAX_ATTEMPT:
            if not self.inputEmail==inputEmail:
                self.attempt = 1
                self.messageState = False
            else:
                self.attempt += 1
        elif not self.messageState:
                #Email().sendEmail(self.inputEmail)
                print("Email enviado!")
                self.messageState = True

    def authorizeLogin(self):
        #teste login sucedido ou nao
        return False
