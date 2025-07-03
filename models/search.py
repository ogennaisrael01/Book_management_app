from storage.save_books import load_books

class SearchBook:
    def __init__(self):
        self._books = load_books()

    def search_by_title(self, title):
        """
            search for a book by its title
            the book will be displayed if available otherwise you will get an unavailable message
        """
        for book in self._books:
            if title == book["title"] and book["available"] == True:
                return book
            
            elif book["available"] == False and title == book["title"]:
                print("Sorry, Got checked out. check back later") 
                return   
        else:
            print(f"{title} is not available in our library")
    
    def search_by_author(self, author):
        """
            search for a book by its author
            Only available books are displayed 
        """
        for book in self._books:
            if author == book["author"] and book["available"] == True:
                print(book)
                return 
            
            elif book["available"] == False and  author == book["author"]:
                print("Sorry, Got checked out. check back later") 
                return
        else:
            print(f"We dont have a book written by {author} in this library")
