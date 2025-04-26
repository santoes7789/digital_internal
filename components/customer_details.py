import validator
pickup_method = "delivery"

customer_details = {}

while True:
    user_input = input("Enter your name: ")
    if validator.validate_name(user_input):
        customer_details["name"] = user_input
        break
    else:
        print("Invalid name. A valid name should not include numbers or special characters.")
        
while True:
    user_input = input("Enter your phone number: ")
    if validator.validate_phone(user_input):
        customer_details["phone"] = user_input
        break
    else:
        print("Invalid phone number. A phone number should consist of 8-10 digits.")

if pickup_method == "delivery":
    customer_details["address"] = input("Enter your address: ")

print("Customer Details:")  
print(customer_details)