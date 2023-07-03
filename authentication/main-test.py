from user import User
from login import Login
import checkfields

#import generator.temporary_password as TemporaryPassword
#import generator.requirement as Requirement


#PROBLEMAS AO IMPORTAR ARQUIVO DE OUTRA PASTA
#DELETAR DEPOIS OS ARQUIVOS DUPLICADOS REQUIREMENT E TEMPORARY_PASSWORD

############## REGISTER ################

inputEmail = 'example@gmail.com'
inputKey = '0123456789abcdef'
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
        if(login.authorizeLogin(inputEmail, inputKey)):
            print('USUARIO LOGADO')  

############## AFTER LOGIN ##############        
        
userLogged = User() 
userLogged.setEmail(login.getInputEmail())
userLogged.setKey(login.getInputKey())
userLogged.setFolderName(login.getInputName())
userLogged.setFolderPath(login.getInputPath())
userLogged.setFullPath(login.getFullPath())
#del login

############## DISCONNECT ###############
userLogged.setIsLogged(False)
if not userLogged.getIsLogged():
    print('Desconectado')
    del userLogged

