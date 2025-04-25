while True:
    print("Would you like to pick up your order or have it delivered?")
    print("Input 'pickup' or 'p' for Pick up")
    print("Input 'delivery' or 'd' for Delivery")

    choice = input("Enter your choice: ").lower()

    if choice in ("pickup", "pick up", "pick", "p"):
        print("You have chosen to pick up your order.")
        break
    elif choice in ("delivery", "deliver", "d"):
        print("You have chosen to have your order delivered.")
        break
    else:
        print("Invalid choice.")