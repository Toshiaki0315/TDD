class Money(object):
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

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

from Dollar import Dollar
from Franc import Franc