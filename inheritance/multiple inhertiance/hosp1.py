class hospital_members:
    hosp_name="<---Kaveri Clinic--->"
    def __init__(self,name,age,gender,contact_no,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.contact_no=contact_no
        self.address=address

    def hospital_details(self):
        print(f"Name= {self.name}\n Age= {self.age}\n Gender= {self.gender}\n Contact Number= {self.contact_no}\n Address= {self.address}")