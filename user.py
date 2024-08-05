from models import User
from storage import Storage

class UserManager:
    def __init__(self, storage_file):
        """Initialize the UserManager with a storage file."""
        self.storage_file = storage_file
        self.users = Storage.load_data(storage_file)

    def add_user(self, name, user_id):
        """Add a new user to the collection."""
        if not self.user_exists(user_id):
            user = {"name": name, "user_id": user_id}
            self.users.append(user)
            self.save_users()
        else:
            print("User already exists.")

    def user_exists(self, user_id):
        """Check if a user exists in the collection by User ID."""
        return any(user["user_id"] == user_id for user in self.users)

    def save_users(self):
        """Save the current list of users to storage."""
        Storage.save_data(self.storage_file, self.users)

    def list_users(self):
        """List all users in the collection."""
        for user in self.users:
            print(user)
        return self.users

    def update_user(self, user_id, **kwargs):
        """Update the details of a user by User ID."""
        for user in self.users:
            if user["user_id"] == user_id:
                for key, value in kwargs.items():
                    user[key] = value
                self.save_users()
                return
        print("User not found.")

    def delete_user(self, user_id):
        """Delete a user from the collection by User ID."""
        self.users = [user for user in self.users if user["user_id"] != user_id]
        self.save_users()

    def search_users_by_name(self, name):
        """Search users by name."""
        return [user for user in self.users if name.lower() in user["name"].lower()]

    def search_users_by_user_id(self, user_id):
        """Search users by User ID."""
        return [user for user in self.users if user["user_id"] == user_id]

