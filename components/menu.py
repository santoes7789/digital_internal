# pie information stored in one array
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

user_order = []

def print_menu():
    column_headers = ["Index", "Pie Name", "Price ($)"]
    column_widths = [8, 23, 7]

    # print header
    for i in range(len(column_headers)):
        print(f"{column_headers[i]:<{column_widths[i]}}", end="")
    print()
    print("--------------------------------------------")

    # print pies
    for row, pie in enumerate(pies):
        print(f"{row + 1:<{column_widths[0]}}", end="")
        print(f"{pie['name']:<{column_widths[1]}}", end="")
        print(f"{pie['price']:>{column_widths[2]}.2f}", end="")
        print()
    print("============================================")

def get_order():
    while True:
        user_input = input("Please enter the index of the pie you want to order (or 'done' to finish): ")
        if user_input == "done":
            break

        order = int(user_input)
        if order > 0 and order <= len(pies):
            print(f"You have ordered {pies[order]['name']} for ${pies[order]['price']:.2f}.")
            user_order.append(pies[order])
        else:
            print("Invalid index. Please try again.")
    

print_menu()
get_order()
print(user_order)

