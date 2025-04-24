import validator
import menu

pies = [
    {"name": "Apple Pie", "price": 10},
    {"name": "Cherry Pie", "price": 12},
    {"name": "Blueberry Pie", "price": 15},
    {"name": "Pumpkin Pie", "price": 8},
    {"name": "Pecan Pie", "price": 14},
    {"name": "Lemon Meringue Pie", "price": 11},
    {"name": "Key Lime Pie", "price": 13},
    {"name": "Chocolate Cream Pie", "price": 9},
    {"name": "Banana Cream Pie", "price": 16},
    {"name": "Butter Chicken Pie", "price": 7}
]

column_headers = ["Index", "Pie Name", "Price ($)"]
column_widths = [8, 23, 7]

user_order = []

menu.print_menu(pies, column_headers, column_widths)

while True:
    # Get user input
    user_input = input("Please enter the index of the pie you want to order (or 'done' to finish): ")

    user_input = user_input.lower()

    # Check for commands
    if user_input in ("done", "d"):
        break

    elif user_input in ("menu", "m"):
        menu.print_menu(pies, column_headers, column_widths)

    elif user_input in ("clear", "c"):
        user_order.clear()
        print("Your order has been cleared.")

    elif user_input in ("show", "s"):
        print("Your current order:")
        menu.print_menu(user_order, column_headers, column_widths)
    else:
        # Validate input
        if not validator.validate_int(user_input):
            print("Invalid input. Please enter a valid index or a command.")
            continue

        # Convert to 0-based index
        order = int(user_input) - 1 

        if order >= 0 and order < len(pies):
            print(f"You have ordered {pies[order]['name']} for ${pies[order]['price']:.2f}.")
            user_order.append(pies[order])
        else:
            print("Invalid index. Please try again.")
        
print(user_order)
    