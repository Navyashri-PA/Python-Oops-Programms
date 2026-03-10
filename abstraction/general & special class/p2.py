#Specialization Class
from p1 import Account

class Savings_acc(Account):
    def __init__(self, name, acc_no, balance,interest_rate):
        super().__init__(name, acc_no, balance)
        self.interest_rate=interest_rate
        
    def add_interest(self):
        interest=self.balance*(self.interest_rate/100)
        self.balance+=interest
        print(f"₹{interest:,.2f} added to the account \n Current Balance :₹{self.balance:,.2f}")