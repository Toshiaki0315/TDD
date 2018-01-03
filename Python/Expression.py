from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def plus(self, addend):
        pass
    
    @abstractmethod
    def reduce(self, bank, to):
        pass
