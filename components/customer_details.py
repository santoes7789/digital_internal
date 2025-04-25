pickup_method = "delivery"

customer_details = {}
customer_details["name"] = input("Enter your name: ")
customer_details["phone"] = input("Enter your phone number: ")
if pickup_method == "delivery":
    customer_details["address"] = input("Enter your address: ")

print("Customer Details:")  
print(customer_details)