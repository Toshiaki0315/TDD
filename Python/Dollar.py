class Dollar:
  __amount = 0
  def __init__(self, amount):
    self.__amount = amount
  
  def times(self, multiplier):
    return Dollar(self.__amount * multiplier)

  def __eq__(self, dollar):
    return self.__amount == dollar.__amount

