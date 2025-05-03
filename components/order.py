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


class Order():
    def __init__(self):
        self.order = []
        self.done = False
        self.table = menu.Table(headers=["Pie Name", "Price ($)"],
                                widths=[23, 7],
                                keys=["name", "price"],
                                alignments=["<", ">"],
                                formats=["", ".2f"],
                                index=True)

    # Calculates cost based on order 
    def calculate_cost(self):
        total_cost = 0
        for pie in self.order:
            total_cost += pie['price']
        return total_cost

    # Finish ordering
    def finish(self):
        if not self.order:
            print("Your order is empty. Please order before finishing.")
            return

        self.show_order()

        confirmation = input("Are you sure you want to finish ordering? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()

        if confirmation in ("yes", "y"):
            self.done = True

    # Prints menu
    def print_menu(self):
        self.table.print(pies)

    def exit(self):
        if self.order:
            confirmation = input("Are you sure you want to exit? All items in order will be cleared. (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
            if not confirmation in ("yes", "y"):
                return

        print("Exiting the ordering system. Goodbye!")
        self.done = True

    # Clears order asks for confirmation before doing so
    def clear_order(self):
        if not self.order:
            print("Your order is empty.")
            return

        confirmation = input("Are you sure you want to clear your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            self.order.clear()
            print("Your order has been cleared.")
        else:
            print("Order not cleared.")

    # Shows current order
    def show_order(self):
        if not self.order:
            print("Your order is empty.")
            return

        print("Your current order:")
        table = self.order.copy()
        table.append(menu.RowType.SINGLE_LINE)  # Add a single line separator
        table.append({"index": "", "name": "Total Cost", "price": self.calculate_cost()})  # Add total cost to the order list
        self.table.print(table)
    
    # Removes pie from order
    def remove_pie(self):
        if not self.order:
            print("Your order is empty. Nothing to remove.")
            return

        print("Your current order:")
        self.table.print(self.order)

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

    def get_order(self):
        print("Here are the available pies:")
        self.print_menu()
        print("To order a pie, please enter the index number of the pie you want.")
        print("You can also type in commands for more options.")
        self.show_help()
        
        self.done = False

        while not self.done:
            # Get user input
            user_input = input("Please enter the index of the pie you want to order (or 'done' to finish): ")

            # lowercase the input for case insensitive matching
            user_input = user_input.lower()

            commands = {
                ("done", "d"): self.finish,
                ("exit", "e"): self.exit,
                ("menu", "m"): self.print_menu,
                ("clear", "c"): self.clear_order,
                ("show", "s"): self.show_order,
                ("remove", "r"): self.remove_pie,
                ("help", "h"): self.show_help
            }

            # Check if input matches any command
            for key, command in commands.items():
                if user_input in key:
                    command()
                    break

            # Check if input is an integer, for ordering a pie
            else:
                if not validator.validate_int(user_input):
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