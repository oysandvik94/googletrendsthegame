import random
import config as conf
from . import trendapi
from .player import Player

class Gamesession:
    currentWord = ""
    turn = 0

    def startGame(self, playerOneName, playerTwoName):
        self.playerOne = Player(playerOneName)
        self.playerTwo = Player(playerTwoName)

        self.generateWord()
     


    def getWord(self):
        return self.currentWord

    def generateWord(self):
        words = open(conf.STATIC_DIR + "dict.txt", 'r')
        lines = words.read().split("\n")
        self.currentWord = random.choice(lines)

    def playRound(self, playerOneTerm, playerTwoTerm):
        points = trendapi.getAverageScore(playerOneTerm, playerTwoTerm)

        self.playerOne.incrementScore(points["scoreOne"])
        self.playerTwo.incrementScore(points["scoreTwo"])

        self.turn += 1
        self.generateWord()

        return {"playerOneScore": self.playerOne.currentScore, "playerTwoScore": self.playerTwo.currentScore}
    
    def getTotalScores(self):
        return {"playerOneTotalScore": self.playerOne.totalScore, "playerTwoTotalScore": self.playerTwo.totalScore}

    def getGameData(self):
        gameData = {
            "playerOne": {
                "name": self.playerOne.name,
                "totalScore": self.playerOne.totalScore,
                "currentScore": self.playerOne.currentScore
            },
             "playerTwo": {
                "name": self.playerTwo.name,
                "totalScore": self.playerTwo.totalScore,
                "currentScore": self.playerTwo.currentScore
            },
            "term": self.currentWord,
            "turn": self.turn
        }

        return gameData