class Money:
    amount = 0
    currency_str = ""

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency_str = currency

    def __eq__(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

    def times(self, multiplier):
        raise NotImplementedError
    
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