# Book Management Application

A simple command-line application for managing a library's books and users.

## Features

- Admin and user roles
- Register users (admin only)
- Add, edit, and delete books (admin only)
- View all books and available books
- Borrow and return books
- Track borrowed books per user
- Search books by title or author

## Usage

1. Run the application:
    ```sh
    python main.py
    ```
2. Log in with your name and password.
3. Follow the menu prompts for admin or user actions.

## Data Storage

- Books: `books.json`
- Users: `users.json`
- Borrowed books: `borrowed_books.json`

## Project Structure

- `main.py` - Entry point and main logic
- `menu.py` - Menu display functions
- `models/` - Core classes for books, users, borrowing, and searching
- `storage/` - Functions for saving/loading data

---

*educational purposes.*


### Author
## Ogenna Israel (Backend dev)
