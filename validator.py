import re
from colorama import Fore

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

    print(Fore.RED + "Invalid name. A valid name should not include numbers or special characters.")
    return False


def validate_phone(phone):
    pattern = r"\d{8,10}"

    if re.fullmatch(pattern, phone):
        return True

    print(Fore.RED + "Invalid phone number. A phone number should consist of 8-10 digits.")
    return False


def validate_address(address):
    # Allow only letters, numbers, spaces, and common address symbols
    allowed_chars = r"[a-zA-Z0-9\s.,#-]+"

    # Check if the address is empty or contains only allowed characters
    if address.strip() and re.fullmatch(allowed_chars, address):
        return True

    print(Fore.RED + "Invalid address. Please input a valid address.")
    return False
