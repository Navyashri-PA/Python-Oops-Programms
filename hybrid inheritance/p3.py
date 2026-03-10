#College Administration System

#<-------Base Class----->
class Person:
    College="Nalanda University"
    Location="Takshashila"

    def __init__(self,name,age):
        self.name=name
        self.age=age


#<-------Derived Class------>
class student(Person):
    def __init__(self, name, age,branch,std_id,CGPA):
        Person.__init__(self,name, age)
        self.branch=branch
        self.CGPA=CGPA
        self.std_id=std_id

    def std_info(self):
        print(f"{self.name} is a student studing in {self.branch} and has a CGPA of {self.CGPA}")

obj_std=student("Karthik",18,"CSE","CS123",8.3)
obj_std.std_info()

class Teacher(Person):
    def __init__(self, name, age,subject,YOE):
        Person.__init__(self,name, age)
        self.subject=subject
        self.YOE=YOE

    def teacher_info(self):
        print(f"{self.name} is teaching a subject of {self.subject} and has a {self.YOE} of Experience")

obj_tech=Teacher("Geetha",55,"Maths","6+")
obj_tech.teacher_info()

# <------Multilevel inheritance--->
class Teaching_Assistent(student,Teacher):
    def __init__(self, name, age, branch, std_id, CGPA,subject,YOE,stipend):
        student.__init__(self,name, age, branch, std_id, CGPA)
        Teacher.__init__(self,name,age,subject,YOE)
        self.stipend=stipend

    def Tech_info(self):
            print(f"{self.name} is working as {self.subject} Teaching Assistant in {self.branch} Depatment and as a stipend of {self.stipend} ")

obj_assiatant=Teaching_Assistent("Divya",27,"ECE","123CS",9,"'Digital Electronics'","None","$25000")
obj_assiatant.Tech_info()
