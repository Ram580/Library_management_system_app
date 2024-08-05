from models import Book
from storage import Storage

class BookManager:
    def __init__(self, storage_file):
        """Initialize the BookManager with a storage file."""
        self.storage_file = storage_file
        self.books = [Book(**data) for data in Storage.load_data(storage_file)]

    def add_book(self, title, author, isbn):
        """Add a new book to the collection."""
        if not self.book_exists(isbn):
            book = Book(title, author, isbn)
            self.books.append(book)
            self.save_books()
        else:
            print("Book already exists.")

    def book_exists(self, isbn):
        """Check if a book exists in the collection by ISBN."""
        return any(book.isbn == isbn for book in self.books)

    def save_books(self):
        """Save the current list of books to storage."""
        data = [book.to_dict() for book in self.books]
        Storage.save_data(self.storage_file, data)

    def list_books(self):
        """List all books in the collection."""
        for book in self.books:
            print(book.to_dict())
        return self.books
        

    def update_book(self, isbn, **kwargs):
        """Update the details of a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                for key, value in kwargs.items():
                    setattr(book, key, value)
                self.save_books()
                return
        print("Book not found.")

    def delete_book(self, isbn):
        """Delete a book from the collection by ISBN."""
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def search_books_by_title(self, title):
        """Search books by title."""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_books_by_author(self, author):
        """Search books by author."""
        return [book for book in self.books if author.lower() in book.author.lower()]

    def search_books_by_isbn(self, isbn):
        """Search books by ISBN."""
        return [book for book in self.books if isbn in book.isbn]
