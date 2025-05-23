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

    utils.print_error(
        "Invalid name. A valid name should not include numbers or special characters.")
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

    address = address.strip()

    # Split the address into segments, the house number and the street name
    address_segments = address.split(" ")

    if len(address_segments) < 2:
        utils.print_error("Invalid address. Please input an address in the form [House number] [Street name].")
        return False

    # The first segment is the house number
    house_number = address_segments[0]
    # Regex, only allow numbers and optional letters
    house_number_regex = r"\d+[a-zA-Z]*+"

    # Join the remaining segments to form the street name
    street_name = " ".join(address_segments[1:])
    # Regex, only allow letters, spaces, hyphens, and apostrophes
    street_name_regex = r"[a-zA-Z-' .]+"

    # Check if the house number and street name match the regex patterns
    if not re.fullmatch(house_number_regex, house_number):
        utils.print_error("Invalid address. [House number] should consist of numbers and optional letters.")
        return False

    if not re.fullmatch(street_name_regex, street_name):
        utils.print_error("Invalid address. [Street name] should consist of letters, spaces, and hyphens.")
        return False

    return True