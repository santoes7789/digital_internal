import random
import validator
from enum import Enum
from colorama import Style 
import utils

# TODO
# Add a comments
# Sort order by name
# Add more pies
# fucntion for thing i know what im takling abt
# remove address from details if pickup is selected

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

def program_end():
    print("Would you like to make a new order?")
    new_order = input(
        "Type 'yes' or 'y' to make a new order, anything else to exit: ").lower()

    if new_order in ("yes", "y"):
        main()
    else: 
        print("Goodbye!")
        
    exit()

# Prints a welcome message with a random bot name
def welcome():
    # Randomly select a bot name from the list
    bot_name = random.choice(bot_names)

    # Set the width of the banner
    banner_width = 50

    # Prints the welcome message
    # Uses utils.print functions to print with preset styles
    utils.print_title("=" * banner_width) # Prints ===== with length of banner width

    # Prints welcome message, centered with title style (bolded)
    utils.print_title(f"Welcome to best pie shop, my name is {bot_name}".center(banner_width)) 
    
    print()

    # Prints "Press enter to start!" centered, with header style (blue)
    utils.print_header("PRESS ENTER TO START ORDERING!".center(banner_width)) 
    utils.print_title("=" * banner_width)

    input() # Waits for user to press enter before continuing

class Order():
    commands = [
        {"command": "'menu' or 'm':", "description": "Show the menu"},
        {"command": "'done' or 'd':", "description": "Finish ordering"},
        {"command": "'clear' or 'c':", "description": "Clear your order"},
        {"command": "'show' or 's':", "description": "Show your current order"},
        {"command": "'remove' or 'r':", "description": "Remove a pie from your order"},
        {"command": "'exit' or 'e':", "description": "Exit the ordering system"},
        {"command": "'help' or 'h':", "description": "Show this help message"}
    ]

    command_table = utils.Table(
        headers=["Available commands:", ""], 
        widths=[20, 30], 
        keys=["command", "description"])

    def __init__(self):
        self.order = []
        self.done = False
        self.table = utils.Table(
                           headers=["Pie Name", "Price ($)"],
                           widths=[23, 7],
                           keys=["name", "price"],
                           alignments=["<", ">"],
                           formats=["", ".2f"],
                           index=True
                           )

    # Calculates cost based on order
    def calculate_cost(self):
        total_cost = 0
        for pie in self.order:
            total_cost += pie['price']
        return total_cost

    # Finish ordering
    def finish(self):
        if not self.order:
            utils.print_error("Your order is empty. Please order before finishing.")
            return

        self.print_order()

        print()

        confirmation = input(
            "Are you sure you want to finish ordering? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()

        if confirmation in ("yes", "y"):
            utils.print_success("You have finished ordering!")
            self.done = True
            return
        utils.print_error("Order confirmation has been cancelled.")

    # Prints menu

    def print_menu(self):
        utils.print_header("MENU:")
        return self.table.print(pies)

    def exit(self):
        if self.order:
            confirmation = input(
                "Are you sure you want to exit? All items in order will be cleared. (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
            if not confirmation in ("yes", "y"):
                return

        print("Exiting the ordering system.")
        print()
        program_end()

    # Clears order asks for confirmation before doing so
    def clear_order(self):
        if not self.order:
            utils.print_error("Your order is empty. Nothing to clear.")
            return

        confirmation = input(
            "Are you sure you want to clear your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            self.order.clear()
            utils.print_success("Your order has been cleared.")
        else:
            utils.print_error("Order has been not been cleared.")

    # Shows current order
    def print_order(self):
        if not self.order:
            utils.print_error("Your order is empty.")
            return

        utils.print_header("Your current order:")
        table = self.order.copy()
        table.append(utils.Table.RowType.SINGLE_LINE)  # Add a single line separator
        # Add total cost to the order list
        table.append({"index": "", "name": "Order Cost",
                     "price": self.calculate_cost()})
        return self.table.print(table)

    # Removes pie from order
    def remove_pie(self):
        if not self.order:
            utils.print_error("Your order is empty. Nothing to remove.")
            return

        utils.print_header("Your current order:")
        self.table.print(self.order)

        remove_index = input("Enter the index of the pie you want to remove: ")

        # Checks if input is an integer
        if not validator.validate_int(remove_index):
            utils.print_error("Invalid input. No item removed.")
            return

        # Convert to 0-based index
        remove_index = int(remove_index) - 1

        # Remove pie from order
        if 0 <= remove_index < len(self.order):
            removed_pie = self.order.pop(remove_index)
            utils.print_success(f"Removed {removed_pie['name']} from your order.")
        else:
            utils.print_error("Invalid index. No item removed.")

    def show_help(self):
        self.command_table.print(self.commands)
        
    def starting_prompt(self):
        utils.print_title("ORDERING SYSTEM") # Prints title 
        print("You can order pies from our menu below.")
        print("To order a pie, please enter the index number of the pie you want.")
        print()
        print("You can also type in commands for more options.")
        print()

        self.print_menu() # Prints menu

        # Offset the command table to put it on the right of the menu
        # x_offset is set to 50 to move it right
        # y_offset is set to 13 to move it up 
        self.command_table.x_offset = 50
        self.command_table.y_offset = 13

        # Print the command table
        self.show_help()

        # Reset the offsets to 0 for the next print
        self.command_table.x_offset = 0
        self.command_table.y_offset = 0

    def get_order(self):
        self.starting_prompt()
        self.done = False

        while not self.done:
            # Get user input
            print()
            user_input = input(
                "Please enter the index of the pie you want to order (or 'done' to finish): ")

            # lowercase the input for case insensitive matching
            user_input = user_input.lower()

            command_map = {
                ("done", "d"): self.finish,
                ("exit", "e"): self.exit,
                ("menu", "m"): self.print_menu,
                ("clear", "c"): self.clear_order,
                ("show", "s"): self.print_order,
                ("remove", "r"): self.remove_pie,
                ("help", "h"): self.show_help
            }

            # Check if input matches any command
            for key, command in command_map.items():
                if user_input in key:
                    command()
                    break

            # Check if input is an integer, for ordering a pie
            else:
                if not validator.validate_int(user_input):
                    utils.print_error("Ivalid input. Please enter a valid index or a command.")

                # Add pie based on index
                else:
                    # Convert to 0-based index
                    order = int(user_input) - 1

                    if 0 <= order < len(pies):
                        utils.print_success(
                            f"You have ordered {pies[order]['name']} for ${pies[order]['price']:.2f}.")
                        self.order.append(pies[order])
                    else:
                        utils.print_error(
                            "Invalid index. Please enter a valid index from the menu.")


def get_pickup_method():
    utils.print_title("PICKUP METHOD")
    while True:
        print("Would you like to pick up your order or have it delivered?")
        print("Input 'pickup' or 'p' for Pick up")
        print("Input 'delivery' or 'd' for Delivery " + Style.BRIGHT + "(Costs an additional $14)")

        # Prompt user for input, case insensitive
        choice = input("Enter your choice: ").lower()

        # Find the user's choice, finding the first match in the list of options
        if choice in ("pickup", "pick up", "pick", "p"):
            utils.print_success("You have chosen to pick up your order.")
            return False
        elif choice in ("delivery", "deliver", "d"):
            utils.print_success("You have chosen to have your order delivered.")
            return True
        else:
            utils.print_error("Invalid choice. Please enter 'pickup' for Pick up, or 'delivery' for Delivery.")


class Details():
    def __init__(self):
        self.name = None
        self.phone = None
        self.address = None

        self.table = utils.Table(
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
        return self.table.print(table_data)

    def get_details(self, delivery):
        utils.print_title("CUSTOMER DETAILS")
        self.name = self.get_valid_input(
            "Enter your name: ", validator.validate_name)
        self.phone = self.get_valid_input(
            "Enter your phone number: ", validator.validate_phone)
        if delivery:
            self.address = self.get_valid_input(
                "Enter your address: ", validator.validate_address)


def confirm(user_order, user_details, delivery):
    confirmed = False

    def confirm_order():
        nonlocal confirmed

        confirmation = input(
            "Are you sure you want to confirm your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            utils.print_success("Your order has been confirmed!")
            utils.print_success("Thank you for ordering with us!")
            if delivery:
                utils.print_success("Your order will be delivered to " +
                                    user_details.address + " soon.")
            else:
                utils.print_success("Your order will be ready for pickup soon.")
                utils.print_sucesss("You will recieve a text message when it is ready.")
            confirmed = True

    def abort():
        nonlocal confirmed
        confirmation = input(
            "Are you sure you want to abort your order? (type 'yes' or 'y' to confirm, anything else to cancel): ").lower()
        if confirmation in ("yes", "y"):
            utils.print_error("Order cancelled.")
            confirmed = True
        else:
            utils.print_error("Order not cancelled.")

    def edit_order():
        print("Editing order...")
        print()
        user_order.get_order()
        utils.print_success("Order updated!")
        print()
        print_all()

    def edit_details():
        print("Editing details...")
        print()
        user_details.get_details(delivery)
        utils.print_success("Details updated!")
        print()
        print_all()
    
    def edit_pickup_method():
        nonlocal delivery

        print("Editing pickup method...")
        print()
        delivery = get_pickup_method()
        if delivery and not user_details.address:
            user_details.address = user_details.get_valid_input(
                "Enter your address: ", validator.validate_address)

        utils.print_success("Pickup method updated!")
        print()
        print_all()

    def help():
        commands_table.print(commands)

    def print_all():
        table_height = user_order.print_order()
        user_details.table.x_offset = 60
        user_details.table.y_offset = table_height
        user_details.print_details()
        if delivery:
            print("Pickup method:  " + Style.BRIGHT + "Delivery")
        else:
            print("Pickup method:  " + Style.BRIGHT + "Pickup")

        total = user_order.calculate_cost() + (14 if delivery else 0)
        print("Total cost:  " + Style.BRIGHT + f"${total:.2f}")

        print()
        print("If everything looks good, please confirm your order by entering 'confirm'.")

    commands_table = utils.Table(
        headers=["Avaliable commands", ""],
        widths=[20, 30],
        keys=["command", "description"],
    )

    commands = [
        {"command": "'confirm' or 'c':", "description": "Confirm the order"},
        {"command": "'abort' or 'a':", "description": "Abort/cancel the order"},
        {"command": "'order' or 'o':", "description": "Edit the order"},
        {"command": "'details' or 'd':", "description": "Edit my details"},
        {"command": "'method' or 'm':", "description": "Change pickup method"},
        {"command": "'view' or 'v':", "description": "View order details again"},
    ]

    command_map = {
        ("abort", "a"): abort,
        ("confirm", "c"): confirm_order,
        ("order", "o"): edit_order,
        ("details", "d"): edit_details,
        ("method", "m"): edit_pickup_method,
        ("view", "v"): print_all,
    }

    utils.print_title("CONFIRMATION")
    print("Just before we send your order, please check that all your details and order are correct.")
    print_all()

    while not confirmed:
        print()
        print("Type in a command for any action you want to take.")
        help()

        user_input = input("Enter command: ").lower()
        for key, command in command_map.items():
            if user_input in key:
                command()
                break
        else:
            utils.print_error("Invalid command. Please try again.")


def main():
    welcome()

    # Getting user order
    # Creates order class
    # Then asks user for their order
    user_order = Order()
    user_order.get_order()


    # Single line separator before moving to next section
    print()

    # Getting pickup method by calling the function
    is_delivery = get_pickup_method()

    # Single line separator before moving to next section
    print()
    
    # Getting user details
    # Creates details class
    # Then asks user for their details
    # If delivery is selected, asks for address
    user_details = Details()
    user_details.get_details(is_delivery)

    # Single line separator before moving to next section
    print()

    # Confirmation
    # Calls the confirmation function
    # Passes the order and details to the function
    confirm(user_order, user_details, is_delivery)

    print()
    program_end()


main()
