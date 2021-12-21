
class Deterministic_die():
    def __init__(self, n):
        self.size = n
        self.next = 1
        self.rolls = 0

    def roll(self):
        out = self.next
        self.next = (self.next % self.size) + 1
        self.rolls += 1
        return out

class Player():
    number = 1
    
    def __init__(self, start):
        self.number = Player.number
        self.position = start
        self.score = 0
        Player.number += 1

    def move(self, value):
        self.position = (self.position + value - 1) % 10 + 1
        self.score += self.position

class Game():
    def __init__(self, players, die):
        self.die = die
        self.players = players

    def play(self):
        while True:
            for player in self.players:
                rolls = (self.die.roll(), self.die.roll(), self.die.roll())
                spaces = sum(rolls)
                player.move(spaces)
                #print(f'Player {player.number} rolls {rolls[0]}+{rolls[1]}+{rolls[2]} and moves to space {player.position} for a total score of {player.score}')
                if player.score >= 1000:
                    scores = [player.score for player in self.players]
                    print(f'WINNER: {player.number}')
                    print(f'SCORES: {scores}')
                    print(f'TOTAL ROLLS: {self.die.rolls}')
                    return

game = Game([Player(6), Player(7)], Deterministic_die(100))
game.play()


