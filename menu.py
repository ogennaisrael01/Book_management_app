def adminMenu():

    print("=" * 50)
    menu = ["Create account for users", "Add new book", "View all books", "Update book datails", "Delete a book", "View all available books", "View borrowed books",\
            "View all users", "Logout"]
    for index, value in enumerate(menu):
        print(f"{index + 1}: {value}")



def userMenu():

    print("=" * 50)
    menu = ["Create an account", "Borrow a book", "Return a book", "Show available books", "View my borrowed books", \
            "Search for a book by title or author", "Logout"]

    for index, value in enumerate(menu):
        print(f"{index + 1}: {value}")
