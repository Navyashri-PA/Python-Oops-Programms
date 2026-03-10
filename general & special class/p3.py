#current Account:It is mainly used by the buisness person, here a person can
# withdraw money more than account balance over a specified 
# for particular interest rate from the bank(This is called Overdraft)
from p1 import Account
class Current_acc(Account):
    def __init__(self, name, acc_no, balance,overdraft_limit):
        super().__init__(name, acc_no, balance)
        self.overdraft_limit=overdraft_limit
        
    def Current_withdraw(self):
        amount=int(input("Enter the amount to withdraw :"))
        if amount<=0:
            print("Enter valid Amount")
        elif amount>self.balance+self.overdraft_limit:
            print(f"Withdrawn Denied : Over Exceed Overdraft limit")
        else:
            self.balance-=amount
            print(f"Amount Withdrawn :₹{amount} ")
            print(f"Remaining Balance :₹{self.balance}")
            
