import validator
pickup_method = "delivery"

customer_details = {}

while True:
    user_input = input("Enter your name: ")
    if validator.validate_name(user_input):
        customer_details["name"] = user_input
        break
    else:
        print("Invalid name. Please enter a valid name.")
        
customer_details["phone"] = input("Enter your phone number: ")
if pickup_method == "delivery":
    customer_details["address"] = input("Enter your address: ")

print("Customer Details:")  
print(customer_details)