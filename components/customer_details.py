import validator
pickup_method = "delivery"

customer_details = {}

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input

customer_details["name"] = get_valid_input("Enter your name: ", validator.validate_name)
customer_details["phone"] = get_valid_input("Enter your phone number: ", validator.validate_phone)  
if pickup_method == "delivery":
    customer_details["address"] = get_valid_input("Enter your address: ", validator.validate_address)

print("Customer Details:")  
print(customer_details)