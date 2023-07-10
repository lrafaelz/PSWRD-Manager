class Requirement():
  def __init__(self, uppercase:int, lowercase:int, number:int, special:int):
    self.uppercase = uppercase
    self.lowercase = lowercase
    self.number = number
    self.special = special

  def charactersAmount(self):
    return self.uppercase + self.lowercase + self.special + self.number

  ### GETTERS AND SETTERS ###

  def setUppercase(self, uppercase):
    self.uppercase = uppercase

  def setLowercase(self, lowercase):
    self.lowercase = lowercase

  def setSpecial(self, special):
    self.special = special

  def setNumber(self, number):
    self.number = number

  def getUppercase(self):
    return self.uppercase

  def getLowercase(self):
    return self.lowercase

  def getSpecial(self):
    return self.special

  def getNumber(self):
    return self.number

  ###########################                     