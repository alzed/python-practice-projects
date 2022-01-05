from random import randint

class Minesweeper:
    def __init__(self, grid_size: int = 10):
        self.grid_size = grid_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.n_mines = self.grid_size
        
    def _populate_mine(self):
        while True:
            row = randint(0, self.grid_size-1)
            column = randint(0, self.grid_size-1)
            if not self.grid[row][column] == 'X':
                self.grid[row][column] = 'X'
                return row, column

    def _is_valid_bound(self, row: int, column: int):
        valid_row = row >= 0 and row < self.grid_size
        valid_column = column >= 0 and column < self.grid_size
        return valid_row and valid_column

    def _populate_numbers(self, row: int, column: int):
        around_coordinates = [
            [row-1, column-1], [row-1, column], [row-1, column+1],
            [row, column-1], [row, column+1],
            [row+1, column-1], [row+1, column], [row+1, column+1]
        ]
        for r, c in around_coordinates:
            if self._is_valid_bound(r, c) and not self.grid[r][c] == 'X':
                self.grid[r][c] += 1 

    def populate_grid(self):
        for _ in range(self.n_mines):
            mine_row, mine_column = self._populate_mine()
            self._populate_numbers(mine_row, mine_column)

    def open_point(self, row, column):
        return self.grid[row][column]
