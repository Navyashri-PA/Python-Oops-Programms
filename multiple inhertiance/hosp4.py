from hosp1 import hospital_members
class nurse(hospital_members):
    def __init__(self, name, age, gender, contact_no, address,ward_assigned,shift,emp_id,YOS):
        super().__init__(name, age, gender, contact_no, address)
        self.ward_assigned=ward_assigned
        self.shift=shift
        self.YOS=YOS
        self.emp_id=emp_id

    def nurse_details(self):
        self.hospital_details()
        print(f"Ward Assigned to the Nurse: {self.ward_assigned}\n Shift : {self.shift}\n Years of Service: {self.YOS}\n Employee ID: {self.emp_id} ")
        

nurse1=nurse("Pranathi",34,"Female",9668754215,"BTM layout,banglore","Ward NO 23","Night","Nurse123","5 yrs")
print(nurse1.hosp_name)
nurse1.nurse_details()