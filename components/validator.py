import re

# Checks if a given value is an integer
def validate_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_name(name):
    # Allow only letters, hyphens, spaces, and apostrophes
    allowed_chars = r"[a-zA-Z-' ]+"

    # Check if the name is empty or contains only allowed characters
    if name.strip() and re.fullmatch(allowed_chars, name):
        return True 

    print("Invalid name. A valid name should not include numbers or special characters.")
    return False

def validate_phone(phone):
    pattern = r"\d{8,10}"

    if re.fullmatch(pattern, phone):
        return True

    print("Invalid phone number. A phone number should consist of 8-10 digits.")
    return False

def validate_address(address):

    address = address.strip()

    address_segments = address.split(" ")

    if len(address_segments) < 2:
        print("Invalid address. Please input an address in the form [House number] [Street name].")
        return False

    house_number = address_segments[0]
    street_name = " ".join(address_segments[1:])
    house_number_regex = r"\d+[a-zA-Z]*+"
    street_name_regex = r"[a-zA-Z-' .]+"

    if not re.fullmatch(house_number_regex, house_number):
        print("Invalid address. [House number] should consist of numbers and optional letters.")
        return False

    if not re.fullmatch(street_name_regex, street_name):
        print("Invalid address. [Street name] should consist of letters, spaces, and hyphens.")
        return False

    return True
