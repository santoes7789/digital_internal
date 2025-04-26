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
    if name.isspace() or not re.fullmatch(allowed_chars, name):
        return False

    return True 

def validate_phone(phone):
    pattern = r"\d{8,10}"

    if phone.isspace() or not re.fullmatch(pattern, phone):
        return False

    return True