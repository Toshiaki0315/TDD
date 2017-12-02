from Money import Money

class Dollar(Money):
#    __currency = ""
    def __init__(self, amount):
        self.amount = amount
        self.currency_str = "USD"
  
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def currency(self):
        return self.currency_str