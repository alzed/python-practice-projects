from minesweeper import Minesweeper
from tabulate import tabulate
import sys

class Display:
    def __init__(self, grid_size: int = 10):
        self.grid_size = grid_size
        self.game = Minesweeper(self.grid_size)
        self.mask = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.opened = self.grid_size**2 - self.game.n_mines
        self.done = False

    def start_game(self):
        self.game.populate_grid()

    def show_game(self):
        print(tabulate(self.mask, tablefmt="grid"))

    def is_valid_bound(self, row: int, column: int):
        valid_row = row >= 0 and row < self.grid_size
        valid_column = column >= 0 and column < self.grid_size
        return valid_row and valid_column

    def get_input(self):
        try:
            row, column = map(int, input().split(','))
            if self.is_valid_bound(row, column):
                return row, column
            raise ValueError(f'Invalid coordinates. Specify coordinates within 0 and {self.grid_size-1}')
        except KeyboardInterrupt:
            sys.exit()
        except:
            raise ValueError('Enter coordinates seperated by a comma')
        
    def is_done(self):
        if self.opened <= 0:
            print('CONGRATS! YOU WIN')
            self.is_done = True
        return self.done

    def play(self, row, column):
        if self.game.open_point(row, column) == 'X':
            self.mask[row][column] = 'X'
            self.opened -= 1
            self.show_game()
            print('GAME OVER')
            self.done = True
            return
        self.open(row, column)
        self.show_game()
            
            
    def open(self, row, column):
        around_coordinates = [
                [row-1, column-1], [row-1, column], [row-1, column+1],
                [row, column-1], [row, column+1],
                [row+1, column-1], [row+1, column], [row+1, column+1]
        ] 
        self.mask[row][column] = self.game.open_point(row, column)
        self.opened -= 1
        if self.mask[row][column] > 0:
            return
        for r, c in around_coordinates:
            if self.is_valid_bound(r, c) and self.mask[r][c] == '-':
                self.open(r, c)
        return
        