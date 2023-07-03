from requirement import Requirement
import re
import random
import string

class TemporaryPassword():

  def getPattern(self, Requirement):
    return fr"^(?=.*[a-z]{{{Requirement.getLowercase()}}})(?=.*[A-Z]{{{Requirement.getUppercase()}}})(?=.*\d{{{Requirement.getNumber()}}})(?=.*[!@#$%^&*()_\-+=\[\]{{}};':\"\\|,.<>\/?]{{{Requirement.getSpecial()}}}).*$"

  def getCharacters(self, Requirement):
    characters = ""
    if(Requirement.getLowercase()>0):
        characters += string.ascii_lowercase
    if(Requirement.getUppercase()>0):
        characters += string.ascii_uppercase
    if(Requirement.getNumber()>0):
        characters += string.digits
    if(Requirement.getSpecial()>0):
        characters += string.punctuation
    return characters

  def shufflePassword(self, password):
    shuffled_password = list(password)
    random.shuffle(shuffled_password)
    password = ''
    password = ''.join(shuffled_password)
    return password


  def getValue(self, Requirement):
      pattern = self.getPattern(Requirement)
      characters = self.getCharacters(Requirement)
      password = ""
      while not re.match(pattern, password):
          password = ''.join(random.choices(characters, k = Requirement.charactersAmount()))
      return self.shufflePassword(password)
