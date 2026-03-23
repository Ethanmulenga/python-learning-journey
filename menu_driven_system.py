print("\n WELCOME TO THE MENU DRIVEN SYSTEM \n")
# Show menu
print("1. Check Eligibilty")
print("2. Exit")
#main logic
#while True:
    #try:
     #   option = int(input("CHOOSE AN OPTION: "))
      #  if option == 1:
       #     name = input("Enter your name: ").lower()
        #    while name == "":
         #         print("Invalid input")
          #        name = input("Enter your name: ").lower()
           # print(f"Welcome {name}")
            #age = int(input("Enter Your Age: "))
            #print(f"You are {age} old")

        #elif option == 2:
         #   break
        #else:
         #   print("INVALID INPUT")
    #except ValueError:
     #   print("please enter a valid number")

#Repeat it again.
while True:
    try: 
        option = int(input("SELECT AN OPTION: "))
        if option == "1":
            name = input("ENTER YOUR NAME: ").lower()
            while name == "":
                  print("invalid input")
                  name = input("ENTER YOU NAME: ").lower()
            print(f"Welcome {name}")
            age = int(input("ENTER YOUR AGE: "))
            print(f"You are {age}")
        
        elif option == "2":
            break
        else:
            print("INVALID INPUT")

    except ValueError:
        print("please enter the right numbers ")    

