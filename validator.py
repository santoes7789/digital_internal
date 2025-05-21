import re
import utils

# Checks if a given value is an integer
def validate_int(value):
    # Tries to convert to integer, if fails value is not int
    try:
        int(value)
        return True
    except ValueError:
        return False

# Validates name
def validate_name(name):
    # Allow only letters, hyphens, spaces, and apostrophes
    allowed_chars = r"[a-zA-Z-' ]+"

    # Check if the name is empty or contains only allowed characters
    if name.strip() and re.fullmatch(allowed_chars, name):
        return True

    utils.print_error("Invalid name. A valid name should not include numbers or special characters.")
    return False

# Validates phone number
def validate_phone(phone):
    pattern = r"\d{8,10}"

    if re.fullmatch(pattern, phone):
        return True

    utils.print_error("Invalid phone number. A phone number should consist of 8-10 digits.")
    return False

# Validates address
def validate_address(address):
    # Allow only letters, numbers, spaces, and common address symbols
    allowed_chars = r"[a-zA-Z0-9\s.,#-]+"

    # Check if the address is empty or contains only allowed characters
    if address.strip() and re.fullmatch(allowed_chars, address):
        return True

    utils.print_error("Invalid address. Please input a valid address.")
    return False
