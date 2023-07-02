from requirement import Requirement
from temporary_password import TemporaryPassword

requirement = Requirement()
requirement.setLowercase(3)
requirement.setUppercase(4)
requirement.setNumber(2)
requirement.setSpecial(1)

temporaryPassword = TemporaryPassword()
temporaryPassword.setValue(requirement)
print(temporaryPassword.getValue())