import re
from datetime import datetime

def is_not_empty(value) -> bool:
    """
    Checks whether a value is not empty.
    
    Example:
        >>> is_not_empty("   ")
        False
        >>> is_not_empty("Hello")
        True
    """
    if value is None:
        return False
    if isinstance(value, str):
        return len(value.strip()) > 0
    if isinstance(value, (list, dict, set, tuple)):
        return len(value) > 0
    return True


def is_valid_email(email: str) -> bool:
    """
    Performs validation of an email address, ensuring it has a standard structure
    and uses a recognized domain extension to prevent typos.
    
    Example:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("we@jq.cod")
        False
    """
    if not isinstance(email, str):
        return False
        
    email = email.strip()
    
    # 1. Structural check using Regular Expressions (Regex)
    # This ensures there are no invalid characters and the @ and . are in the right places
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        return False
        
    # 2. Extract the extension (Top-Level Domain) for strict checking
    domain_part = email.split('@')[1]
    extension = domain_part.split('.')[-1].lower()
    
    # 3. Restrict to a list of common valid extensions to catch typos like '.cod'
    valid_extensions = {
        'com', 'org', 'net', 'edu', 'gov', 
        'co', 'io', 'info', 'biz', 'uk', 
        'in', 'us', 'ca', 'au'
    }
    
    if extension not in valid_extensions:
        return False
        
    return True


def valid_date_Time(date: str) -> bool:
    """
    Checks whether a value represents a valid YYYY-MM-DD HH:MM:SS date-time.
    
    Example:
        >>> valid_date_Time("2026-08-06 22:44:47")
        True
    """
    if not isinstance(date, str):
        return False
    try:
        datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

def valid_username(name: str) -> bool:
    """
    Validates username against minimum requirements.
    
    Example:
        >>> valid_username("Alice123")
        True
    """
    if not name or not isinstance(name, str):
        return False
    if len(name) < 8:
        return False
    if sum(char.isalpha() for char in name) < 5:
        return False
    if sum(char.isdigit() for char in name) < 2:
        return False
    return True

def valid_password(pas: str) -> bool:
    """
    Validates password against minimum requirements.
    
    Example:
        >>> valid_password("Secret99")
        True
    """
    if not pas or not isinstance(pas, str):
        return False
    if len(pas) < 8:
        return False
    if sum(char.isalpha() for char in pas) < 5 or sum(char.isdigit() for char in pas) < 2:
        return False
    return True

def valid_string_only(value: str) -> bool:
    """
    Checks whether a string contains only alphabetic characters and spaces.
    
    Example:
        >>> valid_string_only("John Doe")
        True
    """
    if not isinstance(value, str):
        return False
    cleaned = value.replace(" ", "")
    return len(cleaned) > 0 and cleaned.isalpha()

def prompt_string_only(prompt_msg: str) -> str:
    """
    Prompts user until a string-only (letters and spaces) input is provided.
    
    Example:
        >>> name = prompt_string_only("Enter name: ")
        # Returns 'John Doe'
    """
    while True:
        val = input(prompt_msg).strip()
        if valid_string_only(val):
            return val
        print("Error: Input must contain letters only (no digits or special characters). Please re-enter.")

def prompt_non_empty_string(prompt_msg: str) -> str:
    """
    Prompts user until a non-empty string is provided. Purely numeric
    input is allowed, since real values (book titles like "1984",
    search queries, etc.) can legitimately consist only of digits.
    
    Example:
        >>> text = prompt_non_empty_string("Enter value: ")
        # Returns 'Valid String'
        >>> title = prompt_non_empty_string("Enter book title: ")
        # Also accepts "1984"
    """
    while True:
        val = input(prompt_msg).strip()
        if val:
            return val
        print("Error: Field cannot be empty. Please re-enter.")

def prompt_isbn(prompt_msg: str) -> str:
    """
    Prompts user until a valid ISBN (no spaces, non-empty) is provided.
    
    Example:
        >>> isbn = prompt_isbn("Enter ISBN: ")
        # Returns '663052159-5'
    """
    while True:
        val = input(prompt_msg).strip()
        if not val:
            print("Error: Field cannot be empty. Please re-enter.")
        elif " " in val:
            print("Error: ISBN cannot contain spaces. Please re-enter.")
        else:
            return val

def prompt_date(prompt_msg: str) -> str:
    """
    Prompts user until a valid date (YYYY-MM-DD) is provided.
    Enforces strict 10-character length to prevent single-digit padding issues.
    
    Example:
        >>> date = prompt_date("Enter date: ")
        # Returns '2026-12-31'
    """
    while True:
        val = input(prompt_msg).strip()
        try:
            # Check if it actually parses as a valid date
            datetime.strptime(val, "%Y-%m-%d")
            # Enforce strict length so inputs like 0099-9-9 are rejected
            if len(val) != 10:
                raise ValueError
            return val
        except ValueError:
            print("Error: Invalid date format. Expected exactly YYYY-MM-DD (e.g., 2026-08-06). Please re-enter.")