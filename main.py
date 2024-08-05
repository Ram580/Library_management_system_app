from book import BookManager
from user import UserManager
from check import CheckoutManager

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Checkout Book")
    print("5. Check-in Book")
    print("6. Search Book")
    print("7. Update Book")
    print("8. Delete Book")
    print("9. Update User")
    print("10. Delete User")
    print("11. List Users")
    print("12. Search User")
    print("13. Exit")
    choice = input("Enter choice: ")
    return choice

def search_menu():
    print("\nSearch Book")
    print("1. By Title")
    print("2. By Author")
    print("3. By ISBN")
    choice = input("Enter choice: ")
    return choice

def user_search_menu():
    print("\nSearch User")
    print("1. By Name")
    print("2. By User ID")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = BookManager('books.json')
    user_manager = UserManager('users.json')
    checkout_manager = CheckoutManager('checkouts.json', book_manager)

    while True:
        choice = main_menu()
        try:
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_manager.add_book(title, author, isbn)
                print("Book added.")
            elif choice == '2':
                book_manager.list_books()
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == '4':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                checkout_manager.checkout_book(user_id, isbn)
            elif choice == '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to check-in: ")
                checkout_manager.checkin_book(user_id, isbn)
            elif choice == '6':
                search_choice = search_menu()
                if search_choice == '1':
                    title = input("Enter title to search: ")
                    books = book_manager.search_books_by_title(title)
                elif search_choice == '2':
                    author = input("Enter author to search: ")
                    books = book_manager.search_books_by_author(author)
                elif search_choice == '3':
                    isbn = input("Enter ISBN to search: ")
                    books = book_manager.search_books_by_isbn(isbn)
                else:
                    print("Invalid choice, please try again.")
                    continue

                if books:
                    for book in books:
                        availability = "available" if book.available else "unavailable"
                        print({**book.to_dict(), "availability": availability})
                else:
                    print("No books found.")
            elif choice == '7':
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                updates = {}
                if title:
                    updates["title"] = title
                if author:
                    updates["author"] = author
                book_manager.update_book(isbn, **updates)
                print("Book updated.")
            elif choice == '8':
                isbn = input("Enter ISBN of the book to delete: ")
                book_manager.delete_book(isbn)
                print("Book deleted.")
            elif choice == '9':
                user_id = input("Enter User ID of the user to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                updates = {}
                if name:
                    updates["name"] = name
                user_manager.update_user(user_id, **updates)
                print("User updated.")
            elif choice == '10':
                user_id = input("Enter User ID of the user to delete: ")
                user_manager.delete_user(user_id)
                print("User deleted.")
            elif choice == '11':
                user_manager.list_users()
            elif choice == '12':
                search_choice = user_search_menu()
                if search_choice == '1':
                    name = input("Enter name to search: ")
                    users = user_manager.search_users_by_name(name)
                elif search_choice == '2':
                    user_id = input("Enter User ID to search: ")
                    users = user_manager.search_users_by_user_id(user_id)
                else:
                    print("Invalid choice, please try again.")
                    continue

                if users:
                    for user in users:
                        print(user)
                else:
                    print("No users found.")
            elif choice == '13':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

