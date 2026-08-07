# 📚 Library & Bookstore Management System

A robust, interactive Command Line Interface (CLI) application built with Python. This system seamlessly integrates an **Admin Book Manager** with a fully functional **Customer Portal**, featuring rich UI elements, strict data validation, and automated background backups.

## ✨ Features

### 🛍️ Customer Portal
*   **User Authentication:** Secure registration and login system with strict username and password validation (enforces length, letters, digits, and no spaces).
*   **Book Purchasing & Issuing:** Customers can buy books or issue (borrow) them for 14 days.
*   **Smart Duplicate Checking:** Prevents users from accidentally buying or issuing a book they already own or have currently borrowed.
*   **Rich Receipts & History:** Generates beautiful invoice panels using the `rich` library and stores full transaction history for every user.

### 🔐 Admin Portal (Book Manager)
*   **Full CRUD Operations:** Add, view, update, and permanently delete books.
*   **Advanced Display & Filtering:** 
    *   Paginated, color-coded tables for viewing large inventories without flooding the terminal.
    *   Search by partial Title or Author.
    *   Filter by exact Genre or numeric Price Ranges.
*   **Safe Updates & Deletions:** Shows a "Before vs. After" comparison table before committing updates, and requires explicit confirmation before deleting records.

### 🛠️ Validation & System Security
*   **Robust Input Validation:** Strict format checking for Emails, Passwords, Usernames, Dates (YYYY-MM-DD), Ages, and 10-digit numbers.
*   **Data Persistence & Backups:** Safely reads and writes to JSON files. Automatically generates `.bak` backup files using Python's `shutil` before any data mutation to prevent corruption.
*   **Activity Logging:** Silently logs application events, successful logins, data modifications, and errors to `app.log` behind the scenes.
*   **Interactive UI:** Fully navigable using arrow keys via the `questionary` library—no more typing numbers to navigate menus!

## 🗂️ Project Structure

```text
📦 Library-Bookstore-System
 ┣ 📜 main.py                    # Master entry point and interactive menus
 ┣ 📜 MOCK_DATA.json             # Database storing the book inventory
 ┣ 📜 USERS.json                 # Database storing user credentials and transaction histories
 ┣ 📜 app.log                    # Auto-generated log file for system events
 ┣ 📜 README.md                  # Project documentation
 ┗ 📂 Utility                    # Core modular backend logic
   ┣ 📜 file_handler.py          # JSON read/write, search, filter, and table pagination logic
   ┣ 📜 input_validator.py       # String, email, date, and password regex/validation
   ┣ 📜 numeric_validator.py     # Integer, float, and age range validation
   ┗ 📜 loggers.py               # Application logging configuration
