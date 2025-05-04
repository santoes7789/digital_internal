import validator
import menu

class CustomerDetails():
    def __init__(self):
        self.name = None
        self.phone = None
        self.address = None

        self.table = menu.Table(
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
        self.name = self.get_valid_input("Enter your name: ", validator.validate_name)
        self.phone = self.get_valid_input("Enter your phone number: ", validator.validate_phone)
        if delivery:
            self.address = self.get_valid_input("Enter your address: ", validator.validate_address)
