import os

class UserManager:
    def __init__(self):
        # Initialize an empty dictionary to store user credentials
        self.users = {}
        # Load existing user data from file
        self.load_users()

    def load_users(self):
        # Create 'data' directory if it doesn't exist
        if not os.path.exists('data'):
            os.makedirs('data')

        # Create 'users.txt' file if it doesn't exist
        if not os.path.exists('data/users.txt'):
            with open('data/users.txt', 'w') as f:
                pass

        # Read user data from 'users.txt' and populate the 'users' dictionary
        with open('data/users.txt', 'r') as f:
            for line in f:
                if line.strip(): 
                    username, password = line.strip().split(',')
                    self.users[username] = password

    def save_users(self):
        # Write user data from the 'users' dictionary to 'users.txt' file
        with open('data/users.txt', 'w') as f:
            for username, password in self.users.items():
                f.write(f"{username},{password}\n")

    def validate_username(self, username):
        # Check if the username meets the minimum length requirement
        return len(username) >= 4

    def validate_password(self, password):
        # Check if the password meets the minimum length requirement
        return len(password) >= 8
    
    def register(self, username, password):
        # Check if the username already exists
        if username in self.users:
            print("\nUsername already exists! Please input another.")
            return False

        # Validate username length
        if not self.validate_username(username):
            print("\nThe username does not meet the requirements, must be at least 4 characters.")
            return False
        
        # Validate password length
        if not self.validate_password(password):
            print("\nThe password does not meet the requirements, must be at least 8 characters.")
            return False
        
        # Add new user to the 'users' dictionary and save to file
        self.users[username] = password
        self.save_users()
        print("Registration successful!")
        return True
    
    def login(self, username, password):
        # Check if username exists in the 'users' dictionary
        if username in self.users:
            # Check if the provided password matches the stored password for the username
            if self.users[username] == password:
                return True
            else:
                print("\nIncorrect password. Please try again.")
                return False 
        else:
            print("\nUsername not found. Please input a valid username.")
            return False
