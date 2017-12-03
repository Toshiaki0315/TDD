from Money import Money

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
  
    def times(self, multiplier):
        return Franc(self.amount * multiplier, self.currency_str)
