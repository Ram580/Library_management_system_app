# Library_management_system_app

### Overview

The Library Management System is designed to manage books and users, track book checkouts and check-ins, and maintain the availability status of books. The system is implemented using Object-Oriented Programming (OOP) principles to ensure modularity, scalability, and ease of maintenance. The application supports various operations such as adding, updating, deleting, listing, and searching books and users. Additionally, it provides a command-line interface (CLI) for user interaction and a simple logging mechanism for tracking operations.

  

### File Structure

book.py: Manages book-related operations.

user.py: Manages user-related operations.

check.py: Manages book checkouts and check-ins.

models.py: Contains data models for books, users, and checkouts.

storage.py: Provides functions for data storage and retrieval.

main.py: The main entry point for the application, containing the CLI.

Detailed Documentation

book.py

This module is responsible for managing book-related operations such as adding, updating, deleting, listing, and searching for books.

  

Classes and Methods

BookManager

**\_\_init\_\_**(self, storage\_file): Initializes the BookManager with a storage file.

add\_book(self, title, author, isbn): Adds a new book to the collection.

book\_exists(self, isbn): Checks if a book exists in the collection by ISBN.

save\_books(self): Saves the current list of books to storage.

list\_books(self): Lists all books in the collection.

update\_book(self, isbn, \*\*kwargs): Updates the details of a book by ISBN.

delete\_book(self, isbn): Deletes a book from the collection by ISBN.

search\_books\_by\_title(self, title): Searches books by title.

search\_books\_by\_author(self, author): Searches books by author.

search\_books\_by\_isbn(self, isbn): Searches books by ISBN.

user.py

This module is responsible for managing user-related operations such as adding, updating, deleting, listing, and searching for users.

  

Classes and Methods

UserManager

**\_\_init\_\_**(self, storage\_file): Initializes the UserManager with a storage file.

add\_user(self, name, user\_id): Adds a new user to the collection.

user\_exists(self, user\_id): Checks if a user exists in the collection by User ID.

save\_users(self): Saves the current list of users to storage.

list\_users(self): Lists all users in the collection.

update\_user(self, user\_id, \*\*kwargs): Updates the details of a user by User ID.

delete\_user(self, user\_id): Deletes a user from the collection by User ID.

search\_users\_by\_name(self, name): Searches users by name.

search\_users\_by\_user\_id(self, user\_id): Searches users by User ID.

check.py

This module is responsible for managing book checkouts and check-ins, tracking the availability status of books.

  

Classes and Methods

CheckoutManager

**\_\_init\_\_**(self, storage\_file, book\_manager): Initializes the CheckoutManager with a storage file and a BookManager instance.

checkout\_book(self, user\_id, isbn): Checks out a book to a user.

checkin\_book(self, user\_id, isbn): Checks in a book from a user.

is\_book\_available(self, isbn): Checks if a book is available for checkout.

save\_checkouts(self): Saves the current list of checkouts to storage.

models.py

This module defines data models for books, users, and checkouts. Each model provides a method to convert its instance to a dictionary format suitable for storage.

  

Classes and Methods

Book

  

**\_\_init\_\_**(self, title, author, isbn, available=True): Initializes a Book instance.

to\_dict(self): Converts the Book instance to a dictionary.

User

  

**\_\_init\_\_**(self, name, user\_id): Initializes a User instance.

to\_dict(self): Converts the User instance to a dictionary.

Checkout

  

**\_\_init\_\_**(self, user\_id, isbn): Initializes a Checkout instance.

to\_dict(self): Converts the Checkout instance to a dictionary.

storage.py

This module provides functions for data storage and retrieval, supporting JSON-based file storage.

  

Functions

load\_data(file\_path): Loads data from a specified file.

save\_data(file\_path, data): Saves data to a specified file.

main.py

This module serves as the main entry point for the application. It provides a command-line interface (CLI) for interacting with the library management system.

  

Functions

main\_menu(): Displays the main menu and obtains the user's choice.

search\_menu(): Displays the book search menu and obtains the user's choice.

user\_search\_menu(): Displays the user search menu and obtains the user's choice.

main(): The main function that drives the application, handling user input and executing corresponding operations.

Usage

Run the Application: Execute main.py to start the Library Management System.

bash

Copy code

python main.py

Main Menu: The main menu provides options to add books, list books, add users, check out books, check-in books, search books, update books, delete books, update users, delete users, list users, and search users.

  

Search Books: The search menu allows searching for books by title, author, or ISBN.

  

Search Users: The user search menu allows searching for users by name or User ID.