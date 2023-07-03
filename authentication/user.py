import os

class User():

    def __init__(self):
        self.email = ''
        self.key = ''
        self.folderName = ''
        self.folderPath = ''
        self.fullPath = ''
        self.isLogged = True

    def setFullPath(self, fullPath):
        self.fullPath = fullPath

    def getFullPath(self):
        return self.fullPath

    def createUser(self):
        with open("users.txt", "a", encoding="utf-8") as file:
            file.write("-\n")
            file.write(self.email + '\n')
            file.write(self.folderName + '\n')
            file.write(self.folderPath + '\n')
            file.write(self.key + '\n')
            self.fullPath = self.getFullPath()
            file.close()

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
    
    def setKey(self, key):
        self.key = key

    def getEmail(self):
        return self.email

    def getFolderName(self):
        return self.folderName
    
    def getFolderPath(self):
        return self.folderPath
    
    def getKey(self):
        return self.key
