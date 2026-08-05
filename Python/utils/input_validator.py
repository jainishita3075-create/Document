# def validate_input(value, required=True):
#     """
#     Check whether input has been provided.

#     required=True:
#         None, empty string and whitespace-only strings are invalid.

#     required=False:
#         Empty values are allowed.
#     """

#     if value is None:
#         return not required

#     if isinstance(value, str):
#         if required and not value.strip():
#             return False

#     return True


def validate_type(value, expected_type):
    """
    Check whether the value has the expected data type.

    Example:
        validate_type("Ishita", str)
        validate_type(20, int)
    """

    return isinstance(value, expected_type)


def validate_length(value, min_length=None, max_length=None):
    """
    Validate the length of a value.

    Works with strings, lists, tuples, etc.
    """

    try:
        length = len(value)

    except TypeError:
        return False

    if min_length is not None and length < min_length:
        return False

    if max_length is not None and length > max_length:
        return False

    return True


def validate_required_fields(data, required_fields):
    """
    Check whether all required fields exist
    and contain valid values.

    Example:

        data = {
            "name": "Ishita",
            "email": "ishita@gmail.com"
        }

        required_fields = ["name", "email"]
    """

    if not isinstance(data, dict):
        return False

    for field in required_fields:

        # Check whether field exists
        if field not in data:
            return False

        # Check for None
        if data[field] is None:
            return False

        # Check for empty strings
        if isinstance(data[field], str) and not data[field].strip():
            return False

    return True