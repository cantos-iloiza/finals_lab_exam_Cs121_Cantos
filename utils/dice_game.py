import datetime
import os
import random
from utils.scores import Score  # Importing Score class from utils.scores module
from utils.user_manager import UserManager  # Importing UserManager class from utils.user_manager module

class DiceGame:
    
    def current_time():  # Defining a static method to get current time
        return datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")

    def __init__(self):
        self.user_manager = UserManager()  # Initializing UserManager object
        self.scores = []  # List to store scores
        self.current_user = None  # Current user logged in
        self.load_scores()  # Loading scores from file

    def load_scores(self):  # Method to load scores from file
        if not os.path.exists('data'):  # Checking if data directory exists
            os.makedirs('data')  # Creating data directory if it doesn't exist

        if not os.path.exists('data/rankings.txt'):  # Checking if rankings file exists
            with open('data/rankings.txt', 'w') as f:  # Creating rankings file if it doesn't exist
                pass
        else:
            with open('data/rankings.txt', 'r') as f:  # Opening rankings file
                for line in f:  # Reading each line in the file
                    username, game_id, points, wins = line.strip().split(',')  # Splitting data
                    score = Score(username, game_id, int(points), int(wins))  # Creating Score object
                    self.scores.append(score)  # Appending score to scores list

    def save_score(self, score):  # Method to save score to file
        with open('data/rankings.txt', 'a') as f:  # Opening file in append mode
            f.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")  # Writing score to file

    def game_rules(self):  # Method to display game rules
        print("\nGame Rules -------------------------------------------------------------------------------")
        print("""
            1. Once the user start the game, the dice is rolled automatically.
            2. There would be 3 stage levels per round, if the user wins a round, they'll
              get a point and if they win the stage, 3 points are added.
            3. If the user won a round, they can choose to keep playing or exit the game. 
            4. The winner will be determined in a best of three game.
            """)
        print("-------------------------------------------------------------------------------------------")
        input("Press ENTER to return....")
        self.menu()  # Returning to the main menu

    def play_game(self):  # Method to play the game
        print(f"\nGame Start! {self.current_user} vs Computer!")
        input("Press ENTER to roll the dice >>>")  # Waiting for user to roll dice
        
        total_points = 0  # Total points earned
        total_stages_won = 0  # Total stages won
        
        while True:  # Game loop
            stage_points = 0  # Points earned in current stage

            for stage in range(3):  # Three stages per round
                print("\n====================")
                print(f"Stage {stage+1}:")
                print("====================")

                user_score = random.randint(1, 6)  # User's dice roll
                cpu_score = random.randint(1, 6)  # Computer's dice roll

                print(f"You rolled: {user_score}")
                print(f"CPU rolled: {cpu_score}\n")

                if user_score > cpu_score:
                    print("You win this round!")
                    stage_points += 1
                elif user_score < cpu_score:
                    print("CPU wins this round!")
                else:
                    print("It's a tie! Roll again...")

            if stage_points > 0:  # If user won at least one stage
                total_stages_won += 1
                total_points += 3
                print("\nYou win this stage!")
                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                if choice != '1':
                    break
            else:
                print("Game over! Try harder next time, pal.")
                break
        
        print("\n>>>>> Score Sheet <<<<<")
        print(f"You've won {total_points} point/s.")
        print(f"You've won on {total_stages_won} stage/s.")

        if self.current_user:  # If a user is logged in
            self.update_player_scores(total_stages_won)  # Updating player's scores
            self.menu()  # Returning to main menu

    def update_player_scores(self, user_wins):  # Method to update player's scores
        user_score = None
        for score in self.scores:  # Searching for user's score
            if score.username == self.current_user and score.game_id == "dice_game":
                user_score = score
                break
            
        if user_score is None:  # If user has no score yet
            user_score = Score(self.current_user, "dice_game", 0, 0)  # Creating new score
            self.scores.append(user_score)  # Appending new score 

        if user_wins > 0:  # If user won at least one stage
            user_score.points += user_wins * 3  # Adding points
            user_score.wins += user_wins  # Incrementing wins  

        self.save_score(user_score)  # Saving updated score

    def show_top_scores(self):  # Method to display top scores
        if self.scores:  # If scores exist
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>> Top 10 Scores <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("======================================================================")
            sorted_scores = sorted(self.scores, key=lambda x: x.points, reverse=True)[:10]  # Sorting scores
            for i, score in enumerate(sorted_scores, 1):  # Enumerating scores
                print(f"{i}. User: {score.username}, Points: {score.points}, Wins: {score.wins}")
            print("======================================================================")
            self.menu()  # Returning to main menu
        
        else:  # If no scores exist
            print("\n=============================")
            print("---- No scores available ----")
            print("=============================")
            self.menu()  # Returning to main menu

    def menu(self):  # Method to display menu
        while True:  # Menu loop
            if self.current_user:  # If user is logged in
                print("\n======== Welcome to the Dice Roll Game! ========")
                print("Time Logged in: " + DiceGame.current_time())  # Displaying current time
                print(f"Hello, {self.current_user}!")
                print("------------------------------------------------")
                print("1. Start Dice Game")
                print("2. Show Top Scores")
                print("3. Game Rules")
                print("4. Log out")
                print("================================================")
                
                choice = input("Enter your choice: ")  # Taking user input
                if choice == '1':
                    self.play_game()
                    break
                elif choice == '2':
                    self.show_top_scores()
                    break
                elif choice == '3':
                    self.game_rules()
                    break
                elif choice == '4':
                    input("\nLogging out...")
                    print("\nTime Logged out: " + DiceGame.current_time())
                    self.logout()
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
            else:
                print("You are not logged in.")
                break
        
    def logout(self):
        self.current_user = None
