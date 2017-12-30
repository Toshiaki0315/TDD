from Expression import Expression

class Money(Expression):
    amount = None
    currency_str = None

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency_str = currency

    def __eq__(self, money):
        return self.amount == money.amount and self.currency().__eq__(money.currency())

    def __repr__(self):
        return str(self.amount) + " " + self.currency_str

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_str)
    
    def currency(self):
        return self.currency_str

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self.currency_str, to)
        return Money(self.amount / rate, to)

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

from Sum import Sum
