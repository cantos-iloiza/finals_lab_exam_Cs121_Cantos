class Score:
    def __init__(self, username, game_id, points=0, wins=0):
        # Initialize the Score object with the provided parameters.
        self.username = username  # Username associated with the score.
        self.game_id = game_id  # Game identifier associated with the score.
        self.points = points  # Total points earned in the game.
        self.wins = wins  # Number of wins achieved in the game.
