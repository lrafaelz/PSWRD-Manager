import re

def SyntaxEmail(inputEmail):
        if inputEmail != '':
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(pattern, inputEmail):
                return True
        return False


def SyntaxKey(inputKey):
    if inputKey != '':
        return True
    return False 


def SyntaxFileName(inputFileName):
    if inputFileName != '':
        return True
    return False


def SyntaxFilePath(inputFilePath):
    if inputFilePath != '':
        return True
    return False


def EmailIsValid(self, email, file_path):
    #VERIFICAR SE EMAIL ESTÁ NA BASE DE DADOS
    print('F')