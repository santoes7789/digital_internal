# This function prompts the user to choose between picking up their order or having it delivered.
# It continues to ask for input until a valid choice is made.
def pickup_method():
    while True:
        print("Would you like to pick up your order or have it delivered?")
        print("Input 'pickup' or 'p' for Pick up")
        print("Input 'delivery' or 'd' for Delivery")

        # Prompt user for input, case insensitive
        choice = input("Enter your choice: ").lower()

        # Find the user's choice, finding the first match in the list of options
        if choice in ("pickup", "pick up", "pick", "p"):
            print("You have chosen to pick up your order.")
            break
        elif choice in ("delivery", "deliver", "d"):
            print("You have chosen to have your order delivered.")
            break
        else:
            print("Invalid choice.")
pickup_method()