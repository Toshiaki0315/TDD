class Money:
    amount = 0

    def __eq__(self, money):
        return self.amount == money.amount and self.__class__ == money.__class__

