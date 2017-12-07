
import random

class Dice:
    sides = [1,2,3,4,5,6]

    @classmethod
    def rolling(cls):
        val = random.choice(cls.sides)
        return val

class Game:
    attempts = 3
    players = {}

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = None

    def toss(self):
        pl_list = [self.player1, self.player2]
        Game.players['first'] =  random.choice(pl_list)
        pl_list.remove(Game.players['first'])
        Game.players['second'] =  pl_list[0]

    def play(self):
        first_score, second_score = 0,0

        for atm in range(Game.attempts):
            while atm < Game.attempts:
                first_score =first_score + Dice.rolling()
                print('score of player1 :', first_score)
                second_score =second_score + Dice.rolling()
                print('score of player2 :', second_score)
                break
        if first_score > second_score:
            print('Winner {} with score {}'.format(Game.players['first'],first_score ))
        elif first_score < second_score:
            print('Winner {} with score {}'.format(Game.players['second'],second_score ))
        else :
            print('match is draw with {} having score {} and {} having score {}'.format(Game.players['first'],first_score,Game.players['second'],second_score))
g = Game('king', 'kong')
g.toss()
g.play()
