import unittest
from book import BookManager
from user import UserManager
from check import CheckoutManager
from storage import Storage

class TestLibraryManagementSystem(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment before any tests are run."""
        cls.book_manager = BookManager('test_books.json')
        cls.user_manager = UserManager('test_users.json')
        cls.checkout_manager = CheckoutManager('test_checkouts.json', cls.book_manager)

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests have run."""
        Storage.save_data('test_books.json', [])
        Storage.save_data('test_users.json', [])
        Storage.save_data('test_checkouts.json', [])

    def setUp(self):
        """Set up before each test."""
        self.book_manager.books = []
        self.user_manager.users = []
        self.checkout_manager.checkouts = []

    def test_add_book(self):
        """Test adding a book."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        self.assertEqual(len(self.book_manager.books), 1)

    def test_update_book(self):
        """Test updating a book."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        self.book_manager.update_book('1234567890', title='New Title')
        self.assertEqual(self.book_manager.books[0].title, 'New Title')

    def test_delete_book(self):
        """Test deleting a book."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        self.book_manager.delete_book('1234567890')
        self.assertEqual(len(self.book_manager.books), 0)

    def test_list_books(self):
        """Test listing books."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        books = self.book_manager.list_books()
        self.assertEqual(len(books), 1)

    def test_search_books(self):
        """Test searching for books."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        books_by_title = self.book_manager.search_books_by_title('Test Title')
        self.assertEqual(len(books_by_title), 1)
        books_by_author = self.book_manager.search_books_by_author('Test Author')
        self.assertEqual(len(books_by_author), 1)
        books_by_isbn = self.book_manager.search_books_by_isbn('1234567890')
        self.assertEqual(len(books_by_isbn), 1)

    def test_add_user(self):
        """Test adding a user."""
        self.user_manager.add_user('Test User', 'user1')
        self.assertEqual(len(self.user_manager.users), 1)

    def test_update_user(self):
        """Test updating a user."""
        self.user_manager.add_user('Test User', 'user1')
        self.user_manager.update_user('user1', name='New User')
        self.assertEqual(self.user_manager.users[0]['name'], 'New User')

    def test_delete_user(self):
        """Test deleting a user."""
        self.user_manager.add_user('Test User', 'user1')
        self.user_manager.delete_user('user1')
        self.assertEqual(len(self.user_manager.users), 0)

    def test_list_users(self):
        """Test listing users."""
        self.user_manager.add_user('Test User', 'user1')
        users = self.user_manager.list_users()
        self.assertEqual(len(users), 1)

    def test_search_users(self):
        """Test searching for users."""
        self.user_manager.add_user('Test User', 'user1')
        users_by_name = self.user_manager.search_users_by_name('Test User')
        self.assertEqual(len(users_by_name), 1)
        users_by_id = self.user_manager.search_users_by_user_id('user1')
        self.assertEqual(len(users_by_id), 1)

    def test_checkout_book(self):
        """Test checking out a book."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        self.user_manager.add_user('Test User', 'user1')
        self.checkout_manager.checkout_book('user1', '1234567890')
        self.assertFalse(self.book_manager.books[0].available)

    def test_checkin_book(self):
        """Test checking in a book."""
        self.book_manager.add_book('Test Title', 'Test Author', '1234567890')
        self.user_manager.add_user('Test User', 'user1')
        self.checkout_manager.checkout_book('user1', '1234567890')
        self.checkout_manager.checkin_book('user1', '1234567890')
        self.assertTrue(self.book_manager.books[0].available)

if __name__ == '__main__':
    unittest.main()
