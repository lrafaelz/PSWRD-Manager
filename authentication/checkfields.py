import re
from pyparsing import Regex

class Check():

    def SyntaxEmail(inputEmail):
        if inputEmail != '':
            try:
                regexEmail = Regex(r'\b[A-Za-z0-9._%+-]+(?<!\.)@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
                regexEmail.parseString(inputEmail)
                return True
            except:
                return False
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