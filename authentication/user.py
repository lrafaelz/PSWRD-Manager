class User():

    def __init__(self):
        self.email = ''
        self.key = ''
        self.folderName = ''
        self.folderPath = ''
        self.isLogged = True

    def createUser(self):
        file = open(self.folderPath + self.folderName, "w")
        file.write(self.email())
        file.write("\n" + self.key())
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
