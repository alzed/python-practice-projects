from tabulate import tabulate
from random import choices
from copy import deepcopy

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['-' for i in size] for j in size]

    def print_grid(self):
        print(tabulate(self.grid, tablefmt="pretty"))            

    def place_random_ships(self):
        self.ships_grid = deepcopy(self.grid)
        ships = 1 if self.size == 2 else self.size
        ships_size = deepcopy(ships)
        while ships_size == 0:
            x, y = choices(range(self.size), k=2)
            if self.ships_grid[x][y] == '-':
                self.ships_grid[x][y] = 'H'
                ships_size -= 1
        return ships

    def hidden_ships_grid(self):
        print(tabulate(self.ships_grid, tablefmt="pretty"))

    def attack(self, position):
        x, y = position
        if self.grid[x][y] == 'X' or self.grid[x][y] == 'O':
            return 0
        elif self.ships_grid[x][y] == 'H':
            self.grid[x][y] = 'O'
            return 1
        else:
            self.grid[x][y] = 'X'
            return -1
