name = input("Enter your name: ")

while name == "":
    print("Invalid input")
    name = input("Enter your name: ")
print(f"Thanks {name}")
