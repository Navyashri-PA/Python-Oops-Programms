"""Software Development Lifecycle (SDLC) Automation System
✅ Single → User → Developer
✅ Multilevel → User → Developer → LeadDeveloper
✅ Hierarchical → User → Developer, User → Tester, User → DevOpsEngineer
✅ Multiple → ProjectManager(LeadDeveloper, Tester)"""


# Base class
class user:
    company_name="Tech park"
    location="Japan"
    
    def __init__(self,user_name,email):
        self.user_name=user_name
        self.email=email

    def user_details(self):
        print(f"User Name : {self.user_name}\nEmail : {self.email}")

# <-------single level Inheritance ------>
class developer(user):
    def __init__(self, user_name, email,language):
        user.__init__(self,user_name, email)
        self.language=language

    def write_code(self):
        print(f"{self.user_name} is  writting {self.language}")

#<------Multilevel Inheritance----->
class leaddeveloper(developer):
    def __init__(self, user_name, email, language,YOE,team_size):
        developer.__init__(self,user_name, email, language)
        self.YOE=YOE
        self.team_size=team_size

    def manage_team(self):
        print(f"{self.user_name} is leading {self.team_size} developer")

#<-----Hierarchial Inheritance----->
class Tester(user):
    def __init__(self, user_name, email,testing_tool):
        user.__init__(self,user_name, email)
        self.testing_tool=testing_tool


    def run_test(self):
        print(f"{self.user_name} is using {self.testing_tool} for testing")

class DevopsEnigneer(user):
    def __init__(self, user_name, email,cloud_platform):
        user.__init__(user_name, email)
        self.cloud_platform=cloud_platform
    
    def deploy(self):
        print(f"{self.user_name} is deploying application on {self.cloud_platform}")

#<-------Multiple Inheritance------->
class ProjectManager(leaddeveloper,Tester):
    def __init__(self, user_name, email, language, YOE, team_size,testing_tool,project_name,):
        leaddeveloper.__init__(self,user_name, email, language, YOE, team_size)
        Tester.__init__(self,user_name,email,testing_tool)
        self.project_name=project_name

    def show_project(self):
        print(f"{self.user_name} is Project Manager for {self.project_name} project")

    def show_deatils(self):
        print("<------Details -------->")
        self.user_details()
        self.write_code()
        self.manage_team()
        self.run_test()
        self.show_project()

obj=ProjectManager("keerthi","k@gmail.com","python",5,21,"Pytorach","E-cart")
obj.show_deatils()


