class Money:
    amount = 0

    def __eq__(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

    def times(self, multiplier):
        raise NotImplementedError
    
    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

from Dollar import Dollar
from Franc import Franc