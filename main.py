import datetime
from utils.dice_game import DiceGame  # Import the DiceGame class

def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")

def sign_up(game):
    try:
        # Prompt the user to register
        print("\nRegister-------------------------------------------------------------")
        username = input("Enter a username (at least 4 characters): ")
        password = input("Enter a password (at least 8 characters): ")
        input(f"Registering {username}.....")  
        print("-----------------------------------------------------------------------")

        # Attempt to register the user
        if game.user_manager.register(username, password):
            print("<<<<< Registered successfully >>>>> " + current_time())

        else:
            print(">>>>> Register failed. Please try again. <<<<<")

    except Exception as error:
        print("Error:", error)

def log_in(game):
    try:
        # Prompt the user to log in
        print("\nLog In-----------------------------------------------------------------")
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        input(f"Logging in.....") 
        print("-----------------------------------------------------------------------")

        if game.user_manager.login(username, password):
            game.current_user = username  # Set the current user
            print("<<<<< Logged In successfully >>>>> " + current_time())
            game.menu() 
        else:
            print("Invalid username or password.")

    except Exception as error:
        print("Error:", error)

def main():
    try:
        game = DiceGame()  # Initialize the DiceGame instance
        while True:
            # Display the main menu options
            print("\n======== Welcome to the Dice Roll Game! ========")
            print("1. Register")
            print("2. Log In")
            print("3. Exit")
            print("================================================")
            user_input = input("Enter your choice: ")

            # Process user input
            if user_input == '1':
                sign_up(game)  
            elif user_input == '2':
                log_in(game)  
            elif user_input == '3':
                print(current_time()) 
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.") 

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    main()  # Start the main function
