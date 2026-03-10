# from p1 import Calculator
# class Mycalcii(Calculator):
#     def add(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(f"Sum = {self.n1 + self.n2}")
#         # (or)
#         print(f"sum = {self.n1+ self.n2}")

#     def sub(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(f"Subtraction = {self.n1 - self.n2}")

#     def multiply(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(f"Multiplication = {self.n1 * self.n2}")

#     def division(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(f"Division = {self.n1 / self.n2}")
        
# #Another Method
from p1 import Calculator
class Mycalcii(Calculator):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        
    def add(self):
        print(f"Sum = {self.n1 + self.n2}")
        # (or)
        print(f"sum = {self.n1+ self.n2}")

    def sub(self):
        print(f"Subtraction = {self.n1 - self.n2}")

    def multiply(self):
        print(f"Multiplication = {self.n1 * self.n2}")

    def division(self):
        print(f"Division = {self.n1 / self.n2}")
        
# #Another Method
# from p1 import Calculator
# class Mycalcii(Calculator):
#     def add(self,n1,n2):
#         print(f"Sum = {n1 + n2}")

#     def sub(self,n1,n2):
#         print(f"Subtraction = {n1 - n2}")

#     def multiply(self,n1,n2):
#         print(f"Multiplication = {n1 * n2}")

#     def division(self,n1,n2):
#         print(f"Division = {n1 / n2}")







