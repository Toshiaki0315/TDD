class Money:
    amount = 0
    currency_str = ""

    def __eq__(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

    def times(self, multiplier):
        raise NotImplementedError
    
    def currency(self):
        return self.currency_str

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

from Dollar import Dollar
from Franc import Franc