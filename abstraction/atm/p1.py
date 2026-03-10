from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass
    @abstractmethod
    def Enter_pin(self):
        pass
    @abstractmethod
    def Cash_withdraw(self):
        pass
    @abstractmethod
    def Cash_deposit(self):
        pass
    @abstractmethod
    def Balance_enqiry(self):
        pass
    @abstractmethod
    def Remove_card(self):
        pass