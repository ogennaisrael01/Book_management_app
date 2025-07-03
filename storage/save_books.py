import json


def save_books(books, file_name="books.json"):
    try:
        with open(file_name, "w") as file:
            json.dump(books, file, indent=4)

    except json.JSONDecodeError:
        print(f"Error saving books to {file_name}")

def load_books(file_name="books.json"):
    try:
    
        with open(file_name, 'r') as file:
            books = json.load(file)
            return books
        
    except json.JSONDecodeError:
        return []