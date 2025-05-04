import order
import customer_details
pies = [
    {"name": "Apple Pie", "price": 10},
    {"name": "Cherry Pie", "price": 12},
    {"name": "Blueberry Pie", "price": 15},
    {"name": "Chocolate Cream Pie", "price": 9},
    {"name": "Banana Cream Pie", "price": 16},
    {"name": "Butter Chicken Pie", "price": 7}
]

user_order = order.Order()
user_order.order = pies

user_details = customer_details.CustomerDetails()
user_details.name = "John Doe"
user_details.phone = "1234567890"
user_details.address = "123 Main St, Springfield"

confirmed = False

def confirm_order():
    global confirmed

    confirmation = input("Are you sure you want to confirm your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
    if confirmation in ("yes", "y"):
        print("Order confirmed!")
        confirmed = True

def abort():
    print("Order cancelled. Goodbye!")
    exit()

def edit_order():
    print("Editing order...")
    user_order.get_order()
    print("Order updated!")

def edit_details():
    print("Editing details...")
    user_details.get_details(delivery=True)
    print("Details updated!")

def help():
    print("Available commands:")
    print("  'confirm' or 'c': Confirm the order")
    print("  'abort' or 'a':   Abort/cancel the order")
    print("  'order' or 'o':   Edit the order")
    print("  'details' or 'd': Edit my details")

commands = {
    ("abort", "a"): abort,
    ("confirm", "c"): confirm_order,
    ("order", "o"): edit_order,
    ("details", "d"): edit_details,
}

while not confirmed:
    print("Type in a command for any action you want to take.")
    help()

    user_input = input("Enter command: ").lower()
    for key, command in commands.items():
        if user_input in key:
            command()
            break
    else:
        print("Invalid command. Please try again.")
