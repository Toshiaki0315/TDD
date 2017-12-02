from Money import Money

class Franc(Money):
#    __currency = ""
    def __init__(self, amount):
        self.amount = amount
        self.currency_str = "CHF"
  
    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def currency(self):
        return self.currency_str
