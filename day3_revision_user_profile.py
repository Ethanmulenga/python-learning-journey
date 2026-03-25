

#is_registered = input("Are You A registered User (Yes/No): ").lower()
#grade = float(input("Enter Your Grade: "))

# Main Logic
name = input("what is you name: ").lower()
while name == "":
      print("Enter a your name")
      name = input("what is you name: ").lower()
print(f"Welcome {name}")
age = int(input("Enter your age: "))
while age < 0 or age > 100:
      print("INVALID INPUT")
      age = int(input("Enter your age: "))
      if age < 16:
            print("ACCESS Denied: Not Eligible")
      age = int(input("Enter your age: "))
print("ACCESS Granted: You are Eligible")
is_registered = input("Are you Register (YES/NO): ").lower()
while is_registered == "":
      print("INVALID INPUT")
      is_registered = bool(input("Are you Register (YES/NO): ")).lower()
      if is_registered == "yes":
            is_registered == True
      elif is_registered == "no":
            is_registered == False
      else: 
            print("INCORRECT")
print(f"Registered: {is_registered}")

            




      