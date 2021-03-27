import urllib3
from random import choice

class Hangman:
    def __init__(self, length):
        self.length = length
        self.secret_word = ""
        self.guess_word = ['_'] * self.length
        self.attempted_chars = []
        self.remaining_guesses = self.length

    def random_word(self):
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        http = urllib3.PoolManager()
        response = http.request('GET', word_site)
        raw_words = response.data.split()
        words = list(filter(lambda w: len(w) == self.length, raw_words))
        self.secret_word = choice(words).decode('utf-8')

    def is_already_attempted(self, char):
        return char in self.attempted_chars

    def get_matching_indices(self, char):
        return [i for i in range(self.length) if self.secret_word[i] == char]

    def fill_indices(self, char, indices):
        for i in indices:
            self.guess_word[i] = char

    def try_guess(self, char):
        if self.is_already_attempted(char):
            print("You've already guessed this letter.")
            return False
        elif char in self.secret_word:
            self.attempted_chars.append(char)
            indices = self.get_matching_indices(char)
            self.fill_indices(char, indices)
            return True
        else:
            self.attempted_chars.append(char)
            self.remaining_guesses -= 1
            print(f"Wrong guess. You have {self.remaining_guesses} guess remaining")
            return False

    def ask_player(self):
        print('Enter a character:', end='  ')
        return input()

    def is_won(self):
        return self.secret_word == ''.join(self.guess_word)

    def is_lost(self):
        return self.remaining_guesses == 0

    def is_gameover(self):
        return self.is_won() or self.is_lost()
        