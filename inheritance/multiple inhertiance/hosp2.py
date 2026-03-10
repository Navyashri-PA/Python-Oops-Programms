from hosp1 import hospital_members
class doctor(hospital_members):
    def __init__(self, name, age, gender, contact_no, address,specilization,licence_no,YOE,availability):
        super().__init__(name, age, gender, contact_no, address)
        self.specilization=specilization
        self.licence_no=licence_no
        self.YOE=YOE
        self.availability=availability

    def doctor_details(self):
        self.hospital_details()
        print(f"Specilization of the Doctor: {self.specilization}\n Licence No: {self.licence_no}\n Years of Experience: {self.YOE}\n Availability: {self.availability} ")
        

doc1=doctor("Pranathi",34,"Female",9668754215,"BTM layout,banglore","othropedition","0Xld123","5 yrs","Mon & Sat")
print(doc1.hosp_name)
doc1.doctor_details()