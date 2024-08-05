import unittest
from models import Library, Book
import book

class TestBookManagement(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_add_duplicate_book(self):
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        self.assertEqual(len(self.library.books), 1)

    def test_list_books(self):
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        book.add_book(self.library, "Another Book", "Another Author", "0987654321")
        self.assertEqual(len(self.library.books), 2)

    def test_update_book(self):
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        book.update_book(self.library, "1234567890", title="Updated Book")
        self.assertEqual(self.library.books[0].title, "Updated Book")

    def test_delete_book(self):
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        book.delete_book(self.library, "1234567890")
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        book.add_book(self.library, "Test Book", "Test Author", "1234567890")
        results = book.search_books(self.library, title="Test Book")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book")

if __name__ == '__main__':
    unittest.main()
