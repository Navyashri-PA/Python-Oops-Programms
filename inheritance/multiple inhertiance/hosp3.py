from hosp1 import hospital_members
class patient(hospital_members):
    def __init__(self, name, age, gender, contact_no, address,room_no,admission_date,medical_history=None):
        super().__init__(name, age, gender, contact_no, address)
        self.room_no=room_no
        self.admission_date=admission_date
        # self.medical_history=[]
        if medical_history==None:
            self.medical_history=[]
        else:
            self.medical_history=medical_history

    def patient_details(self):
        self.hospital_details()
        print(f"Room No: {self.room_no}\n Admission Date :{self.admission_date}\n Medical History : {self.medical_history}")

p1=patient("Kavya",55,"F",9582468,"kalkere,Tumkur","Room-201","21/05/2024",['cough','fever','headache','vomiting'])
p1.patient_details()
    
    



