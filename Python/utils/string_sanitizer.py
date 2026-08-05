import re       # regular expression, also used to remove extra spaces between the words, check mail and phone number
import unicodedata      # special character assigned to each word/letter so that we can write that unicode and the desired output will be given

def sanitize_string(value):
    """
    Basic string sanitization.

    - Converts value to string
    - Normalizes Unicode
    - Removes leading/trailing spaces
    - Replaces multiple spaces with one
    """

    if value is None:
        return ""

    value = str(value)

    # Unicode normalization
    value = unicodedata.normalize("NFKC", value)

    # Remove leading/trailing whitespace
    value = value.strip()

    # Replace multiple whitespace characters with one space
    value = re.sub(r"\s+", " ", value)

    return value


def remove_spaces(value):
    """
    Remove all whitespace from a string.
    """

    if value is None:
        return ""

    return re.sub(r"\s+", "", str(value))


def remove_special_characters(value, keep=""):
    """
    Remove special characters.

    Letters, numbers and spaces are kept.

    'keep' can be used to preserve specific symbols.

    Example:
        remove_special_characters("Ishita@123", keep="@")
    """

    if value is None:
        return ""

    value = str(value)

    result = ""

    for char in value:

        # .isalnum() ==> alphanumeric, .isspace() ==> used to check characters whitespaces 
        if char.isalnum() or char.isspace() or char in keep:
            result += char

    return result


def normalize_case(value, mode="lower"):
    """
    Normalize the case of a string.

    mode:
        lower
        upper
        title
    """

    if value is None:
        return ""

    value = str(value)

    if mode == "lower":
        return value.lower()

    if mode == "upper":
        return value.upper()

    if mode == "title":
        return value.title()        # .title() capitalize first letter of every word in a string

    # capitalize() is used to capitalize first character of every string

    raise ValueError("Invalid mode. Use lower, upper or title.")