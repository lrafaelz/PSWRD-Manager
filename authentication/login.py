# from email import Email
# import authentication.email as Email
from authentication.email import Email
import os
MAX_ATTEMPT = 2

class Login():
    
    email = Email()

    def __init__(self):
        self.inputEmail = ''
        self.inputPath = '' 
        self.inputName = '' 
        self.attempt = 0
        self.messageState = False

    def resetData(self):
        self.inputEmail = ''
        self.inputPath = '' 
        self.inputName = '' 
        self.attempt = 0
        self.messageState = False

    def getFullPath(self):
        return self.inputPath + "\n" + self.inputName + '.txt'

    def getInputPath(self):
        return self.inputPath

    def getInputName(self):
        return self.inputName
    
    def setInputName(self, inputName):
        self.inputName = inputName

    def setInputEmail(self, inputEmail):
        self.inputEmail = inputEmail
    
    def getInputEmail(self):
        return self.inputEmail

    def separateData(self):
        file_path = os.path.abspath("authentication")
        with open(file_path + "/users.txt", "r", encoding="utf-8") as file:
            listUsers = file.readlines()
            file.close()

        listEmail = []
        listName = []
        listPath = []
        index = 0

        while index < len(listUsers):
            if listUsers[index].strip() == '-':
                index += 1
                listEmail.append(listUsers[index].strip())

                index += 1
                listName.append(listUsers[index].strip())

                index += 1
                listPath.append(listUsers[index].strip())
            index += 1
            
        return listEmail, listName, listPath

    def isEmailValid(self, email):
        listEmail, _, _ = self.separateData()
        for nEmail in listEmail:
            if email == nEmail:
                return True
        return False

    def updateAttempt(self, inputEmail):
        if not self.inputEmail == inputEmail:
            self.attempt = 1
            self.messageState = False
        elif self.attempt < MAX_ATTEMPT:
            self.attempt += 1
        else:
            self.email.sendEmail(self.inputEmail)
            self.messageState = True
            print("Email enviado!")
            

    def updateData(self, inputEmail, inputKey):
        if self.isEmailValid(inputEmail):
            self.updateAttempt(inputEmail)
        if not self.inputEmail == inputEmail:
            self.inputEmail = inputEmail
        self.inputKey = inputKey
    

    def findFolderPath(self, inputEmail, indexEmail, listPath):
        return listPath[indexEmail]

    def findNamePath(self, inputEmail, indexEmail, listName):
        return listName[indexEmail]

    def findIndexEmail(self, inputEmail, listEmail):
        for nEmail in listEmail:
            if inputEmail == nEmail:
                return listEmail.index(nEmail)
        return -1

    def validateKey(self, inputKey):
        return True

    def authorizeLogin(self, inputEmail, inputKey):
        listEmail, listName, listPath = self.separateData()
        indexEmail = self.findIndexEmail(inputEmail, listEmail)
        
        if indexEmail != -1:
            if self.validateKey(inputKey):
                self.inputPath = self.findFolderPath(inputEmail, indexEmail, listPath)
                self.inputName = self.findNamePath(inputEmail, indexEmail, listName)
                return True
        return False
