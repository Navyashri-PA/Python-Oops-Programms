#.Employee Role Hierarchy
   #Objective:
# To demonstrate hybrid inheritance in Python using classes like Employee, Developer, Manager, and TechLead.

#<----Base Class----->
class Employee:
    Company="Amazon"

    def __init__(self,name,email_id):
        self.name=name
        self.email_id=email_id

    def emp_info(self):
        print("<------Employees Details------->")
        print(f"Name : {self.name}\nEmail Id : {self.email_id}")

#<-----Devired Classes ---------->
class developer(Employee):
    
    def __init__(self,name,email_id,language):
        Employee.__init__(self,name,email_id)
        self.language=language

    def developer_info(self):
        print(f"{self.name} is a {self.language} developer")

developer1=developer("Allen","Allen31@gmail.com","Python")
print("Company :" ,developer.Company)
developer1.developer_info()


class manager(Employee):
    def __init__(self, name, email_id,team_size,YOE):
        Employee.__init__(self,name, email_id)
        self.team_size=team_size
        self.YOE=YOE

    def manager_info(self):
        print(f"{self.name} is a Manager of {self.team_size} members Team")

manager1=manager("Allen","Allen31@gmail.com",12,"3+")
manager1.manager_info()

#<----Multiple Inhertiance----->
class Techlead(developer,manager):
    def __init__(self, name, email_id, language,team_size,YOE,perfomance_rating):
        developer.__init__(self,name, email_id, language)
        manager.__init__(self,name,email_id,team_size,YOE)
        self.performance_rating=perfomance_rating

    def Techlead_info(self):
        print(f"{self.name} is a Teachlead in a Software Company with a Performance Rating of {self.performance_rating}")

obj_tech=Techlead("Allen","Allen31@gmail.com","Python",12,3,4.5)
obj_tech.Techlead_info()


