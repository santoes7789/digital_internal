import validator
print("Would you like to pick up your order or have it delivered?")
print("Enter 1 for Pick up")
print("Enter 2 for Delivery")

choice = input("Enter your choice: ")
if not validator.validate_int(choice): 
    print("Invalid choice. Please enter 1 or 2.")
elif int(choice) == 1:
    print("You have chosen to pick up your order.")
elif int(choice) == 2:
    print("You have chosen to have your order delivered.")