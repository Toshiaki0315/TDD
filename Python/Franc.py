from Money import Money

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
