from board import Board
from player import Player

class Battleship:
    def __init__(self):
        self.player = Player()
        self.board = Board()
        self.remaining_guesses = 0

    def start_game(self):
        pass

    def is_win(self):
        return False

    def is_lost(self):
        return False

    def is_game_over(self):
        return False

    def turn(self):
        pass

