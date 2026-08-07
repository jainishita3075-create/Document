import json
import os
import shutil
from Utility.loggers import get_logger
from rich.console import Console
from rich.table import Table

# Initialize the logger for this specific file
logger = get_logger(__name__)
# Initialize the rich console for drawing tables
console = Console()

def load_books(filename="MOCK_DATA.json"):
    """
    Loads books from the JSON file safely.
    
    Example:
        >>> books = load_books("MOCK_DATA.json")
        >>> print(len(books))
        1000
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            books = json.load(file)
            logger.info(f"Successfully loaded {len(books)} books from {filename}.")
            return books
    except FileNotFoundError:
        logger.warning(f"File {filename} not found. Returning empty list.")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON decoding error in {filename}: {e}")
        print("Error: The data file is corrupted. Please check the logs.")
        return []


def _save_books(filename, books):
    """
    INTERNAL HELPER: Saves books to the JSON file and creates a backup first.
    
    Example:
        >>> my_books = [{"isbn": "123", "book_title": "Test Book"}]
        >>> _save_books("MOCK_DATA.json", my_books)
        True
    """
    if os.path.exists(filename):
        backup_name = f"{filename}.bak"
        shutil.copy(filename, backup_name)
        logger.info(f"Backup created at {backup_name}.")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)
        logger.info(f"Successfully saved {len(books)} books to {filename}.")
        return True
    except Exception as e:
        logger.critical(f"Critical error saving file {filename}: {e}")
        print(f"Error saving file. A backup is available at {filename}.bak")
        return False


def _display_books_table(books, title="Books", page_size=20):
    """
    INTERNAL HELPER: Draws a rich table to display books and handles pagination.
    
    Example:
        >>> my_books = [{"isbn": "123", "book_title": "Test Book", "price": 10.0}]
        >>> _display_books_table(my_books, title="My Books", page_size=5)
        # Outputs a formatted, colorful table to the terminal
    """
    total_books = len(books)
    if total_books == 0:
        print(f"No books found for: {title}")
        return

    # Loop through the books in chunks (pages)
    for i in range(0, total_books, page_size):
        chunk = books[i:i + page_size]
        
        # Create a new table for the current page
        table = Table(
            title=f"{title} (Showing {i + 1} to {min(i + page_size, total_books)} of {total_books})", 
            show_header=True, 
            header_style="bold magenta"
        )
        
        # Define the columns
        table.add_column("S.No", style="dim", width=5)
        table.add_column("Title", style="cyan")
        table.add_column("Author", style="green")
        table.add_column("Genre", style="blue")
        table.add_column("Price", justify="right", style="yellow")
        table.add_column("Qty", justify="right")
        table.add_column("ISBN", style="dim")

        # Add a row for each book in the current chunk
        for idx, book in enumerate(chunk, i + 1):
            table.add_row(
                str(idx),
                str(book.get("book_title", "N/A"))[:30],
                str(book.get("author", "N/A"))[:20],
                str(book.get("genre", "N/A"))[:15],
                f"${book.get('price', 0.0)}",
                str(book.get("quantity", 0)),
                str(book.get("isbn", "N/A"))
            )
            
        # Print the table to the terminal
        console.print(table)
        
        # Ask the user if they want to continue to the next page
        if i + page_size < total_books:
            cont = input("\nPress Enter to see the next page, or type 'q' to quit viewing: ")
            if cont.strip().lower() == 'q':
                break


def view_books(filename="MOCK_DATA.json"):
    """
    Displays all books stored in the JSON file in a paginated table.
    
    Example:
        >>> view_books("MOCK_DATA.json")
        # Opens an interactive, paginated table of all books
    """
    books = load_books(filename)
    _display_books_table(books, title="All Library Books")


def search_books(filename, query):
    """
    Searches for a book by partial title or author match (case-insensitive).
    
    Example:
        >>> results = search_books("MOCK_DATA.json", "potter")
        # Draws a table showing all matching records and returns them
    """
    books = load_books(filename)
    query = query.lower().strip()
    
    results = [
        book for book in books 
        if query in book.get("book_title", "").lower() 
        or query in book.get("author", "").lower()
    ]
    
    _display_books_table(results, title=f"Search Results for '{query}'")
    return results


def filter_books(filename, key, value):
    """
    Filters books by an exact match on a specific key (e.g., genre).
    
    Example:
        >>> results = filter_books("MOCK_DATA.json", "genre", "mystery")
        # Draws a table showing exclusively mystery books
    """
    books = load_books(filename)
    value = value.lower().strip()
    
    results = [
        book for book in books 
        if book.get(key, "").lower() == value
    ]
    
    _display_books_table(results, title=f"Filtered by {key.capitalize()}: '{value}'")
    return results


def filter_by_range(filename, key, min_val, max_val):
    """
    Filters books by a numeric range (e.g., price or quantity).
    
    Example:
        >>> results = filter_by_range("MOCK_DATA.json", "price", 10.0, 20.0)
        # Draws a table of books priced between $10 and $20
    """
    books = load_books(filename)
    
    results = [
        book for book in books 
        if isinstance(book.get(key), (int, float)) and min_val <= book.get(key) <= max_val
    ]
    
    _display_books_table(results, title=f"Filtered {key.capitalize()} between {min_val} and {max_val}")
    return results


def add_book(filename, book):
    """
    Adds a new book to the JSON file if the ISBN is unique.
    
    Example:
        >>> new_book = {"isbn": "999-9", "book_title": "New Book"}
        >>> add_book("MOCK_DATA.json", new_book)
        Book added successfully.
        True
    """
    books = load_books(filename)

    for existing_book in books:
        if existing_book.get("isbn") == book.get("isbn"):
            logger.warning(f"Attempted to add duplicate ISBN: {book.get('isbn')}")
            print("Book with this ISBN already exists.")
            return False

    books.append(book)
    if _save_books(filename, books):
        logger.info(f"Book added successfully: ISBN {book.get('isbn')}")
        print("Book added successfully.")
        return True
    return False


def update_book(filename, isbn, updated_data):
    """
    Updates a book using its ISBN.
    
    Example:
        >>> update_book("MOCK_DATA.json", "663052159-5", {"price": 15.99})
        Book updated successfully.
        True
    """
    books = load_books(filename)

    for book in books:
        if book.get("isbn") == isbn:
            book.update(updated_data)
            if _save_books(filename, books):
                logger.info(f"Book updated successfully: ISBN {isbn}")
                print("Book updated successfully.")
                return True

    logger.warning(f"Update failed. Book not found: ISBN {isbn}")
    print("Book not found.")
    return False


def delete_book(filename, isbn):
    """
    Deletes a book using its ISBN.
    
    Example:
        >>> delete_book("MOCK_DATA.json", "663052159-5")
        Book deleted successfully.
        True
    """
    books = load_books(filename)

    for book in books:
        if book.get("isbn") == isbn:
            books.remove(book)
            if _save_books(filename, books):
                logger.info(f"Book deleted successfully: ISBN {isbn}")
                print("Book deleted successfully.")
                return True

    logger.warning(f"Deletion failed. Book not found: ISBN {isbn}")
    print("Book not found.")
    return False

def load_users(filename="USERS.json"):
    """Loads users from the JSON file safely."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logger.warning(f"File {filename} not found. Returning empty list.")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON decoding error in {filename}: {e}")
        return []

def _save_users(filename, users):
    """INTERNAL HELPER: Saves users to the JSON file."""
    if os.path.exists(filename):
        shutil.copy(filename, f"{filename}.bak")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        return True
    except Exception as e:
        logger.critical(f"Critical error saving users: {e}")
        return False