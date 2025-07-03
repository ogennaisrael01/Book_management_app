from storage.save_books import save_books, load_books


class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.ISBN = ""
        self.publication_date = ""
        self.description = ""
        self._is_available = True
        self.total_copies = 0
        self.available_copies = 0

    def __str__(self):
        return f"{self.title} By {self.author}"

    def to_dict(self):
        """ serialize book attributes to a dictionary """
        return {
            "title": self.title,
            "author": self.author,
            "ISBN": self.ISBN,
            "Publication_date": self.publication_date,
            "description": self.description,
            "available": self._is_available,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies
        }

class Library:

    def __init__(self):
        self._books = load_books()
    
    

    def add_book(self, title, author, ISBN, publication_date, description, total_copies):
        """
            Add books to you library
        """
        book = Book()
        book.title = title
        book.author = author
        book.ISBN = ISBN
        book.publication_date = publication_date
        book.description = description
        book.total_copies = total_copies
        book.available_copies = total_copies

        self._books.append(book.to_dict())
        save_books(self._books)

    def view_available_books(self):
        """
            List all availble books (Books not checked out) in our library
        """
        print("Available books")
        for index, books in enumerate(self._books):
            
            if books["available"] == True:
                print(f"{index + 1}. {books["title"]} By {books["author"]}: ({books["available_copies"]} copy(s) left)")

    def edit_book(self, title, author, ISBN, publication_date, description, total_copies):
        """
            Edit books in the library by the book title
        """
        available = True
        book_to_edit = int(input("Please enter the ID of the book to edit: "))
        print(f"Editing book: {self._books[book_to_edit] if book_to_edit in range(len(self._books)) else 0}")
        self._books[book_to_edit] = {
             
            "title": title,
            "author": author,
            "ISBN": ISBN,
            "Publication_date": publication_date,
            "description": description,
            "available": available,
            "total_copies": total_copies
         }
        save_books(self._books)
    

    def delete_book(self):
        """
            Delete by ID
        """
        ID = int(input("Enter the id to delete: "))
        if ID not in range(len(self._books)):
            print("Out of range")

        confirm = input(f"Are you sure you want to delete this book: {self._books[ID] if ID in range(len(self._books)) else 0}  :").strip().lower()
        if confirm not in ("yes", "y"):
            print('enter "yes" or "y" ')
            return 
        
        self._books.pop(ID)
        save_books(self._books)

    def view_all_books(self):
        """
            List all  books in our library
        """
        print("ALl books")
        for index, books in enumerate(self._books):
                print(f"{index}. {books["title"]} By {books["author"]}")