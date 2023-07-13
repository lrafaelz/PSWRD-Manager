import os

class User():

    def __init__(self):
        self.email = ''
        self.folderName = ''
        self.folderPath = ''
        self.fullPath = ''
        self.isLogged = False

    def logout(self):
        self.email = ''
        self.folderName = ''
        self.folderPath = ''
        self.fullPath = ''
        self.isLogged = False

    def setFullPath(self, fullPath):
        self.fullPath = fullPath

    def getFullPath(self):
        return self.fullPath

    def createUser(self):
        file_path = os.path.abspath("authentication")
        with open(file_path + "/users.txt", "a", encoding="utf-8") as file:
            file.write("-\n")
            file.write(self.email + '\n')
            file.write(self.folderName + '\n')
            file.write(self.folderPath + '\n')
            self.isLogged = True
            self.fullPath = self.folderPath + "/" + self.folderName
            file.close()

    def verifyUser(self, userEmail):
        file_path = os.path.abspath("authentication")
        vetor_emails = []
        with open(file_path + "/users.txt", 'r', encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                if '@' in linha:
                    email = linha.split()[0]
                    vetor_emails.append(email)

            for e in vetor_emails:
                if userEmail == e:
                    return False
        return True

    def setIsLogged(self, isLogged):
        self.isLogged = isLogged

    def getIsLogged(self):
        return self.isLogged

    def setEmail(self, email):
        self.email = email

    def setFolderName(self, folderName):
        self.folderName = folderName + ".txt"
    
    def setFolderPath(self, folderPath):
        self.folderPath = folderPath

    def getEmail(self):
        return self.email

    def getFolderName(self):
        return self.folderName
    
    def getFolderPath(self):
        return self.folderPath