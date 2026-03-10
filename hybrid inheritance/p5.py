#Online Course Platform

#<----- Base Class-------->
class User:
    def __init__(self,user_name,email):
        self.user_name=user_name
        self.email=email

    def user_details(self):
        print(f"User Name : {self.user_name}\n Email Id : {self.email}")

#<---------Dervied Classes------->
#<---Single level Inheritance------->
class Courses(User):
    def __init__(self, user_name, email,course_name,duration):
        User.__init__(self,user_name, email)
        self.course_name=course_name
        self.duration=duration

    def Course_info(self):
        print(f"{self.user_name} has enrolled in {self.course_name} for {self.duration}")

#<------------Multiple/Multilevel Inheritance----->
class Payment(User,Courses):
    def __init__(self, user_name, email,course_name,duration,mode,amount):
        User.__init__(self,user_name, email)
        Courses.__init__(self,course_name,duration)
        self.mode=mode
        self.amount=amount

    def Payment_details(self):
        self.Course_info()
        print(f"Payment of {self.amount} had been made using {self.mode}")


class Enrolled_students(User,Courses):
    def __init__(self, user_name, email,course_name,duration,enroll_id):
        User.__init__(self,user_name, email)
        Courses.__init__(self,course_name,duration)
        self.enroll_id=enroll_id

    def enroll_info(self):
        self.Course_info()
        print(f"Enrollment Id of the student is{self.enroll_id}")


class Premium_stduent(Enrolled_students,Payment):
    def __init__(self, user_name, email,course_name,duration,mode,amount):
        Enrolled_students.__init__(self,user_name, email,course_name,duration)
        Payment.__init__(mode,amount)

        if self.amount>=40000:
            self.badge="Golden"
            self.access_level="Full Access"
        else:
            self.badge="Basic"
            self.access_level="Limited Access"

    def check_premium_access(self):
        if self.amount>=40000:
            print(f"{self.user_name} is a student of Premium Batch with {self.badge} badge")
        else:
            print(f"{self.user_name} is a regular student, Upgrade to Premium to Access more Information ")

    def show_benefits(self):
        if self.badge=="Golden":
            print("Prenium Course Benefits : Full Course Access,Live Sessions, Mentorship and Certification")
        else:
            print("BAsics Access : limited Course Access,No Mentorship")
    



        