from board import Board
from player import Player

class Battleship:
    def __init__(self, size):
        self.player = Player()
        self.board = Board(size)
        self.remaining_guesses = self.board.num_ships() + 2

    def start_game(self):
        self.board.print_grid()
        self.board.place_random_ships()

    def turn(self):
        position = self.player.get_move()
        if 0 <= position[0]*position[1] <= (self.board.size-1)**2:
            attacked = self.board.attack(position)
            if attacked == -1:
                self.remaining_guesses -= 1
                self.board.print_grid()
            elif attacked == 1:
                print("You sunk my battleship!")
                self.board.print_grid()
            else:
                print('Repeated guess')
                self.turn()
        else:
            print("Invalid position")
            self.turn()

    def is_won(self):
        return self.board.num_ships() == 0

    def is_lost(self):
        return self.remaining_guesses == 0

    def is_game_over(self):
        return self.is_won() or self.is_lost()
