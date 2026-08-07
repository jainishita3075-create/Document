def is_integer(value) -> bool:
    """
    Checks whether the given value is an integer.
    
    Example:
        >>> is_integer(10)
        True
        >>> is_integer(10.5)
        False
    """
    return isinstance(value, int) and not isinstance(value, bool)

def is_float(value) -> bool:
    """
    Checks whether the given value is a float.
    
    Example:
        >>> is_float(10.5)
        True
        >>> is_float(10)
        False
    """
    return isinstance(value, float)

def valid_age(value) -> bool:
    """
    Checks whether a value is a valid age integer (0 to 100).
    
    Example:
        >>> valid_age(25)
        True
    """
    if type(value) is not int:
        return False
    return 0 <= value <= 100

def valid_number(value) -> bool:
    """
    Checks whether a value is a valid 10-digit integer.
    
    Example:
        >>> valid_number(1234567890)
        True
    """
    if not isinstance(value, int):
        return False
    return 1000000000 <= value <= 9999999999

def is_inrange(value, minimum, maximum) -> bool:
    """
    Checks whether a numeric value falls within the given range.
    
    Example:
        >>> is_inrange(50, 1, 100)
        True
    """
    if not isinstance(value, (int, float)):
        return False
    return minimum <= value <= maximum

def valid_percentage(value) -> bool:
    """
    Checks if a value is a valid percentage (0-100).
    
    Example:
        >>> valid_percentage(85.5)
        True
    """
    return is_inrange(value, 0, 100)

def prompt_float(prompt_msg: str, min_val: float = 0.0) -> float:
    """
    Prompts user until a valid floating-point number is provided.
    
    Example:
        >>> price = prompt_float("Enter Price: ", min_val=10.0)
        # Returns 15.5
    """
    while True:
        val = input(prompt_msg).strip()
        try:
            num = float(val)
            if num >= min_val:
                return num
            print(f"Error: Price/Number must be greater than or equal to {min_val}. Please re-enter.")
        except ValueError:
            print("Error: Input must be a valid numeric/decimal value. Please re-enter.")

def prompt_int(prompt_msg: str, min_val: int = 0) -> int:
    """
    Prompts user until a valid integer is provided.
    
    Example:
        >>> qty = prompt_int("Enter Quantity: ", min_val=1)
        # Returns 5
    """
    while True:
        val = input(prompt_msg).strip()
        try:
            num = int(val)
            if num >= min_val:
                return num
            print(f"Error: Quantity/Number must be an integer >= {min_val}. Please re-enter.")
        except ValueError:
            print("Error: Input must be a valid whole integer. Please re-enter.")