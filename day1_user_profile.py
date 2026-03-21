#-Task: Build a Simple User Profile Script
# Data types
name = input("Your Name please: ")
age = int(input("And your Age: "))
height = float(input("How tall are you (yes/no): "))
is_student = bool(input("Are you are student: "))
nickname = None

#Print profile summary;
print("Simple User Profile:\n")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("student", is_student)
print("Nickname:", nickname)

#conditional 
if age >= 18:
    print("You are an adult")
else:
    print("You are too young")

#update age
age = age + 1
print("Next year you will be ", age)

#Type Checks 
print(type(name))
print(type(age))
print(type(is_student))
print(type(height))
print(type(nickname))
