from p1 import a
class b(a):
    b=20
    def __init__(self,p,q):
        super().__init__(p)
        self.q=q

    def meth1(self):
        print(f"q={self.q}")
        self.meth()

o1=b(100,200)
o1.meth1()
print(o1.a)
print(o1.b)
