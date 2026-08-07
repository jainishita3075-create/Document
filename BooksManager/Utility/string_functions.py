def is_string(value) -> bool:
    """
    Checks whether the given value is a string.
    
    Example:
        >>> is_string("Hello")
        True
    """
    return isinstance(value, str)

def is_string_only(value) -> bool:
    """
    Checks whether a value is a string containing alphabetic characters only.
    
    Example:
        >>> is_string_only("Alphabet")
        True
    """
    if not isinstance(value, str):
        return False
    cleaned = value.replace(" ", "")
    return len(cleaned) > 0 and cleaned.isalpha()

def str_int(value: str) -> int:
    """
    Converts a string value into an integer.
    
    Example:
        >>> str_int("25")
        25
    """
    try:
        return int(value)
    except:
        raise ValueError("Value should be an Integer")

def str_float(value: str) -> float:
    """
    Converts a string value into a float.
    
    Example:
        >>> str_float("25.5")
        25.5
    """
    try:
        return float(value)
    except:
        raise ValueError("Value should be in Decimals")

def str_bool(value: str) -> bool:
    """
    Converts a string value into a boolean.
    
    Example:
        >>> str_bool("yes")
        True
    """
    value = value.strip().lower()
    if value in ('1','yes','true'):
        return True
    if value in ('0','no','false'):
        return False
    raise ValueError("Value must be True or False")