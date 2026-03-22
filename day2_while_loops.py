name = input("Enter your name: ")

while name == "":
    print("Invalid input")
    name = input("Enter your name: ")

# Another while loop
age = int(input("Enter your AGE: "))
while age < 0 or age > 100:
    print("INVALID INPUT")
    age = int(input("Enter your AGE: "))

# Another Loop
food = input("what food do you like (type X to stop) ?")

while food.upper() != "X":
     print(f"You Like {food}")
     food = input("what food do you like (type X to stop) ?")
print("WE ARE DONE HERE")
print(f"Thanks {name}")
