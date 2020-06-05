from board import Board
from player import Player

class Battleship:
    def __init__(self, size):
        self.player = Player()
        self.board = Board(size)
        self.remaining_guesses = size + 1 if size > 2 else size

    def start_game(self):
        self.board.print_grid()
        self.ships = self.board.place_random_ships()
        self.won = 0

    def turn(self, position):
        pos = list(map(int, position.split(',')))
        attacked = self.board.attack(pos)
        if attacked == -1:
            self.remaining_guesses -= 1
            self.board.print_grid()
        elif attacked == 1:
            self.won += 1
            self.board.print_grid()
        else:
            raise ValueError('Repeated guess')

    def is_won(self):
        return self.won == self.ships

    def is_lost(self):
        return self.remaining_guesses == 0

    def is_game_over(self):
        return self.is_won or self.is_lost
