from tabulate import tabulate
from random import choices
from copy import deepcopy

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['-' for i in range(size)] for j in range(size)]
        self.ships = int(size**2 * 0.25)

    def print_grid(self):
        print(tabulate(self.grid, tablefmt="pretty"))            

    def num_ships(self):
        return self.ships 

    def place_random_ships(self):
        self.ships_grid = []
        ships_size = deepcopy(self.ships)
        while ships_size:
            pos = tuple(choices(range(self.size), k=2))
            if pos not in self.ships_grid:
                self.ships_grid.append(pos)
                ships_size -= 1

    def attack(self, position):
        x, y = position
        if self.grid[x][y] == 'X' or self.grid[x][y] == 'O':
            return 0
        elif position in self.ships_grid:
            self.grid[x][y] = 'O'
            self.ships -= 1
            return 1
        else:
            self.grid[x][y] = 'X'
            return -1
