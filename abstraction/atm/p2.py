from p1 import ATM
class ATM_info(ATM):
    
    def __init__(self,balance,card_inserted=False,pin_entered=False):
        self.card_inserted=card_inserted
        self.pin_entered=pin_entered
        self.balance=balance

    def insert_card(self):
        if self.card_inserted==True:
            print("Card is Inserted Sucessfully")
            self.card_inserted=True
        else:
            print("Please Insert the Card")

    def Enter_pin(self):
        if self.card_inserted==False:
            print("Please Insert your card before entering the PIN")
        else:
            pin=input("Enter 4 digit PIN : ")
            if pin=='1234':
                print("PIN Verfied Sucessfully")
                self.pin_entered=True
            else:
                print("Incorrect PIN , Try Again")
                
    def Cash_withdraw(self):
        if self.card_inserted==False:
            print("Please Insert your card First")
        elif self.pin_entered==False:
            print("Please Enter the PIN before Withdrawing")
        else:
            amount=int(input("Enter the Amount to Withdraw :"))
            if amount>self.balance:
                print("Insufficient Balance !")
            elif amount<=0:
                print("Enter Valid Amount")
            else:
                self.balance-=amount
                print(f"Please collect your Cash : ₹{amount}")
                print(f"Remaining Balance : ₹{self.balance}")
                
    def Cash_deposit(self):
        if self.card_inserted==False:
            print("Insert the Card First")
        elif self.pin_entered==False:
            print("Enter the PIN before Depositing the amount")
        else:
            amount=int(input("Enter the Amount to Deposit :"))
            if amount<=0:
                print("Enter the valid amount")
            else:
                self.balance+=amount
                print(f"₹{amount} has deposited sucessfuly")
                print(f"New Balance : {self.balance}")
                
    def Balance_enqiry(self):
        if self.card_inserted==False:
            print("Please Insert the Card first")
        elif self.pin_entered==False:
            print("Please Enter the PIN before checking the balance")
        else:
            print(f"Current Balance is {self.balance}")
    
    def Remove_card(self):
        if  self.card_inserted==False:
            print("No Card Inserted")
        else:
            print("Transaction is Successfull\nPlease Remove the Card")
            self.card_inserted=False
            self.pin_entered=False