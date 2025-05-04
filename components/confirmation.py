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


print("Please check your order and details before confirming:")
confirmation = input("Are you sure you want to confirm your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
if confirmation in ("yes", "y"):
    print("Order confirmed!")



