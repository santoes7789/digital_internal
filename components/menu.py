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

# prints out pie info
for index, pie in enumerate(pies):
    print(f"{index + 1}. {pie["name"]} - ${pie["price"]:.2f}")
print("====================================================")