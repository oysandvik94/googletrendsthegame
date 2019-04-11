class Player:
    name = ""
    totalScore = 0
    currentScore = 0

    def __init__(self, name):
        self.name = name

    def incrementScore(self, points):
        self.currentScore = points
        self.totalScore += points
