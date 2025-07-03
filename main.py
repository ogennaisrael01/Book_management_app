from menu import userMenu,  adminMenu
from models.books import Library
from models.borrow import BorrowBook
from storage.save_user import load_user
from models.users import User
from models.search import SearchBook

def admin():
    active = True
    while active:
            
        print("Admin dashboard\n")
        adminMenu()
        menu = int(input("Choose an action to perform: \n"))
        library = Library()
        match menu:
            case 1:
                #  Register accounts for users
                user = User()
                user.register()
            
            case 2:
                
                print("Add books to your library")
                
                try:
                    # Prompt for book details
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    ISBN = input("Enter book ISBN: ")
                    publication_date = input("Enter book publication date: ")
                    description = input("Enter book description: ")
                    total_copies = int(input("Enter total copies: "))
                    
                except ValueError:
                    print("Invalid. Please enter the correct details.")
                library.add_book(title, author, ISBN, publication_date, description, total_copies)

                add_more = input("\nDo you want to add more books? ")
                if add_more in ("yes", "y"):
                    continue
                else:
                    print("Book collection complete.")
                       
            case 3:
                library.view_all_books()

            case 4:
                print("Update book details")
                try:
                    # Prompt for book details
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    ISBN = input("Enter book ISBN: ")
                    publication_date = input("Enter book publication date: ")
                    description = input("Enter book description: ")
                    total_copies = int(input("Enter total copies: "))

                    if total_copies < 0:
                        raise ValueError("Total copies cannot be negative.")
                    if title == "" or author == "":
                        raise ValueError("Title and author must be filled out.")
                    
                except ValueError:
                    print("Invalid. Please enter the correct details.")

                library.edit_book(title, author, ISBN, publication_date, description, total_copies)
                print("Book details updated successfully.")
            case 5:
                print("Delete a book")
                library.delete_book()
                print("Book deleted successfully.")

            case 6:
                # print("View all available books")
                
                library.view_available_books()
            case 7:
                print("View borrowed books")
                books = BorrowBook()
                books.show_borrowed_book()
            case 8:
                print("All users")
                users = load_user()
                for user in users:
                    print(user["Name"])
            case 9:
                print("Logging out.....")
                active = False
                

def users():
    while True:
        print("User dashboard")

        userMenu()
        menu = int(input("Choose an action to perform: \n"))
        book = BorrowBook()
        match menu:
            case 1:
                name = input("\nWhat is your name? ")
                title = input("\nWhat is the title of the book you want to borrow? ")
                book.borrow_book(title, name)
            case 2:
                title = input("\nWhat is the name if the book you want to return? ")
                book.return_book(title)

            case 3:
                # print("View all available books")
                library = Library()
                library.view_available_books()

            case 4:
                name = input("Enter you name to fetch all your borrowed book(s)")
                book.show_user_borrowed_book(name)

            case 5:
                choice = input("Do you want to search by title or by author name: ").strip().lower()
                search = SearchBook()
                if choice == "title":
                    title = input("Enter the title you are looking for: ").strip().lower()
                    search.search_by_title(title)
                elif choice == "author":
                    author = input("Enter the name of the author: ").strip().lower()
                    search.search_by_author(author)
                else:
                    print("Invalid, choice")
                    
            case 6:
                print("Logging out....")
                break

            

def main():
    """
    """
    
    while True:
        print("Welcome to the Book Management App\n")
        exit_choice = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
        if exit_choice == "exit":
            print("Exiting the application...")
            break
    
        load_users = load_user()
        # sign in
        name = input("Enter you name for verification: ")
        password = input("Enter your password: ").strip()

        match_user = [user for user in load_users if user["Name"] == name and user["Password"] == password]
        if not match_user: 
            print("\nYou are not authenticated \nPlease register an account\n")
            continue

        else:
            input("Press enter to continue.\n")

        user = match_user[0]
        
        while True:
            if user["Role"] == "admin":
                admin()
                break
            elif user["Role"] == "user":
                 users()
                 break
            else:
                print("You can't access this program.")
        
                break
if __name__ == "__main__":
    main()





