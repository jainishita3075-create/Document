import math

def validate_integer(value):
    """
    Check whether the value is a valid integer.
    """

    try:
        int(value)
        return True

    except (ValueError, TypeError):
        return False

def validate_float(value):
    """
    Check whether the value is a valid finite float.
    """

    try:
        number = float(value)

        return math.isfinite(number)

    except (ValueError, TypeError):
        return False

def validate_number(value):
    """
    Check whether the value is a valid finite number.
    """

    try:
        number = float(value)

        return math.isfinite(number)

    except (ValueError, TypeError):
        return False

def validate_age(age):
    """
    Validate age between 0 and 100.
    """

    if not validate_integer(age):
        return False

    age = int(age)

    return 0 <= age <= 100

# def validate_percentage(value):
#     """
#     Validate percentage between 0 and 100.
#     """

#     if not validate_float(value):
#         return False

#     value = float(value)

#     return 0 <= value <= 100

# def validate_even_number(value):
#     """
#     Validate whether the number is even.
#     """

#     if not validate_integer(value):
#         return False

#     return int(value) % 2 == 0

def validate_positive_number(value):
    """
    Validate whether the number is positive.
    """

    if not validate_number(value):
        return False

    return float(value) > 0