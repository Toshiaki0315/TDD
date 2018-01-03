from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def times(self, multiplier):
        pass
    
    @abstractmethod
    def plus(self, addend):
        pass
    
    @abstractmethod
    def reduce(self, bank, to):
        pass
