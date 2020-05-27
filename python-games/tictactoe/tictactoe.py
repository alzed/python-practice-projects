import random

class Gameboard:
    def __init__(self):
        self.n_rows = 3
        self.n_cols = 3
        self.gameboard = [[' ' for c in range(self.n_rows)] for r in range(self.n_cols)]
        self.h_win = [0]*3
        self.v_win = [0]*3
        self.diag = [0]*2
        self.available = ['00', '01', '02', '10', '11', '12', '20', '21', '22']

    def choose_symbol(self, sym):
        self.symbol = sym
        if sym == 'x':
            self.computer = 'o'
            return True
        else:
            self.computer = 'x'
            return False

    def check_pos(self, row, column):
        if str(row)+str(column) in self.available:
            return True
        else:
            return False

    def set_pos(self, symbol, row, column):
        self.gameboard[row][column] = symbol
        self.available.remove(str(row)+str(column))
        val = 1 if symbol == self.symbol else 4
        self.h_win[row] += val
        self.v_win[column] += val
        if row == column:
            self.diag[0] += val
        if [0,1,2].index(row) == [2,1,0].index(column):
            self.diag[1] += val 

    def play(self):
        choice = random.choice(self.available)
        self.set_pos(self.computer, int(choice[0]), int(choice[1])) 

    def check_wins(self):
        if (3 in self.h_win) or (3 in self.v_win) or (3 in self.diag):
            return 'won'
        elif (12 in self.h_win) or (12 in self.v_win) or (12 in self.diag):
            return 'lost'
        else:
            return 'draw'
        
    def display_board(self):
        print('-'*11)
        for r in self.gameboard:
            line = ' | '.join(r)
            print(' ' + line + ' ')
            print('-'*11)
    