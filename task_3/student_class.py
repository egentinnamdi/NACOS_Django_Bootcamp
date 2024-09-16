class Student_Class:
    name=""
    age=""
    department = ""

    def get_details(self):
        self.name= input("What is your name?")
        self.age= int(input("How old are you?"))
        self.department=input("What department are you in?")

        return [self.name, self.age, self.department]
    
student1= Student_Class().get_details()[1]
student2= Student_Class().get_details()[1]
student3= Student_Class().get_details()[1]
student4= Student_Class().get_details()[1]

print(student1)
print(student2)
print(student3)
print("Name is the oldest student and is age years old")