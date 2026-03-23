

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




      