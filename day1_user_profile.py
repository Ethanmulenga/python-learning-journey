#-Task: Build a Simple User Profile Script
# Data types
name = input("Your Name please: ")
age = int(input("And your Age: "))
height = float(input("How tall are you: "))
is_student = input("Are you are student(yes/no): ").lower()
if is_student == "yes":
    is_student = True
else:
    is_student = False
nickname = None

#Print profile summary;
print("\nSimple User Profile:\n")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("student:", is_student)
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
