import json

class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"{self.title} by {self.author} -{self.isbn} -{status}"
class PhysicalBook(Book):
    def __init__(self,title,author,isbn,available,shelf_location):
        super().__init__(title,author,isbn,available)
        self.shelf_location=shelf_location
    def __str__(self):
         return f"{super().__str__()} - Shelf Location: {self.shelf_location}"

class EBook(Book):
    def __init__(self,title,author,isbn,available,file_size_mb):
        super().__init__(title,author,isbn,available)
        self.file_size_mb=file_size_mb
    def __str__(self):
        return f"{super().__str__()} - File Size: {self.file_size_mb} MB"
    
class Library:
    def __init__(self,books=None):
        self.books = books if books is not None else []
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,isbn):
        self.books=[book for book in self.books if book.isbn != isbn]
    def checkout_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn and book.available:
                book.available=False
                return f"checked out {book.title}"
        return "Book not available for checkout"
    def return_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn and not book.available:
                book.available=True
                return f"returned {book.title}"
        return "Book not found or already available"
    def search_by_author(self,author):
        for book in self.books:
            if book.author.lower()==author.lower():
                print(book)
    def list_available_books(self):
        for book in self.books:
            if book.available:
                print(book)
    


    def save_to_json(self):
        data = []
        for book in self.books:
            if isinstance(book, PhysicalBook):
                data.append({
                    "type": "physical",
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "available": book.available,
                    "shelf_location": book.shelf_location
                    })
            elif isinstance(book, EBook):
                data.append({
                     "type": "ebook",
                     "title": book.title,
                     "author": book.author,
                     "isbn": book.isbn,
                     "available": book.available,
                     "file_size_mb": book.file_size_mb
                     })
        with open("library.json", "w") as f:
            json.dump(data, f, indent=4)  # saves to file
    
    def load_from_json(self):
        try:
              with open("library.json", "r") as f:
                     data = json.load(f)  # reads from file
                     for item in data:
                          if item["type"] == "physical":
                              book = PhysicalBook(item["title"], item["author"], str(item["isbn"]), item["available"], item["shelf_location"])
                          elif item["type"] == "ebook":
                              book = EBook(item["title"], item["author"], str(item["isbn"]), item["available"], item["file_size_mb"])
                          self.books.append(book)
        except FileNotFoundError:
            pass  # first time running, no file yet — that's fine

