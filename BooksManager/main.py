import questionary
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from Utility.file_handler import (
    load_books,
    view_books,
    search_books,
    filter_books,
    filter_by_range,
    add_book,
    update_book,
    delete_book,
    _save_books,
    load_users,
    _save_users
)
from Utility.input_validator import (
    is_valid_email,
    valid_date_Time,
    valid_username,
    valid_password,
    prompt_string_only,
    prompt_non_empty_string,
    prompt_isbn,
    prompt_date
)
from Utility.numeric_validator import (
    valid_age,
    valid_number,
    prompt_float,
    prompt_int
)
from Utility.loggers import get_logger

# Initialize logger and rich console
logger = get_logger(__name__)
console = Console()

BOOKS_FILE = "MOCK_DATA.json"
USERS_FILE = "USERS.json"


# ==========================================
# 1. CUSTOMER PORTAL & AUTHENTICATION
# ==========================================

def generate_invoice(user: str, action: str, book: dict, price: float) -> dict:
    """
    Generates and displays a beautifully formatted receipt using the rich library.
    
    Example:
        >>> receipt = generate_invoice("Alice", "BUY", {"book_title": "1984", "isbn": "123", "author": "Orwell"}, 15.99)
        # Outputs a colorful receipt panel to the terminal and returns the receipt dictionary.
    """
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    invoice_id = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    receipt_content = (
        f"[bold]Invoice ID:[/bold] {invoice_id}\n"
        f"[bold]Date:[/bold] {date_now}\n"
        f"[bold]Customer:[/bold] {user}\n"
        f"----------------------------------------\n"
        f"[bold]Action:[/bold] {action.upper()}\n"
        f"[bold]Item:[/bold] {book.get('book_title')} by {book.get('author')}\n"
        f"[bold]ISBN:[/bold] {book.get('isbn')}\n"
        f"----------------------------------------\n"
        f"[bold green]TOTAL PAID: ${price}[/bold green]"
    )
    
    console.print(Panel(receipt_content, title="🧾 TRANSACTION RECEIPT", border_style="green", expand=False))
    
    # Save the ISBN to the history as well to make duplicate-checking accurate
    return {
        "invoice_id": invoice_id, 
        "date": date_now, 
        "action": action, 
        "book": book.get('book_title'), 
        "isbn": book.get('isbn'), 
        "price": price
    }


def check_duplicate_transaction(username: str, target_book: dict, users_file: str) -> bool:
    """
    Safely and strictly checks if a user already owns a book by matching 
    the ISBN or Title (case-insensitive, ignoring trailing spaces).
    """
    users = load_users(users_file)
    user_record = next((u for u in users if u.get("username") == username), None)
    
    if not user_record or not user_record.get("history"):
        return False
        
    target_isbn = str(target_book.get("isbn", "")).strip().lower()
    target_title = str(target_book.get("book_title", "")).strip().lower()
    
    for record in user_record.get("history", []):
        rec_isbn = str(record.get("isbn", "")).strip().lower()
        rec_title = str(record.get("book", "")).strip().lower()
        
        # If either the ISBN or Title matches perfectly, they already have it
        if (target_isbn == rec_isbn and target_isbn != "") or (target_title == rec_title and target_title != ""):
            return True
            
    return False


def browse_library(books_file: str):
    """
    Displays the library inventory to the customer.
    """
    print("\n--- BROWSE LIBRARY ---")
    print("[INFO] Here you can view all available books in our catalog.")
    print("[INFO] Take note of the 'ISBN' if you wish to Buy or Issue a book.")
    print("-" * 40)
    
    view_books(books_file)


def buy_book(username: str, books_file: str, users_file: str):
    """
    Handles the purchasing of a book by a user, preventing accidental duplicate purchases.
    """
    print("\n--- BUY A BOOK ---")
    print("[REQUIREMENTS] 1. You need the exact ISBN of the book you want to buy.")
    print("[REQUIREMENTS] 2. Purchasing permanently adds the book to your collection and deducts from our stock.")
    print("-" * 40)
    
    books = load_books(books_file)
    users = load_users(users_file)
    
    isbn = prompt_isbn("Enter the ISBN of the book you want to BUY: ")
    target_book = next((b for b in books if b.get("isbn") == isbn), None)
    
    if not target_book:
        print("[!] Book not found in library. Please check the ISBN.")
        return

    if target_book.get("quantity", 0) <= 0:
        print("[!] Sorry, this book is currently out of stock.")
        return

    # ROBUST DUPLICATE CHECK
    if check_duplicate_transaction(username, target_book, users_file):
        console.print(f"\n[bold yellow]⚠️ NOTICE: You already have '{target_book.get('book_title')}' in your transaction history![/bold yellow]")
        proceed_anyway = questionary.confirm("Are you absolutely sure you want to BUY another copy?").ask()
        if not proceed_anyway:
            print("Transaction cancelled. You were not charged.")
            return

    price = target_book.get('price', 0.0)
    confirm = questionary.confirm(f"The price for '{target_book.get('book_title')}' is ${price}. Proceed with purchase?").ask()
        
    if not confirm:
        print("Transaction cancelled.")
        return

    # Update Book Inventory
    target_book["quantity"] -= 1
    _save_books(books_file, books)
    
    # Generate Invoice & Update User History
    receipt = generate_invoice(username, "BUY", target_book, price)

    for user in users:
        if user.get("username") == username:
            user.setdefault("history", []).append(receipt)
            break
            
    _save_users(users_file, users)
    logger.info(f"User '{username}' bought book ISBN {isbn}")


def issue_book(username: str, books_file: str, users_file: str):
    """
    Handles borrowing a book for a limited time, checking for duplicate issues.
    """
    print("\n--- ISSUE (BORROW) A BOOK ---")
    print("[REQUIREMENTS] 1. You need the exact ISBN of the book.")
    print("[REQUIREMENTS] 2. Issued books are completely free of charge ($0.00).")
    print("[REQUIREMENTS] 3. You MUST return the book within exactly 14 days.")
    print("-" * 40)
    
    books = load_books(books_file)
    users = load_users(users_file)
    
    isbn = prompt_isbn("Enter the ISBN of the book you want to ISSUE: ")
    target_book = next((b for b in books if b.get("isbn") == isbn), None)
    
    if not target_book:
        print("[!] Book not found in library. Please check the ISBN.")
        return

    if target_book.get("quantity", 0) <= 0:
        print("[!] Sorry, this book is currently unavailable for issuing (Out of stock).")
        return

    # ROBUST DUPLICATE CHECK
    if check_duplicate_transaction(username, target_book, users_file):
        console.print(f"\n[bold yellow]⚠️ NOTICE: You already have '{target_book.get('book_title')}' in your transaction history![/bold yellow]")
        proceed_anyway = questionary.confirm("Are you absolutely sure you want to ISSUE another copy?").ask()
        if not proceed_anyway:
            print("Transaction cancelled.")
            return

    due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    confirm = questionary.confirm(f"Issue '{target_book.get('book_title')}' for 14 days? (Due Date: {due_date})").ask()
        
    if not confirm:
        print("Transaction cancelled.")
        return

    # Update Book Inventory
    target_book["quantity"] -= 1
    _save_books(books_file, books)
    
    # Generate Invoice & Update User History
    receipt = generate_invoice(username, "ISSUE", target_book, 0.0)
    receipt["due_date"] = due_date

    for user in users:
        if user.get("username") == username:
            user.setdefault("history", []).append(receipt)
            break
            
    _save_users(users_file, users)
    logger.info(f"User '{username}' issued book ISBN {isbn}")


def view_user_history(username: str, users_file: str):
    """
    Shows the user their past transactions.
    """
    print("\n--- YOUR TRANSACTION HISTORY ---")
    print("[INFO] This lists all your previous purchases and current borrowed books.")
    print("-" * 40)
    
    users = load_users(users_file)
    user_data = next((u for u in users if u.get("username") == username), None)
    
    if not user_data or not user_data.get("history"):
        print("\nYou have no transaction history yet.")
        return
        
    table = Table(title=f"📜 Transaction History for {username}", show_header=True, header_style="bold cyan")
    table.add_column("Date", style="dim")
    table.add_column("Action", style="bold")
    table.add_column("Book Title")
    table.add_column("Price/Due Date", style="yellow")
    
    for record in user_data["history"]:
        extra = f"${record['price']}" if record['action'] == "BUY" else f"Due: {record.get('due_date', 'N/A')}"
        table.add_row(record["date"], record["action"], record["book"], extra)
        
    console.print(table)


def customer_dashboard(username: str):
    """
    The main interactive menu shown to a logged-in user.
    """
    while True:
        print("\n")
        choice = questionary.select(
            f"========== WELCOME, {username.upper()} ==========\nSelect a task:",
            choices=[
                questionary.Choice("📖 1. Browse Library", "1"),
                questionary.Choice("🛒 2. Buy a Book", "2"),
                questionary.Choice("📚 3. Issue (Borrow) a Book", "3"),
                questionary.Choice("📜 4. View My History & Invoices", "4"),
                questionary.Choice("🔙 5. Logout", "5")
            ]
        ).ask()

        if choice == "1":
            browse_library(BOOKS_FILE)
        elif choice == "2":
            buy_book(username, BOOKS_FILE, USERS_FILE)
        elif choice == "3":
            issue_book(username, BOOKS_FILE, USERS_FILE)
        elif choice == "4":
            view_user_history(username, USERS_FILE)
        elif choice == "5" or choice is None:
            print("Logging out...")
            break


def register_user(users_file: str) -> bool:
    """
    Handles the registration of a new customer with strict validation.
    Enforces password and username strength requirements.
    """
    users = load_users(users_file)
    print("\n--- Create Account ---")
    print("[REQUIREMENTS] 1. Username must be unique.")
    print("[REQUIREMENTS] 2. Usernames & Passwords must be at least 8 chars, 5 letters, and 2 digits.")
    print("-" * 40)
    
    # 1. Validate Username
    while True:
        username = input("Choose a Username: ").strip()
        if not valid_username(username):
            print("[!] Invalid username. It must be at least 8 chars, 5 letters, and 2 digits.")
            continue
        if any(u.get("username") == username for u in users):
            print("[!] Username already exists. Please choose another.")
            continue
        break
        
    # 2. Validate Password
    while True:
        password = input("Choose a Password: ").strip()
        if not valid_password(password):
            print("[!] Invalid password. It must be at least 8 chars, 5 letters, and 2 digits. No spaces allowed.")
            continue
        break
        
    # 3. Save User
    users.append({"username": username, "password": password, "history": []})
    if _save_users(users_file, users):
        print("[bold green]Account created successfully! You can now log in.[/bold green]")
        logger.info(f"New user registered: {username}")
        return True
        
    return False


def login_user(users_file: str) -> str:
    """
    Handles customer authentication.
    """
    users = load_users(users_file)
    print("\n--- Login ---")
    print("[REQUIREMENTS] Please provide your registered Username and Password.")
    print("-" * 40)
    
    username = prompt_non_empty_string("Enter Username: ")
    password = prompt_non_empty_string("Enter Password: ")
    
    # Find user matching both username and password
    user = next((u for u in users if u.get("username") == username and u.get("password") == password), None)
    
    if user:
        print(f"[bold green]Login successful! Welcome back, {username}.[/bold green]")
        return username
    else:
        print("[bold red]Invalid username or password. Please try again.[/bold red]")
        return None


def customer_portal():
    """
    Displays the Customer Portal menu and routes to Login or Registration.
    """
    while True:
        print("\n")
        choice = questionary.select(
            "========== CUSTOMER PORTAL ==========\nSelect an option:",
            choices=[
                questionary.Choice("🔑 1. Login", "1"),
                questionary.Choice("📝 2. Register", "2"),
                questionary.Choice("🔙 3. Go Back", "3")
            ]
        ).ask()
        
        if choice == "1":
            logged_in_user = login_user(USERS_FILE)
            if logged_in_user:
                logger.info(f"User '{logged_in_user}' logged in.")
                customer_dashboard(logged_in_user)
                
        elif choice == "2":
            register_user(USERS_FILE)
            
        elif choice == "3" or choice is None:
            print("Returning to Main Menu...")
            break


# ==========================================
# 2. BOOK MANAGER (ADMIN)
# ==========================================

def book_manager_menu():
    """
    Runs the interactive loop for the Book Manager.
    """
    while True:
        print("\n")
        choice = questionary.select(
            "========== ADMIN: BOOK MANAGER ==========\nSelect a task:",
            choices=[
                questionary.Choice("📂 1. Load/Count Books", "1"),
                questionary.Choice("📖 2. View Books", "2"),
                questionary.Choice("🔍 3. Search Books (Partial match on Title/Author)", "3"),
                questionary.Choice("🗂️ 4. Filter Books (Exact match or Range)", "4"),
                questionary.Choice("➕ 5. Add Book", "5"),
                questionary.Choice("✏️ 6. Update Book", "6"),
                questionary.Choice("🗑️ 7. Delete Book", "7"),
                questionary.Choice("🔙 8. Return to Main Menu", "8")
            ]
        ).ask()

        if choice == "1":
            books = load_books(BOOKS_FILE)
            print("Books loaded successfully.")
            print("Total books:", len(books))

        elif choice == "2":
            view_books(BOOKS_FILE)

        elif choice == "3":
            query = prompt_non_empty_string("Enter partial title or author to search: ")
            search_books(BOOKS_FILE, query)

        elif choice == "4":
            print("\n")
            sub_choice = questionary.select(
                "--- Filter Options ---",
                choices=[
                    questionary.Choice("📌 1. Filter by Exact Genre", "1"),
                    questionary.Choice("💲 2. Filter by Price Range", "2"),
                    questionary.Choice("🔙 3. Go Back", "3")
                ]
            ).ask()
            
            if sub_choice == "1":
                genre = prompt_string_only("Enter genre to filter by (letters only): ")
                filter_books(BOOKS_FILE, "genre", genre)
            elif sub_choice == "2":
                min_p = prompt_float("Enter minimum price: $", min_val=0.0)
                max_p = prompt_float(f"Enter maximum price (must be >= {min_p}): $", min_val=min_p)
                filter_by_range(BOOKS_FILE, "price", min_p, max_p)

        elif choice == "5":
            print("\n--- Enter Book Details ---")
            book = {
                "book_title": prompt_non_empty_string("Enter book title: "),
                "author": prompt_string_only("Enter author (letters only): "),
                "genre": prompt_string_only("Enter genre (letters only): "),
                "publication_date": prompt_date("Enter publication date (YYYY-MM-DD): "),
                "isbn": prompt_isbn("Enter ISBN: "),
                "price": prompt_float("Enter price: $", min_val=0.0),
                "quantity": prompt_int("Enter quantity: ", min_val=0),
                "language": prompt_string_only("Enter language (letters only): ")
            }
            add_book(BOOKS_FILE, book)

        elif choice == "6":
            isbn = prompt_isbn("Enter ISBN of book to update: ")
            
            # EARLY CHECK: Find the specific book before proceeding
            books = load_books(BOOKS_FILE)
            target_book = next((b for b in books if b.get("isbn") == isbn), None)
            
            if not target_book:
                print("Error: Book not found. Please check the ISBN and try again.")
                continue

            print("\nEnter new details:")
            updated_data = {
                "book_title": prompt_non_empty_string("Enter book title: "),
                "author": prompt_string_only("Enter author (letters only): "),
                "genre": prompt_string_only("Enter genre (letters only): "),
                "publication_date": prompt_date("Enter publication date (YYYY-MM-DD): "),
                "price": prompt_float("Enter price: $", min_val=0.0),
                "quantity": prompt_int("Enter quantity: ", min_val=0),
                "language": prompt_string_only("Enter language (letters only): ")
            }
            
            # COMPARISON TABLE
            print("\n")
            table = Table(title="⚠️ Please Review Your Changes ⚠️", show_header=True, header_style="bold magenta")
            table.add_column("Field", style="cyan", justify="right")
            table.add_column("Previous Data", style="red")
            table.add_column("New Data", style="green")
            
            table.add_row("Title", str(target_book.get("book_title")), str(updated_data.get("book_title")))
            table.add_row("Author", str(target_book.get("author")), str(updated_data.get("author")))
            table.add_row("Genre", str(target_book.get("genre")), str(updated_data.get("genre")))
            table.add_row("Pub Date", str(target_book.get("publication_date")), str(updated_data.get("publication_date")))
            table.add_row("Price", f"${target_book.get('price', 0.0)}", f"${updated_data.get('price', 0.0)}")
            table.add_row("Quantity", str(target_book.get("quantity")), str(updated_data.get("quantity")))
            table.add_row("Language", str(target_book.get("language")), str(updated_data.get("language")))
            
            console.print(table)
            print("\n")
            
            # CONFIRMATION
            confirm = questionary.confirm("Do you want to apply these changes?").ask()
            
            if confirm:
                update_book(BOOKS_FILE, isbn, updated_data)
            else:
                logger.info("User cancelled book update.")
                print("Update cancelled. Previous data was retained.")

        elif choice == "7":
            isbn = prompt_isbn("Enter ISBN of book to delete: ")
            
            # EARLY CHECK: Find the specific book before proceeding
            books = load_books(BOOKS_FILE)
            target_book = next((b for b in books if b.get("isbn") == isbn), None)
            
            if not target_book:
                print("Error: Book not found. Please check the ISBN and try again.")
                continue
                
            # DISPLAY BOOK DETAILS TO BE DELETED
            print("\n")
            table = Table(title="🚨 Book Scheduled for Deletion 🚨", show_header=False)
            table.add_column("Field", style="cyan", justify="right")
            table.add_column("Value", style="red")
            
            table.add_row("Title:", str(target_book.get("book_title")))
            table.add_row("Author:", str(target_book.get("author")))
            table.add_row("Genre:", str(target_book.get("genre")))
            table.add_row("Price:", f"${target_book.get('price', 0.0)}")
            table.add_row("ISBN:", str(target_book.get("isbn")))
            
            console.print(table)
            print("\n")

            # CONFIRMATION
            confirm = questionary.confirm("Are you sure you want to PERMANENTLY delete this book?").ask()
            
            if confirm:
                delete_book(BOOKS_FILE, isbn)
            else:
                logger.info("User cancelled book deletion.")
                print("Deletion cancelled. The book was retained.")

        elif choice == "8" or choice is None:
            print("Returning to Main Menu...")
            break


# ==========================================
# 3. USER VALIDATION TOOLS
# ==========================================

def user_validation_menu():
    """
    Runs the interactive loop for testing user validation functions.
    """
    while True:
        print("\n")
        option = questionary.select(
            "========== USER VALIDATION ==========\nSelect a task:",
            choices=[
                questionary.Choice("📧 1. Check Email", "1"),
                questionary.Choice("🎂 2. Check Age", "2"),
                questionary.Choice("📅 3. Check Date-Time", "3"),
                questionary.Choice("👤 4. Check Username", "4"),
                questionary.Choice("🔑 5. Check Password", "5"),
                questionary.Choice("🔢 6. Check Number", "6"),
                questionary.Choice("🔙 7. Return to Main Menu", "7")
            ]
        ).ask()

        if option == "1":
            while True:
                value = input("Enter email: ")
                if is_valid_email(value):
                    print("Result: Valid email")
                    break
                else:
                    print("Error: Invalid email address format or extension. Please re-enter.")

        elif option == "2":
            while True:
                value = prompt_int("Enter age: ")
                if valid_age(value):
                    print("Result: Valid age")
                    break
                else:
                    print("Error: Age must be between 0 and 100. Please re-enter.")

        elif option == "3":
            while True:
                value = input("Enter date-time (YYYY-MM-DD HH:MM:SS): ")
                if valid_date_Time(value):
                    print("Result: Valid date-time")
                    break
                else:
                    print("Error: Invalid format. Must match YYYY-MM-DD HH:MM:SS. Please re-enter.")

        elif option == "4":
            print("\n[USERNAME REQUIREMENTS]")
            print(" - Minimum length: 8 characters")
            print(" - At least 5 alphabetic letters")
            print(" - At least 2 numeric digits")
            while True:
                value = input("Enter username: ")
                if valid_username(value):
                    print("Result: Valid username")
                    break
                else:
                    print("Error: Username does not meet minimum requirements. Please re-enter.")

        elif option == "5":
            print("\n[PASSWORD REQUIREMENTS]")
            print(" - Minimum length: 8 characters")
            print(" - At least 5 alphabetic letters")
            print(" - At least 2 numeric digits")
            print(" - No spaces allowed")
            while True:
                value = input("Enter password: ")
                if valid_password(value):
                    print("Result: Valid password")
                    break
                else:
                    print("Error: Password does not meet minimum requirements. Please re-enter.")

        elif option == "6":
            while True:
                value = input("Enter 10-digit number: ")
                try:
                    num_val = int(value)
                    if valid_number(num_val):
                        print("Result: Valid 10-digit number")
                        break
                    else:
                        print("Error: Number must be a valid 10-digit integer. Please re-enter.")
                except ValueError:
                    print("Error: Input must contain digits only. Please re-enter.")

        elif option == "7" or option is None:
            print("Returning to Main Menu...")
            break


# ==========================================
# MASTER ENTRY
# ==========================================

def main():
    """
    Master entry point for the combined application.
    """
    logger.info("Application started.")
    
    while True:
        print("\n")
        choice = questionary.select(
            "========== LIBRARY & BOOKSTORE SYSTEM ==========\nSelect a Portal:",
            choices=[
                questionary.Choice("🛍️ 1. Customer Portal (Login/Buy/Issue)", "1"),
                questionary.Choice("🔐 2. Admin Portal (Book Manager)", "2"),
                questionary.Choice("🛠️ 3. Validation Tools", "3"),
                questionary.Choice("❌ 4. Exit Application", "4")
            ]
        ).ask()
        
        if choice == "1":
            customer_portal()
        elif choice == "2":
            book_manager_menu()
        elif choice == "3":
            user_validation_menu()
        elif choice == "4" or choice is None:
            print("Exiting application. Goodbye!")
            logger.info("Application exited cleanly by user.")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Application terminated abruptly via KeyboardInterrupt (Ctrl+C).")
        print("\nExiting application. Goodbye!")