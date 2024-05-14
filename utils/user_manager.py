import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        # Create data directory if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

        # Check if users.txt exists, if not, create it
        if not os.path.exists('data/users.txt'):
            with open('data/users.txt', 'w') as file:
                pass 

        # Load user data from users.txt
        with open('data/users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                self.users[username] = password

    def save_users(self):
        # Save user data to users.txt
        with open('data/users.txt', 'w') as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        if len(username) >= 4:
            return True
        else:
            return False

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else:
            return False

    def register(self, username, password):
        if username in self.users:
            print("Username already exists! Choose another.")
            return False
        
        # Validate username and password
        if not self.validate_username(username) or not self.validate_password(password):
            print("*-" * 28)
            print("The username or password does not meet the requirements.")
            print("*-" * 28)
            return False
        
        # Add new user to users dictionary and save to file
        self.users[username] = password
        self.save_users()
        return True

    def login(self, username, password):
        if username not in self.users:
            print("*-" * 10)
            print("Username not found.")
            print("*-" * 10)
            return False 
        
        if self.users[username] != password:
            print("*-" * 10)
            print("Incorrect Password.")
            print("*-" * 10)
            return False 
        
        return True
