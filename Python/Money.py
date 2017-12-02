class Money:
    amount = 0
    __currency = ""

    def __init__(self, amount, currency):
        self.amount = amount
        self.__currency = currency

    def __eq__(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

    def times(self, multiplier):
        raise NotImplementedError
    
    def currency(self):
        return self.__currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

from Dollar import Dollar
from Franc import Franc