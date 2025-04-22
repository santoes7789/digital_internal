pie_names = ["Apple Pie", "Cherry Pie", "Blueberry Pie", 
             "Pumpkin Pie", "Pecan Pie", "Lemon Meringue Pie", 
             "Key Lime Pie", "Chocolate Cream Pie", 
             "Banana Cream Pie", "Butter Chicken Pie"]

pie_prices = [10, 12, 15, 8, 14, 11, 13, 9, 16, 7]

for index in range(len(pie_names)):
    print(f"{index + 1}. {pie_names[index]} - ${pie_prices[index]:.2f}")
print("====================================================")