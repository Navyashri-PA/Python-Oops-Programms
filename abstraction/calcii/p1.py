#Simple Calculator

from abc import ABC,abstractmethod

#Abstract Class
class Calculator(ABC):

    #Abstract Method

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def division(self):
        pass





    