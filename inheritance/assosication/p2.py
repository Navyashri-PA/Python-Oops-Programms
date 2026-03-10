class Myclass:
    var=None
    def __init__(self):
        if Myclass.var is None:
            Myclass.var=self
        else:
            raise Exception("This is single ton class")
        
m1=Myclass()
