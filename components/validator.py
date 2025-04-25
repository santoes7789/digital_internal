# Checks if a given value is an integer
def validate_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_name(name):
    if not name.isalpha():
        return False
    return True