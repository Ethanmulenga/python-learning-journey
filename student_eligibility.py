#Inputs 
name = input("Enter Your name: ")
age = int(input("Enter Your Age: "))
is_registered = input("Are you registered(YES/NO): ").lower()

#Boolean Logic
if is_registered == "yes":
    is_registered = True
elif is_registered == "no":
    is_registered = False
else:
    print("what are you doing ?")
    exit()

# Rule 1 Not Registered
if not is_registered:
    print("Access Denied: NOT REGISTERED")

# Rule 2 Age Check 
elif age < 0:
    print("Not Yet Born")
elif age < 16:
    print("Access Denied")

#Grade Logic
else: 
    grade = float(input("Enter Your grade: "))
    if grade < 0 or grade > 100:
        print("Invalid input")
    elif grade >= 75:
        print("Eligible For Advanced Program")
    elif grade >= 50:
        print("Eligible For Standard Program")
    else:
        print("Not Eligible For The Program")