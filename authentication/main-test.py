from user import User
from requirement import Requirement
from temporary_password import TemporaryPassword
from login import Login
import checkfields

#PROBLEMAS AO IMPORTAR ARQUIVO DE OUTRA PASTA
#DELETAR DEPOIS OS ARQUIVOS DUPLICADOS REQUIREMENT E TEMPORARY_PASSWORD

############## REGISTER ################

inputEmail = 'example@gmail.com'
inputKey = TemporaryPassword().setValue(Requirement(3,2,1,3))
#TESTE ABAIXO (VAI DAR ERRO AO USER.CREATEUSER())
inputFolderName = "teste"
inputFolderPath = "desktop/pswrd/"

user = User()
if(checkfields.SyntaxEmail(inputEmail)):
    if(checkfields.SyntaxFileName(inputFolderName)):
        if(checkfields.SyntaxFilePath(inputFolderPath)):
            user.setEmail(inputEmail)
            user.setKey(inputKey)
            user.setFolderName(inputFolderName)
            user.setFolderPath(inputFolderPath)
            user.createUser()

##############  LOGIN  #################

inputEmail = 'example@gmail.com'
inputKey = '21dsa5@da1BCa'

login = Login() 
if(checkfields.SyntaxEmail(inputEmail)):        
    if(checkfields.SyntaxKey(inputKey)):        
        login.updateData(inputEmail, inputKey)  
        #if(login.authorizeLogin()):  
         


############## AFTER LOGIN ##############        
        
userLogged = User() 
userLogged.setEmail(login.getInputEmail)
userLogged.setKey(login.getInputKey)
#UserLogged.setFolderName()
#UserLogged.setFolderPath()
#del login

############## DISCONNECT ###############
userLogged.setIsLogged(False)
if not userLogged.getIsLogged():
    print('Desconectado')
    del userLogged

