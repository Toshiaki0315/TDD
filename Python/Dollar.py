from Money import Money

class Dollar(Money):
    def __init__(self, amount):
        self.amount = amount
  
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
