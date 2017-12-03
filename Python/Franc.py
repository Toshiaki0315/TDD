from Money import Money

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
  
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_str)
