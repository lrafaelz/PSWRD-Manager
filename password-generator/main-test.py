from requirement import Requirement
from temporary_password import TemporaryPassword

requirement = Requirement()
requirement.setLowercase(3)
requirement.setUppercase(3)
requirement.setNumber(3)
requirement.setSpecial(3)

temporaryPassword = TemporaryPassword()
temporaryPassword.setValue(requirement)
print(temporaryPassword.getValue())