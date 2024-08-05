from models import Checkout
from storage import Storage

class CheckoutManager:
    def __init__(self, storage_file, book_manager):
        self.storage_file = storage_file
        self.book_manager = book_manager
        self.checkouts = [Checkout(**data) for data in Storage.load_data(storage_file)]

    def checkout_book(self, user_id, isbn):
        if self.book_manager.book_exists(isbn):
            if self.is_book_available(isbn):
                checkout = Checkout(user_id, isbn)
                self.checkouts.append(checkout)
                self.book_manager.update_book(isbn, available=False)
                self.save_checkouts()
                print("Book checked out.")
            else:
                print("Book is not available.")
        else:
            print("Book does not exist.")

    def checkin_book(self, user_id, isbn):
        if not self.book_manager.book_exists(isbn):
            print("Book does not exist.")
            return

        if not any(checkout.user_id == user_id and checkout.isbn == isbn for checkout in self.checkouts):
            print("No record of this book being checked out by this user.")
            return

        self.checkouts = [checkout for checkout in self.checkouts if not (checkout.user_id == user_id and checkout.isbn == isbn)]
        self.book_manager.update_book(isbn, available=True)
        self.save_checkouts()
        print("Book checked in.")

    def is_book_available(self, isbn):
        for book in self.book_manager.books:
            if book.isbn == isbn:
                return book.available
        return False

    def save_checkouts(self):
        data = [checkout.to_dict() for checkout in self.checkouts]
        Storage.save_data(self.storage_file, data)