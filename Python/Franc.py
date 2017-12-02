class Franc:
  __amount = 0
  def __init__(self, amount):
    self.__amount = amount
  
  def times(self, multiplier):
    return Franc(self.__amount * multiplier)

  def __eq__(self, franc):
    return self.__amount == franc.__amount

