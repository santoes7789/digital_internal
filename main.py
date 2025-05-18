import random
import validator
from enum import Enum
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Bot names for the ordering system
bot_names = ["Alice", "Bob", "Charlie", "Daisy",
             "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Menu information stored in one array
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


def welcome():
    # Randomly select a bot name from the list
    bot_name = random.choice(bot_names)

    banner_width = 50

    print("=" * banner_width)
    print(f"Welcome to best pie shop, my name is {
          bot_name}".center(banner_width))
    print("=" * banner_width)


class Table():
    index_column_width = 8

    class RowType(Enum):
        SINGLE_LINE = 1
        DOULBLE_LINE = 2

    def __init__(self, headers, widths, keys, alignments=None, formats=None, index=False):
        self.headers = headers
        self.widths = widths
        self.keys = keys
        self.alignments = alignments if alignments else ["<"] * len(headers)
        self.formats = formats if formats else [""] * len(headers)
        self.index = index

    def single_line(self):
        print("--------------------------------------------")

    def double_line(self):
        print("============================================")

    def print(self, array):
        # Print header
        if self.index:
            print(f"{'Index':<{self.index_column_width}}", end="")

        for i in range(len(self.headers)):
            print(f"{self.headers[i]:<{self.widths[i]}}", end="")
        print()
        self.single_line()

        # Print pies
        for row, item in enumerate(array):
            if item == Table.RowType.SINGLE_LINE:
                self.single_line()
            elif item == Table.RowType.DOULBLE_LINE:
                self.double_line()
            else:
                if self.index:
                    print(f"{item.get("index", row + 1)
                          :<{self.index_column_width}}", end="")
                for i, key in enumerate(self.keys):
                    value = item.get(key, "")
                    print(f"{value:{self.alignments[i]}{
                          self.widths[i]}{self.formats[i]}}", end="")
                print()

        self.double_line()


class Order():
    def __init__(self):
        self.order = []
        self.done = False
        self.table = Table(headers=["Pie Name", "Price ($)"],
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
            print(Fore.RED + "Your order is empty. Please order before finishing.")
            return

        self.print_order()

        confirmation = input(
            "Are you sure you want to finish ordering? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()

        if confirmation in ("yes", "y"):
            print(Fore.GREEN + "You have confirmed your order")
            self.done = True
            return
        print(Fore.RED + "Order confirmation has been cancelled")

    # Prints menu

    def print_menu(self):
        print(Fore.BLUE + "Menu:")
        self.table.print(pies)

    def exit(self):
        if self.order:
            confirmation = input(
                "Are you sure you want to exit? All items in order will be cleared. (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
            if not confirmation in ("yes", "y"):
                return

        print("Exiting the ordering system. Goodbye!")
        self.done = True

    # Clears order asks for confirmation before doing so
    def clear_order(self):
        if not self.order:
            print(Fore.RED + "Your order is empty.")
            return

        confirmation = input(
            "Are you sure you want to clear your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            self.order.clear()
            print(Fore.GREEN + "Your order has been cleared.")
        else:
            print(Fore.RED + "Order not cleared.")

    # Shows current order
    def print_order(self):
        if not self.order:
            print(Fore.RED + "Your order is empty.")
            return

        print()
        print(Fore.BLUE + "Your current order:")
        table = self.order.copy()
        table.append(Table.RowType.SINGLE_LINE)  # Add a single line separator
        # Add total cost to the order list
        table.append({"index": "", "name": "Total Cost",
                     "price": self.calculate_cost()})
        self.table.print(table)

    # Removes pie from order
    def remove_pie(self):
        if not self.order:
            print(Fore.RED + "Your order is empty. Nothing to remove.")
            return

        print("Your current order:")
        self.table.print(self.order)

        remove_index = input("Enter the index of the pie you want to remove: ")

        # Checks if input is an integer
        if not validator.validate_int(remove_index):
            print(Fore.RED + "Invalid input. No item removed.")
            return

        # Convert to 0-based index
        remove_index = int(remove_index) - 1

        # Remove pie from order
        if 0 <= remove_index < len(self.order):
            removed_pie = self.order.pop(remove_index)
            print(Fore.GREEN +
                  f"Removed {removed_pie['name']} from your order.")
        else:
            print(Fore.RED + "Invalid index. No item removed.")

    def show_help(self):
        print("Available commands:")
        print("  'menu' or 'm':   Show the menu")
        print("  'done' or 'd':   Finish ordering")
        print("  'clear' or 'c':  Clear your order")
        print("  'show' or 's':   Show your current order")
        print("  'remove' or 'r': Remove a pie from your order")
        print("  'exit' or 'e':   Exit the ordering system")
        print("  'help' or 'h':   Show this help message")
        print()

    def starting_prompt(self):
        print("You can order pies from our menu below.")
        print("To order a pie, please enter the index number of the pie you want.")
        print()
        print("You can also type in commands for more options.")
        print()
        self.print_menu()
        print()
        self.show_help()

    def get_order(self):
        self.done = False

        while not self.done:
            # Get user input
            print()
            user_input = input(
                "Please enter the index of the pie you want to order (or 'done' to finish): ")

            # lowercase the input for case insensitive matching
            user_input = user_input.lower()

            commands = {
                ("done", "d"): self.finish,
                ("exit", "e"): self.exit,
                ("menu", "m"): self.print_menu,
                ("clear", "c"): self.clear_order,
                ("show", "s"): self.print_order,
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
                    print(
                        Fore.RED + "Invalid input. Please enter a valid index or a command.")

                # Add pie based on index
                else:
                    # Convert to 0-based index
                    order = int(user_input) - 1

                    if 0 <= order < len(pies):
                        print(Fore.GREEN +
                              f"You have ordered {pies[order]['name']} for ${
                                  pies[order]['price']:.2f}.")
                        self.order.append(pies[order])
                    else:
                        print(Fore.RED + "Invalid index. Please try again.")


def get_pickup_method():
    print(Style.BRIGHT + "PICKUP METHOD")
    while True:
        print("Would you like to pick up your order or have it delivered?")
        print("Input 'pickup' or 'p' for Pick up")
        print("Input 'delivery' or 'd' for Delivery")

        # Prompt user for input, case insensitive
        choice = input("Enter your choice: ").lower()

        # Find the user's choice, finding the first match in the list of options
        if choice in ("pickup", "pick up", "pick", "p"):
            print(Fore.GREEN + "You have chosen to pick up your order.")
            print()
            return False
        elif choice in ("delivery", "deliver", "d"):
            print(Fore.GREEN + "You have chosen to have your order delivered.")
            print()
            return True
        else:
            print(Fore.RED + "Invalid choice.")
            print()


class Details():
    def __init__(self):
        self.name = None
        self.phone = None
        self.address = None

        self.table = Table(
            headers=["Your Details:", ""],
            widths=[10, 30],
            keys=["Field", "Value"])

    def get_valid_input(self, prompt, validation_func):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input

    def print_details(self):
        table_data = []
        table_data.append({"Field": "Name:", "Value": self.name})
        table_data.append({"Field": "Phone:", "Value": self.phone})

        if self.address:
            table_data.append({"Field": "Address:", "Value": self.address})

        # print the table with customer details
        self.table.print(table_data)

    def get_details(self, delivery):
        print(Style.BRIGHT + "CUSTOMER DETAILS")
        self.name = self.get_valid_input(
            "Enter your name: ", validator.validate_name)
        self.phone = self.get_valid_input(
            "Enter your phone number: ", validator.validate_phone)
        if delivery:
            self.address = self.get_valid_input(
                "Enter your address: ", validator.validate_address)


def confirm(user_order, user_details):
    confirmed = False

    def confirm_order():
        nonlocal confirmed

        confirmation = input(
            "Are you sure you want to confirm your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            print(Fore.GREEN + "Order confirmed!")
            confirmed = True

    def abort():
        print(Fore.GREEN + "Order cancelled. Goodbye!")
        exit()

    def edit_order():
        print("Editing order...")
        user_order.get_order()
        print(Fore.GREEN + "Order updated!")

    def edit_details():
        print("Editing details...")
        user_details.get_details(delivery=True)
        print(Fore.GREEN + "Details updated!")

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

    print(Style.BRIGHT + "CONFIRMING YOUR ORDER")
    print("Just before we send your order, please check that all your details and order are correct.")

    while not confirmed:
        print()
        print("Type in a command for any action you want to take.")
        help()

        user_input = input("Enter command: ").lower()
        for key, command in commands.items():
            if user_input in key:
                command()
                break
        else:
            print(Fore.RED + "Invalid command. Please try again.")


def main():
    welcome()
    time.sleep(1)

    # Getting user order
    # Creates order class
    # prints out starting prompt
    # Then asks user for their order
    user_order = Order()
    user_order.starting_prompt()
    user_order.get_order()

    print()
    is_delivery = get_pickup_method()

    user_details = Details()
    user_details.get_details(is_delivery)

    print()
    confirm(user_order, user_details)


main()
