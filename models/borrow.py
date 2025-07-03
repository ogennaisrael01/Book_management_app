
from storage.save_books import save_books, load_books
from storage.save_user import load_user
from storage.borrowed_books import save_borrowed_book, load_borrowed_books
from .users import User
import datetime
class BorrowBook:
    """
        Handles borrowing and returning of books
    """
    def __init__(self):
        self._books = load_books()
        self.users = load_user()
        self.borrowed_books = load_borrowed_books()

    
    def borrow_book(self, title, name):
        """
            
            Authenticates a user and allows them to borrow a book from the library.
            Prompts for user credentials, checks book availability, updates records,
            and saves the borrowing transaction with a timestamp.

        """

        for book in self._books:
                
            if title == book["title"] and book["available_copies"] > 0: 
                self.borrowed_books.append({
                    "title": book["title"],
                    "Name": name,
                    "date": str(datetime.datetime.now())
                }) 
                book["available_copies"] -= 1

                if book["available_copies"] == 0:
                    book["available"] = False

                save_books(self._books)
                save_borrowed_book(self.borrowed_books) # save borrowed books 
                return (f"{title} has been borrowed by {name}")
                
            
            
            elif title == book["title"] and book["available_copies"] == 0:
                return (f"Sorry, {title} is not available at the moment, Check back later.")
            

        else:
            return (f"Sorry, We do not have '{title}' in our library.")
            
            
           

    def return_book(self, title):
        """
            Return of a borrowed book.
            Prompts for book title, updates the book's availability.
            Removes the transaction from  borrowed books and saves changes back
        """
        for book in self._books:
            
            if title == book["title"]:
                if book["available_copies"] == book["total_copies"]:
                    break
                book["available_copies"] += 1
                if book["available_copies"] > 0:
                    book["available"] = True
                save_books(self._books)     
                break
        else:
            return ("Title did not match.")

        name = input("What is your name? ").strip().lower()
        for borrowed_book in self.borrowed_books:
            if title == borrowed_book["title"] and borrowed_book["Name"] == name:
                self.borrowed_books.remove(borrowed_book)
                save_borrowed_book(self.borrowed_books)

                print(f"{title} has been returned by {name}")
                break
        else:
            print("No matching record found for this book and user.")

    def show_borrowed_book(self):
        """
            Show all borrowed books from library
        """
        print("\nBooks borrowed from our library.")
        for borrowed_book in self.borrowed_books:
            print("=" * 50)
            print(f"Name: {borrowed_book["Name"]}, \
                  \nTItle: {borrowed_book["title"]},\
                    \nDate: {borrowed_book["date"] }")
            
    def show_user_borrowed_book(self, name):
        print("=" * 50)
        print(f"Books borrowed by {name}")
        for borrowed in self.borrowed_books:
            if name == borrowed["Name"]:
                print(f"Name: {borrowed["Name"]}, \
                \nTItle: {borrowed["title"]},\
                \nDate: {borrowed["date"] }")

        else:
            print(f"No book borrowed by {name}")