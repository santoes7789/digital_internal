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

column_headers = ["Index", "Pie Name", "Price ($)"]
column_widths = [8, 23, 7]

def print_menu(array, headers, widths):

    # Print header
    for i in range(len(headers)):
        print(f"{headers[i]:<{widths[i]}}", end="")
    print()
    print("--------------------------------------------")

    # Print pies
    for row, item in enumerate(array):
        print(f"{row + 1:<{column_widths[0]}}", end="")
        print(f"{item['name']:<{column_widths[1]}}", end="")
        print(f"{item['price']:>{column_widths[2]}.2f}", end="")
        print()
    print("============================================")

