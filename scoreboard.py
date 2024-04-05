class Scoreboard:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Scoreboard, cls).__new__(cls)
            cls._instance.scores = {}
        return cls._instance

    def update_score(self, player, points):
        if player in self.scores:
            self.scores[player] += points
        else:
            self.scores[player] = points

    def display_scores(self):
        print("\nCURRENT SCORE:")
        for player, score in self.scores.items():
            print(f"{player}: {score} points") 