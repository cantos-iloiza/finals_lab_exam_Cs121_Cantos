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

            with open('data/users.txt' , 'r') as f:
                for line in f:
                    username, password = line.strip().split(',')
                    self.users[username] = password

    def save_users(self):
        with open('data/users.txt', 'w') as f:
            for username, password in self.users.item():
                f.write(f"User1: {username}, Password: {password}\n")

    def validate_username(self, username):
        if len(username) >= 4:
            return 

    def validate_password(self, password):
        if len(password) >= 8:
            return 
    
    def register(self, username, password):
        if username in self.users:
            print("Username already exists! Please input another.")
            return

        if not self.validate_username(username):
            print("*-" * 28)
            print("The username does not meet the requirements, must be at least 4 characters.")
            print("*-" * 28)
            return False
        
        if not self.validate_password(password):
            print("*-" * 28)
            print("The password does not meet the requirements, must be at least 8 characters.")
            print("*-" * 28)
            return False
        
        self.users[username] = password
        self.save_users()
        return
    
    def login(self, username, password):
        if username in self.users:
            if self.users[username] == password:
                return True
            else:
                print("*-" * 10)
                print("Incorrect password. Please try again.")
                print("*-" * 10)
                return False 
        else:
            print("*-" * 10)
            print("Username not found. Please input a valid username.")
            print("*-" * 10)
            return False
            
        

        
