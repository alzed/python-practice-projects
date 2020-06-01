from code import Code

class Mastermind:
    def __init__(self, number):
        self.length = number
        self._secret_code = Code.generate_secret_code(self.length)

    def print_matches(self, code):
        exact, near = code.get_matches(self._secret_code)
        return exact, near

    def ask_user(self):
        print("Type your guess:", end="  ")
        guess = Code(input(), self.length)
        print(guess.code)
