#from email import Email

MAX_ATTEMPT = 3

class Login():

    def __init__(self):
        self.inputEmail = ''
        self.inputKey = '' #0123456789abcdef
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

    def getInputKey(self):
        return self.inputKey

    def setInputEmail(self, inputEmail):
        self.inputEmail = inputEmail
    
    def setInputKey(self, inputKey):
        self.inputKey = inputKey

    def getInputEmail(self):
        return self.inputEmail

    def getInputKey(self):
        return self.inputKey

    def separateData(self):
        with open("users.txt", "r", encoding="utf-8") as file:
            listUsers = file.readlines()
            file.close()

        listEmail = []
        listKey = []
        listName = []
        listPath = []
        index = 0

        while index < len(listUsers):
            if listUsers[index].strip() == '-':
                index += 1
                listEmail.append(listUsers[index].strip())

                index += 1
                listKey.append(listUsers[index].strip())

                index += 1
                listName.append(listUsers[index].strip())

                index += 1
                listPath.append(listUsers[index].strip())
            index += 1
            
        print(listEmail, listKey, listName, listPath)
        return listEmail, listKey, listName, listPath

    def isEmailValid(self, email):
        listEmail, _, _, _ = self.separateData()
        for nEmail in listEmail:
            if email == nEmail:
                return True
        return False

    def updateData(self, inputEmail, inputKey):
        if self.isEmailValid(inputEmail):
            self.updateAttempt(inputEmail)
        if not self.inputEmail == inputEmail:
            self.inputEmail = inputEmail 
        self.inputKey = inputKey

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

    def findFolderPath(self, inputEmail, indexEmail, listPath):
        return listPath[indexEmail]

    def findNamePath(self, inputEmail, indexEmail, listName):
        return listName[indexEmail]

    def findIndexEmail(self, inputEmail, listEmail):
        for nEmail in listEmail:
            if inputEmail == nEmail:
                return listEmail.index(nEmail)
        return -1

    def authorizeLogin(self, inputEmail, inputKey):
        listEmail, listKey, listName, listPath = self.separateData()
        indexEmail = self.findIndexEmail(inputEmail, listEmail)
        
        if indexEmail != -1:
            if listKey[indexEmail] == inputKey:
                self.inputPath = self.findFolderPath(inputEmail, indexEmail, listPath)
                self.inputName = self.findNamePath(inputEmail, indexEmail, listName)
                return True
        return False



if __name__ == "__main__":   
    inputEmail = 'guilhermecaneda@gmail.com'
    inputKey = '0123456789abcdef'
    login = Login()
    print(login.authorizeLogin(inputEmail, inputKey))
    print(login.inputPath)
    print(login.inputName)