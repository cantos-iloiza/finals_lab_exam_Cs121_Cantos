class User:
    #Initializes a User object with the provided attributes.
    def __init__(self, username, password, points, stages_won): 
        self.username = username #The username of the user.
        self.password = password #The password of the user.
        self.points = 0 #The points earned by the user.
        self.stages_won = 0 #The number of stages won by the user.