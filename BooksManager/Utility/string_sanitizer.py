def remove_spaces(s: str) -> str:
    """
    Removes extra spaces from a string.
    
    Example:
        >>> remove_spaces("  Hello    World  ")
        "Hello World"
    """
    return " ".join(s.split())

def normalize_case(s: str, mode: str) -> str:
    """
    Converts a string to the specified case.
    
    Example:
        >>> normalize_case("hello WORLD", "title")
        "Hello World"
    """
    if mode == "lower":
        return s.lower()
    if mode == "upper":
        return s.upper()
    if mode == "title":
        return s.title()
    raise ValueError(f"Unknown Mode: {mode}")

def remove_specialchar(s: str) -> str:
    """
    Removes special characters from a string.
    
    Example:
        >>> remove_specialchar("Hello@World! 123#")
        "HelloWorld 123"
    """
    return "".join(char for char in s if char.isalnum() or char.isspace())

def valid_filename(filen: str) -> bool:
    """
    Checks whether a filename has a valid basic format.
    
    Examples:
        >>> valid_filename("report.pdf")
        True
        >>> valid_filename("my.report.pdf")
        False
    """
    if not filen:
        return False
    if '.' not in filen:
        return False
    parts = filen.split('.')
    if len(parts) != 2:
        return False
    file, exten = parts
    if not file or not exten:
        return False
    return True