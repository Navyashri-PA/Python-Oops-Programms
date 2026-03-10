class battery:
    var=None
    def __init__(self,capacity,voltage,type,charge_level,status):
        self.capacity=capacity
        self.voltage=voltage
        self.type=type
        self.charge_level=charge_level
        self.status=status
        if battery.var is None:
            battery.var=self
        else:
            raise Exception ("This is Single ton Class")
        
    def battery_info(self):
        print(f"Battery Capacity : {self.capacity}\nVoltage : {self.voltage}\nType : {self.type}\nCharge Level : {self.charge_level}\nsStatus : {self.status}")



class Mobile:
    b1=battery(7500,3.7,"Li-on","85%","Charging")
    # b2=battery(1000,5.5,"lithium","70%","Charging")
    def __init__(self,brand,model,storage,resolution,price):
        self.brand=brand
        self.model=model 
        self.storage=storage
        self.resolution=resolution
        self.price=price

    def mobile_info(self):
        print(f"Brand : {self.brand}\nModel : {self.model}\nStorage : {self.storage}\nResolution : {self.resolution}\nPrice : {self.price}")

m1=Mobile("Vivo","V17","256 GB","120 Mpx",17000)
m1.mobile_info()
m1.b1.battery_info()


        