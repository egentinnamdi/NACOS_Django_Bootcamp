import re

name= input("What is your name?")
if len(name) < 2 or len(name) > 64:
    print("Name must be between 2 to 64 characters long")
    name= input("What is your name?")


age=int(input("How old are you?"))
if age < 16 or age > 30:
    print("Age must be between 16 to 30")
    age=int(input("How old are you?"))


department=input("What department are you in?")
if  not (department.isalpha()):
    print("Department name can only contain alphabets")
    department=input("What department are you in?")


reg_num=input("Please input your reg number")
pattern=r"^\d{4}/\d{6}$"
if not re.match(pattern, reg_num):
    print("Invalid reg number format")
    reg_num=input("Please input your reg number")



student_profile=[name,age, department, reg_num]
print(f"This user's name is {student_profile[0]}")