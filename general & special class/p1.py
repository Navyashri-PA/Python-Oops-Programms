#General Class
class Account:
    Bank_name="HDFC"
    Branch="BTM"
    
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
        
    def deposit(self):
        amount=int(input("Enter the amount to be deposit:"))
        if amount<=0:
            print("Enter the Valid amount")
        else:
            self.balance+=amount
            print(f"The amount of ₹{amount} as been deposited")
    
    def withdraw(self):
        amount= int(input("Enter the amount to be Withdrawn : "))
        if amount<=0:
            print("Enter the Valid amount")
        elif amount>self.balance:
            print("Insufficient Balance")
        else:            
            self.balance-=amount
            print(f"₹{amount} is withdrawn")
            
    def current_bal(self):
        print(f"Account Holder : {self.name}")
        print(f"Current balance is ₹{self.balance}")
        
   
        
        