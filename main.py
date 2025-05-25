# Random library is used to randomly select a bot name
import random

# Colorama library is used to add color and styling to the console output
from colorama import Style

# Importing custom modules for utility functions and validation
import utils
import validator

# Constant for delivery cost
DELIVERY_COST = 14

# Constant for free delivery threshold - if order total is above this, delivery is free
FREE_DELIVERY_THRESHOLD = 50


# DESIGN CONSTANTS:
# Widths for the menu table columns
MENU_COLUMN_WIDTHS = [23, 9]
# Widths for commnad table columns
COMMAND_COLUMN_WIDTHS = [20, 30]
#  Widhts for customer details table columns
CUSTOMER_DETAILS_COLUMN_WIDTHS = [10, 30]
# Indents for table
TABLE_INDENT = 2
# Table spacing, between two tables
TABLE_SPACING = 6



# Bot names for the ordering system
bot_names = ["Alice", "Bob", "Charlie", "Daisy",
             "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Menu information stored in one array
pies = [
    {"name": "Apple Pie", "price": 7.99},
    {"name": "Pumpkin Pie", "price": 6.99},
    {"name": "Cherry Pie", "price": 8.49},
    {"name": "Pecan Pie", "price": 8.99},
    {"name": "Blueberry Pie", "price": 8.29},
    {"name": "Key Lime Pie", "price": 7.49},
    {"name": "Lemon Meringue Pie", "price": 7.29},
    {"name": "Sweet Potato Pie", "price": 6.79},
    {"name": "Chocolate Cream Pie", "price": 8.19},
    {"name": "Butter Chicken Pie", "price": 7.99},
    {"name": "Banana Cream Pie", "price": 7.89},
    {"name": "Strawberry Rhubarb Pie", "price": 8.59},
    {"name": "Meat Pie", "price": 9.49},
    {"name": "Chicken Pot Pie", "price": 9.29},
    {"name": "Shepherd’s Pie", "price": 8.99}
]



# Prints a welcome message with a random bot name
# Also awaits for enter
def welcome():
    # Randomly select a bot name from the list
    bot_name = random.choice(bot_names)

    # Set the width of the banner
    banner_width = 50

    # Prints the welcome message
    # Uses utils.print functions to print with preset styles
    # Prints ===== with length of banner width
    utils.print_title("=" * banner_width)

    # Prints welcome message, centered with title style (bolded)
    message = f"Welcome to the best pie shop, my name is {bot_name}"
    utils.print_title(message.center(banner_width))

    print()

    # Prints "Press enter to start!" centered, with header style (blue)
    utils.print_header("PRESS ENTER TO START ORDERING!".center(banner_width))
    utils.print_title("=" * banner_width)

    input()  # Waits for user to press enter before continuing

# Prints a message asking if the user wants to make a new order
# If yes, it restarts the program
# If no, it exits the program
def program_end():
    # Prompts user
    print("Would you like to make a new order?")

    # Gets user confirmation
    if utils.confirm_prompt("Type 'yes' or 'y' to make a new order, anything else to exit: "):
        main()
    else:
        print("Goodbye!")

    # Terminates the program
    exit()

# Order class for ordering
class Order():

    # possible commands for order system, to be printed
    commands = [
        {"command": "'menu' or 'm':", "description": "Show the menu"},
        {"command": "'done' or 'd':", "description": "Finish ordering"},
        {"command": "'clear' or 'c':", "description": "Clear your order"},
        {"command": "'show' or 's':", "description": "Show your current order"},
        {"command": "'remove' or 'r':", "description": "Remove a pie from your order"},
        {"command": "'exit' or 'e':", "description": "Exit the ordering system"},
        {"command": "'help' or 'h':", "description": "Show this help message"}
    ]

    # creating table from commands to be printed
    command_table = utils.Table(
        headers=["Available commands:", ""],
        widths=COMMAND_COLUMN_WIDTHS,
        keys=["command", "description"],
        x_offset=TABLE_INDENT)

    def __init__(self):
        # init empty array
        self.order = []

        # set ordering to not done
        self.done = False

        # create table template for order and menu to be printed from
        self.table = utils.Table(
            headers=["Pie Name", "Price ($)"],
            widths=MENU_COLUMN_WIDTHS,
            keys=["name", "price"],
            alignments=["<", ">"],
            formats=["", ".2f"],
            index=True,
            x_offset=TABLE_INDENT
        )

    # Calculates cost based on order
    def calculate_cost(self):
        total_cost = 0
        # Iterate through each pie to get the price
        for pie in self.order:
            # Add the price of the pie to the total cost
            total_cost += pie['price']

        # Returns total cost
        return total_cost

    # Finish ordering
    def finish(self):
        # Check if order is empty or not
        if not self.order:
            # If order is empty, print error message and return
            utils.print_error(
                "Your order is empty. Please order before finishing.")
            return

        # If order is not empty, print success message
        self.print_order()
        print()

        # Ask for confirmation before finishing the order
        if utils.confirm_prompt("Are you sure you want to finish ordering? (type 'yes' or 'y' to confirm, anything else to cancel): "):
            utils.print_success("You have finished ordering!")
            self.done = True
        else:
            # If confirmation is anything else, print error message and return
            utils.print_error("Order confirmation has been cancelled.")

    # Prints pie menu
    def print_menu(self):
        utils.print_header("MENU:")
        return self.table.print(pies)

    # Exits the program, asks for confirmation before
    def exit(self):
        # If order is not empty, ask for confirmation before exiting
        if self.order:
            # If confirmation is not yes or y, exit the program
            if not utils.confirm_prompt("Are you sure you want to exit? All items in order will be cleared. (type 'yes' or 'y' to confirm, anything else to cancel): "):
                utils.print_error("Exit cancelled. Returning to ordering system.")
                return

        utils.print_success("Exiting the ordering system.")
        print()
        program_end()

    # Clears order asks for confirmation before doing so
    def clear_order(self):
        # If order is empty, print error message and return
        if not self.order:
            utils.print_error("Your order is empty. Nothing to clear.")
            return

        if utils.confirm_prompt("Are you sure you want to clear your order? (type 'yes' or 'y' to confirm, anything else to cancel): "):
            self.order.clear()
            utils.print_success("Your order has been cleared.")
        else:
            utils.print_error("Order has been not been cleared.")

    # Shows current order
    def print_order(self):
        # If order is empty, print error message and return
        if not self.order:
            utils.print_error("Your order is empty.")
            return

        # Otherwise print order, adding total cost at the end.
        utils.print_header("Your current order:")
        table = self.order.copy()

        # Add a single line separator
        table.append(utils.Table.RowType.SINGLE_LINE)

        # Add total cost to the order list
        table.append({"index": "", "name": "Order Cost",
                     "price": self.calculate_cost()})
        return self.table.print(table)

    # Removes pie from order
    def remove_pie(self):
        # If order is empty, print error message and return
        if not self.order:
            utils.print_error("Your order is empty. Nothing to remove.")
            return

        # Prints out current order
        utils.print_header("Your current order:")
        self.table.print(self.order)

        # Ask user for index of pie to remove
        remove_index = input(
            "Enter the index of the pie you want to remove: ").strip()

        # Checks if input is an integer
        if not validator.validate_int(remove_index):
            utils.print_error("Invalid input. No item removed.")
            return

        # Convert to 0-based index
        remove_index = int(remove_index) - 1

        # Remove pie from order
        if 0 <= remove_index < len(self.order):
            # remove pie from order
            removed_pie = self.order.pop(remove_index)
            # print success message
            utils.print_success(
                f"Removed {removed_pie['name']} from your order.")
        else:
            # If index is out of range, print error message, and do not remove anything
            utils.print_error("Invalid index. No item removed.")

    # Shows help message with available commands
    def show_help(self):
        self.command_table.print(self.commands)

    # Prints the starting prompt for the ordering system
    def starting_prompt(self):
        utils.print_title("ORDERING SYSTEM")  # Prints title
        print("You can order pies from our menu below.")
        print("To order a pie, please enter the index number of the pie you want.")
        print("Delivery cost is free for orders over $50.")
        print()
        print("You can also type in commands for more options.")
        print()

        # Prints menu
        table_width, table_height = self.print_menu()

        # Offset the command table to put it on the right of the menu
        # x_offset is set to table width + TABLE_INDENT + TABLE_SPACING
        # This will put it next to the menu, with gap of TABLE_SPACING

        # y_offset is set to table height so it is right next to the menu
        self.command_table.set_offset(table_width + TABLE_INDENT + TABLE_SPACING, table_height)

        # Print the command table
        self.show_help()

        # Reset the offsets to 0 for the next print
        self.command_table.set_offset(TABLE_INDENT, 0)

    # starts ordering system
    def get_order(self):
        # prints out starting prompt
        self.starting_prompt()

        # sets done to false, so loop will run
        self.done = False

        # Keeps asking for prompts until user is done
        while not self.done:
            # Get user input
            print()
            user_input = input(
                "Please enter the index of the pie you want to order (or 'done' to finish): ")

            # lowercase the input for case insensitive matching
            user_input = user_input.strip().lower()

            # Command map for commands to functions
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
                    utils.print_error(
                        "Invalid input. Please enter a valid index or a command.")

                # Add pie based on index
                else:
                    # Convert to 0-based index
                    order = int(user_input) - 1

                    # Check if index is within range
                    if 0 <= order < len(pies):
                        # If index is valid, add pie to order
                        utils.print_success(
                            f"You have ordered {pies[order]['name']} for ${pies[order]['price']:.2f}.")
                        self.order.append(pies[order])
                    else:
                        # If index is out of range, print error message
                        utils.print_error(
                            "Invalid index. Please enter a valid index from the menu.")


# Gets pickup method
def get_pickup_method():
    utils.print_title("PICKUP METHOD")

    # Keep asking question until loop is broken - valid input is accepted
    while True:
        print("Would you like to pick up your order or have it delivered?")
        print("Delivery costs an additional $14, but is free for orders over $50.")
        print("Input 'pickup' or 'p' for Pick up")
        print("Input 'delivery' or 'd' for Delivery " +
              Style.BRIGHT + "(+$14)")

        # Prompt user for input, case insensitive
        choice = input("Enter your choice: ").strip().lower()

        # Find the user's choice, finding the first match in the list of options
        if choice in ("pickup", "pick up", "pick", "p"):
            # If choice is pickup, print success message and return False
            utils.print_success("You have chosen to pick up your order.")
            return False

        elif choice in ("delivery", "deliver", "d"):
            # If choice is delivery, print success message and return True
            utils.print_success(
                "You have chosen to have your order delivered.")
            return True

        else:
            # If choice is invalid, print error message and ask again
            utils.print_error(
                "Invalid choice. Please enter 'pickup' for Pick up, or 'delivery' for Delivery.")


# Class for getting user details
class Details():
    def __init__(self, delivery):
        # Initialize user details
        self.name = None
        self.phone = None
        self.address = None
        self.suburb = None

        self.delivery = delivery

        # Create a table template for customer details
        self.table = utils.Table(
            headers=["Your Details:", ""],
            widths=CUSTOMER_DETAILS_COLUMN_WIDTHS,
            keys=["Field", "Value"],
            x_offset=TABLE_INDENT
        )

    # Function for asking questions, takes in prompt and validator function
    def get_valid_input(self, prompt, validation_func):
        # Asks question until validator function returns true
        while True:
            user_input = input(prompt).strip()
            if validation_func(user_input):
                return user_input

    # Prints customer details in a table format, returns the height of the table
    def print_details(self):
        # Create table data, adding name and phone
        table_data = []
        table_data.append({"Field": "Name:", "Value": self.name})
        table_data.append({"Field": "Phone:", "Value": self.phone})

        # Only add address if address if not falsey
        if self.delivery:
            table_data.append({"Field": "Address:", "Value": self.address})
            table_data.append({"Field": "Suburb:", "Value": self.suburb})

        # print the table with customer details
        return self.table.print(table_data)

    # Main starting function for getting details.
    # Gets address if delivery is true
    def get_details(self):
        utils.print_title("CUSTOMER DETAILS")

        # Get name
        self.name = self.get_valid_input(
            "Enter your name: ", validator.validate_name)

        # Get phone
        self.phone = self.get_valid_input(
            "Enter your phone number: ", validator.validate_phone)

        # Get address (and suburb) if delivery is true
        if self.delivery:
            self.address = self.get_valid_input(
                "Enter your address (format: [House number] [Street Name]): ", validator.validate_address)
            self.suburb = self.get_valid_input(
                "Enter your suburb: ", validator.validate_name)

        utils.print_success("Your information has been saved!")


def confirm(user_order, user_details):

    # asks user for confirmation before continuing
    # returns boolean whether confirmed or not
    def confirm_order():
        # If confirmation is yes or y, print success message and return True
        if utils.confirm_prompt("Are you sure you want to confirm your order? (type 'yes' or 'y' to confirm, anything else to cancel): "):
            utils.print_success("Your order has been confirmed!")
            utils.print_success("Thank you for ordering with us!")
            # Print different things depending on whether delivery is selected or not
            if user_details.delivery:
                print()
                utils.print_success("Your order will be delivered to " +
                                    user_details.address + " soon.")
                utils.print_success(
                    "You will receive a text message regarding delivery status.")
            else:
                print()
                utils.print_success(
                    "Your order will be ready for pickup soon.")
                utils.print_success(
                    "You will receive a text message when it is ready.")
            return True

        # If confirmation is anything else, print error message and return nothing
        utils.print_error("Order confirmation has been cancelled.")

    # aborts program
    def abort():
        if utils.confirm_prompt("Are you sure you want to cancel your order? (type 'yes' or 'y' to confirm, anything else to cancel): "):
            utils.print_success("Order cancelled.")
            return True
        else:
            utils.print_error("Order not cancelled.")

    # sends user back to ordering system
    def edit_order():
        print("Editing order...")
        print()
        user_order.get_order()
        utils.print_success("Order updated!")
        print()
        print_all()

    # sends user back to editing details
    def edit_details():
        print("Editing details...")
        print()
        user_details.get_details()
        utils.print_success("Details updated!")
        print()
        print_all()

    # sends user back to changing pickup method
    # if changes from pickup to delivery, ask for address
    def edit_pickup_method():

        print("Editing pickup method...")
        print()
        user_details.delivery = get_pickup_method()

        # If option is changed to delivery and there is no address, get the address
        if user_details.delivery and not user_details.address:
            user_details.address = user_details.get_valid_input(
                "Enter your address (format: [House number] [Street Name]): ", validator.validate_address)
            user_details.suburb = user_details.get_valid_input(
                "Enter your suburb: ", validator.validate_name)

        utils.print_success("Pickup method updated!")
        print()
        print_all()

    def show_help():
        commands_table.print(commands)

    # Prints all details, order, details and pickup method
    def print_all():
        # print order
        table_width, table_height = user_order.print_order()

        # print details next to table, same as before
        user_details.table.set_offset(table_width + TABLE_INDENT + TABLE_SPACING, table_height)
        user_details.print_details()

        # if delivery, print delivery, if not print pickup
        if user_details.delivery:
            print("Pickup method:  " + Style.BRIGHT + "Delivery")
        else:
            print("Pickup method:  " + Style.BRIGHT + "Pickup")

        # calculate total cost
        # if delivery, add an additional $14
        total = user_order.calculate_cost()

        # If delivery is selected, add delivery cost, if total is less than $50
        if user_details.delivery and total <= FREE_DELIVERY_THRESHOLD:
            total += DELIVERY_COST

        print("Total cost:  " + Style.BRIGHT + f"${total:.2f}")

        print()
        print("If everything looks good, please confirm your order by entering 'confirm'.")

    # Create table from commands to be printed nicely
    commands_table = utils.Table(
        headers=["Avaliable commands", ""],
        widths=COMMAND_COLUMN_WIDTHS,
        keys=["command", "description"],
        x_offset= TABLE_INDENT
    )

    # Array of possible commands and their description
    commands = [
        {"command": "'confirm' or 'c':", "description": "Confirm the order"},
        {"command": "'abort' or 'a':", "description": "Abort/cancel the order"},
        {"command": "'order' or 'o':", "description": "Edit the order"},
        {"command": "'details' or 'd':", "description": "Edit my details"},
        {"command": "'method' or 'm':", "description": "Change pickup method"},
        {"command": "'view' or 'v':", "description": "View order details again"},
    ]

    # Dictionary of possible commands and their functions
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

    # Prints all details
    print_all()

    # Keeps asking question until order is confirmed or aborted
    while True:
        print()
        print("Type in a command for any action you want to take.")
        show_help()

        user_input = input("Enter command: ").strip().lower()
        # Iterates through the command map to find command
        for key, command in command_map.items():
            if user_input in key:
                # Execute that command's function
                if command():
                    return
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

    print()

    # Getting pickup method by calling the function
    is_delivery = get_pickup_method()

    print()

    # Getting user details
    # Creates details class
    # Then asks user for their details
    # If delivery is selected, asks for address
    user_details = Details(is_delivery)
    user_details.get_details()

    print()

    # Confirmation
    # Calls the confirmation function
    # Passes the order and details to the function
    confirm(user_order, user_details)

    print()
    program_end()


main()
