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

class Order():
    def __init__(self):
        self.order = []

    

    # Calculates cost based on order 
    def calculate_cost(self):
        total_cost = 0
        for pie in self.order:
            total_cost += pie['price']
        return total_cost

    # Prints menu
    def print_menu(self):
        menu.print_table(pies, column_headers, column_widths)


    # Clears order asks for confirmation before doing so
    def clear_order(self):
        if not self.order:
            print("Your order is empty.")
            return

        confirmation = input("Are you sure you want to clear your order? (type yes to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            self.order.clear()
            print("Your order has been cleared.")
        else:
            print("Order not cleared.")

    # Shows current order
    def show_order(self):
        print("Your current order:")
        menu.print_table(self.order, column_headers, column_widths)
    
    # Removes pie from order
    def remove_pie(self):
        if not self.order:
            print("Your order is empty. Nothing to remove.")
            return

        self.show_order()

        remove_index = input("Enter the index of the pie you want to remove: ")

        # Checks if input is an integer
        if not validator.validate_int(remove_index):
            print("Invalid input. No item removed.")
            return

        # Convert to 0-based index
        remove_index = int(remove_index) - 1

        # Remove pie from order
        if 0 <= remove_index < len(self.order):
            removed_pie = self.order.pop(remove_index)
            print(f"Removed {removed_pie['name']} from your order.")
        else:
            print("Invalid index. No item removed.")
    
    def show_help(self):
        print("Available commands:")
        print("  'menu' or 'm':   Show the menu")
        print("  'done' or 'd':   Finish ordering")
        print("  'clear' or 'c':  Clear your order")
        print("  'show' or 's':   Show your current order")
        print("  'remove' or 'r': Remove a pie from your order")
        print("  'exit' or 'e':   Exit the ordering system")
        print("  'help' or 'h':   Show this help message")

    def get(self):
        print("Here are the available pies:")
        self.print_menu()
        print("To order a pie, please enter the index number of the pie you want.")
        print("You can also type in commands for more options.")
        self.show_help()

        while True:
            # Get user input
            user_input = input("Please enter the index of the pie you want to order (or 'done' to finish): ")
            user_input = user_input.lower()

            # Check for commands
            if user_input in ("done", "d"):
                if not self.order:
                    print("Your order is empty. Please add pies before finishing.")
                    continue

                self.show_order()

                confirmation = input("Are you sure you want to finish ordering? (type yes to confirm, anything else to cancel): ").lower()

                if confirmation in ("yes", "y"):
                    return True

            elif user_input in ("exit", "e"):
                confirmation = input("Are you sure you want to exit? All items in order will be cleared. (type yes to confirm, anything else to cancel): ").lower()

                if confirmation in ("yes", "y"):
                    print("Exiting the ordering system. Goodbye!")
                    return False

            elif user_input in ("menu", "m"):
                self.print_menu()

            elif user_input in ("clear", "c"):
                self.clear_order()

            elif user_input in ("show", "s"):
                if not self.order:
                    print("Your order is empty.")
                    continue

                self.show_order()
            
            elif user_input in ("remove", "r"):
                self.remove_pie()

            elif user_input in ("help", "h"):
                self.show_help()

            # Check if input is an integer, for ordering a pie
            elif not validator.validate_int(user_input):
                print("Invalid input. Please enter a valid index or a command.")

            # Add pie based on index
            else:
                # Convert to 0-based index
                order = int(user_input) - 1 

                if 0 <= order < len(pies):
                    print(f"You have ordered {pies[order]['name']} for ${pies[order]['price']:.2f}.")
                    self.order.append(pies[order])
                else:
                    print("Invalid index. Please try again.")
user_order = Order()
user_order.get()

menu.print_table(user_order.order, column_headers, column_widths)