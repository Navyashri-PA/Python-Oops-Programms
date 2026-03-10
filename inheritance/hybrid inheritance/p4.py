#Smart Device System
"""This program demonstrates single, multilevel, hierarchical, and multiple inheritance in Python 
using electronic devices like smartphones, phones, and cameras.
It also shows instance methods performing multiple operations (calculations, updates, and logic) 
to simulate real-world functionality."""

#<-------Base Class------>
class Device:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def PowerOn(self,device_power):
        if device_power=="ON":
            print(f"{self.name} is ON")
        else:
            print(f"{self.name} is OFF")

    def Check_Battery(self,battery_life=None):
        if battery_life is None:
            print("Battery is not working")
        else:
            print("Battery is working")

    def Device_deatils(self):
        print(f"Name : {self.name}\tBrand : {self.brand}")


# <---------Single-Level inheritance----------->
class Phone(Device):
    def __init__(self, name, brand,sim_type):
        Device.__init__(self,name, brand)
        self.sim_type=sim_type
        self.call_history=[]

    def make_call(self,number):
        self.call_history.extend(number)
        if number is None:
           print("Call is not Made")
        
        
    def show_call_history(self):
        self.Device_deatils()
        if self.call_history is None:
            print("Empty Call Log")
        else:
           print(f"Call History : {self.call_history}")


p1=Phone("Kiran","Nokia","Airtel")
p1.make_call([9356791,56987422,8457592])
p1.show_call_history()


# <-------Hierarchical Inheritance------->
class Camera(Device):
    def __init__(self, name, brand,resolution):
        Device.__init__(self,name, brand)
        self.resolution=resolution
        self.Zoom_level=10
        self.Photos_taken=[]

    def take_Photo(self,Photos):
        self.Photos_taken.extend(Photos)
        if self.Photos_taken is None:
            print("NO Photos")
        else:
            print(f"Photos are {self.Photos_taken}")

    def show_Photo(self):
        print(f"{self.name} is taken a photo  with {self.resolution} Resolution")

c1=Camera("Geetha","Intel","250Mpx")
c1.show_Photo()
c1.take_Photo(["Dog",'Cat','Flower'])


# <-------Multiple/Multilevel Inheritance--------->
class Smartphone(Phone,Camera):
    def __init__(self, name, brand, sim_type,resolution,RAM,OS):
        Phone.__init__(self,name, brand, sim_type)
        Camera.__init__(self,name,brand,resolution)
        self.RAM=RAM
        self.OS=OS
        self.app_installed=[]

    def install_app(self,apps):
        self.app_installed.extend(apps)
        print(f"{apps} Installed")

    def Show_specifications(self):
        print(f"Brand: {self.brand}\tCamera : {self.resolution}\tOperating System : {self.OS}\t Sim Type : {self.sim_type}\t RAM : {self.RAM}")
        print(f"{self.app_installed} are Present in SmartPhone")


s1=Smartphone("Karan","Samsung","Jio","250Mpx","8GB","Android")
s1.install_app(['Snapchat','Whatsup,"facebook'])
s1.Show_specifications()     




        





