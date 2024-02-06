"""Board games."""

class Statistics:
    
    def __init__(self, filename):
        self.players = []
        self.games = []
        self.total = 0
        
    def get(self, path: str):
        
class Player:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.favourite = ""
        self.won = 0
        
    def amount(self):
        return self.amount
    
    def favourite(self):
        return self.favourite
    
    def won(self):
        return self.won

class Game:
    
    def __init__(self, game):
        self.game = game
        self.players = []
        
    def player_amount(self):
        return len(self.players)
    
    