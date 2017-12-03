from Money import Money

class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
  
    def times(self, multiplier):
        return Dollar(self.amount * multiplier, self.currency_str)
