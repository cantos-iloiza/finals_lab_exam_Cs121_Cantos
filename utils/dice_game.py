import datetime
import os
import random
from utils.scores import Score  
from utils.user_manager import UserManager

class DiceGame:
    
    def current_time():
        return datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S.%f")

    def __init__(self):
        self.user_manager = UserManager()
        self.scores = []
        self.current_user = None
        self.load_scores()

    def load_scores(self):
        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists('data/rankings.txt'):
            with open('data/rankings.txt', 'w') as file:
                pass
        else:
            with open('data/rankings.txt', 'r') as file:
                for line in file:
                    username, game_id, points, wins = line.strip().split(',')
                    score = Score(username, game_id, int(points), int(wins))
                    self.scores.append(score)

    def save_score(self, score):
        with open('data/rankings.txt', 'a') as file:
            file.write(f"{score.username},{score.game_id},{score.points},{score.wins}\n")

    def game_rules(self):
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
        self.menu()

    def play_game(self):
        print(f"\nGame Start! {self.current_user} vs Computer!")
        input("Press ENTER to roll the dice >>>")
        total_points = 0
        total_stages_won = 0

        while True:
            stage_points = 0 
            for stage in range(3):
                print("====================")
                print(f"Stage {stage+1}:")
                print("====================")

                user_score = random.randint(1, 6)
                cpu_score = random.randint(1, 6)
                print(f"You rolled: {user_score}")
                print(f"CPU rolled: {cpu_score}\n")

            if user_score > cpu_score:
                print("You win this round!")
                stage_points += 1
            elif user_score < cpu_score:
                print("CPU wins this round!")
            else:
                print("It's a tie! Roll again...")

            if stage_points > 0:
                total_stages_won += 1
                total_points += 3
                print("You win this stage!")
                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")
                if choice != '1':
                    break
            else:
                print("Game over! Try harder next time, pal.")
                break
        
        print("\n>>>>> Score Sheet <<<<<")
        print(f"You've got {total_points} point/s.")
        print(f"You've won on {total_stages_won} stage/s.")

        if self.current_user:
            self.update_player_scores(total_stages_won)
            self.menu()

    def update_player_scores(self, user_wins):
        user_score = None
        for score in self.scores:
            if score.username == self.current_user and score.game_id == "dice_game":
                user_score = score
                break
            
        if user_score is None:
            user_score = Score(self.current_user, "dice_game", 0, 0)
            self.scores.append(user_score) 

        if user_wins > 0:  
            user_score.points += user_wins * 3  
            user_score.wins += user_wins  

        self.save_score(user_score)

    def show_top_scores(self):
        if not self.scores:
            print("\n=============================")
            print("---- No scores available ----")
            print("=============================")
            self.menu()
            return

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>> Top 10 Scores <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("======================================================================")
        sorted_scores = sorted(self.scores, key=lambda x: x.points, reverse=True)[:10]
        for i, score in enumerate(sorted_scores, 1):
            print(f"{i}. Username: {score.username}, Points: {score.points}, Wins: {score.wins}")
            
        self.menu()
    
    def menu(self):  
        while True:  # Use a loop to allow re-entry on invalid choice
            if self.current_user:
                print("\n======== Welcome to the Dice Roll Game! ========")
                print("Time Logged in: " + DiceGame.current_time())
                print(f"Hello, {self.current_user}!")
                print("------------------------------------------------")
                print("1. Start Dice Game")
                print("2. Show Top Scores")
                print("3. Game Rules")
                print("4. Log out")
                print("================================================")
                
                choice = input("Enter your choice: ")
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
