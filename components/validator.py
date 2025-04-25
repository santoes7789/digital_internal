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
    if re.fullmatch(allowed_chars, name):
        return True 
    return False 