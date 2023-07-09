from requirement import Requirement
from temporary_password import TemporaryPassword


# 10 / nº de requisitos (4) -> 1, 2, 3, 4
requirement = Requirement(0,0,0,0)
requirement.setLowercase(3)
requirement.setUppercase(4)
requirement.setNumber(2)
requirement.setSpecial(1)



temporaryPassword = TemporaryPassword()
print(temporaryPassword.getValue(requirement))