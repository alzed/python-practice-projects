from random import randint

class GuessingGame:
    def __init__(self, min_num, max_num):
        self._min = min_num
        self._max = max_num
        self._secret_number = randint(self._min, self._max)
        self.gameover = False
        self.num_attempts = 0
        
    def ask_number(self):
        self.num_attempts += 1
        print("Guess a number:", end="  ")
        return int(input())

    def check_number(self, number):
        if number < self._secret_number:
            print('Too small')
        elif number > self._secret_number:
            print('Too big')
        else:
            self.gameover = True
