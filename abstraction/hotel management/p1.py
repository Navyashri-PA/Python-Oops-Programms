#Hotel Management
class Hotel:
    #class variable
    Hotel_name="Grand Palace Hotel"
    total_room=50
    gst_rate=12
    
    #Instance Variable
    def __init__(self,guest_name,room_no,days_stayed,room_rate ):
        self.guest_name=guest_name
        self.room_no=room_no
        self.days_stayed=days_stayed
        self.room_rate=room_rate
    
    #instance Method     
    def total_bill(self):
        base_amount=self.days_stayed*self.room_rate
        gst=base_amount*(Hotel.gst_rate/100)
        total=base_amount+gst
        print(f"Total Bill with GST : ₹{total:,.2f}")
        
    def cust_info(self):
        print(f"Guest : {self.guest_name}\nRoom NO : {self.room_no}\nStaying Duration: {self.days_stayed} days ")
          
    #class Method
    @classmethod
    def update_gst_rate(cls,new_rate):
        cls.gst_rate+=new_rate
        print(f"{cls.Hotel_name} as upgraded GST rate to : {cls.gst_rate}% for all the room bookings")
        
    #static Method
    @staticmethod
    def check_instructions():
        print("<-----Hotel Check Instructions----->")
        print("Check In Time  : 2 AM to 3 AM")
        print("Check Out Time : 11 AM to 12 AM")
        print("Please Carry Valid ID Proof")
        
        
#Object Creation
guest1=Hotel("Kiran",15,3,3000)
guest1.cust_info()
guest1.total_bill()
guest1.update_gst_rate(2)
guest1.check_instructions()
guest1.total_bill()
        
    