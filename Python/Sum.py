from Expression import Expression

class Sum(Expression):
    augend = None
    addend = None
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def plus(self, addend):
        return None
    
    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amount, to)

from Money import Money
