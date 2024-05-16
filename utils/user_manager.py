import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists('data/users.txt'):
            with open('data/users.txt', 'w') as f:
                pass

        with open('data/users.txt', 'r') as f:
            for line in f:
                if line.strip(): 
                    username, password = line.strip().split(',')
                    self.users[username] = password

    def save_users(self):
        with open('data/users.txt', 'w') as f:
            for username, password in self.users.items():
                f.write(f"{username},{password}\n")

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
            print("\nUsername already exists! Please input another.")
            return False

        if not self.validate_username(username):
            print("\nThe username does not meet the requirements, must be at least 4 characters.")
            return False
        
        if not self.validate_password(password):
            print("\nThe password does not meet the requirements, must be at least 8 characters.")
            return False
        
        self.users[username] = password
        self.save_users()
        print("Registration successful!")
        return True
    
    def login(self, username, password):
        if username in self.users:
            if self.users[username] == password:
                return True
            else:
                print("\nIncorrect password. Please try again.")
                return False 
        else:
            print("\nUsername not found. Please input a valid username.")
            return False