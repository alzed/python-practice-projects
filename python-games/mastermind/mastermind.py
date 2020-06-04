from code import Code

class Mastermind:
    def __init__(self, number):
        self.length = number
        self._secret_code = Code.generate_secret_code(self.length)
        self.game_over = False

    def declare_pegs(self):
        possible_pegs = Code.possible_pegs[:self.length]
        print(f"Possible letters of secret code: {', '.join(possible_pegs)}")

    def ask_user(self):
        print("Type your guess:", end="  ")
        try:
            guess = Code(input(), self.length)
            return guess
        except ValueError as err:
            print(f"{err}. Try again.")
            return self.ask_user()

    def print_matches(self, code):
        exact, near = code.get_matches(self._secret_code)
        self.game_over = self.is_game_over(exact)
        print(f"Exact matches: {exact}")
        print(f"Near matches: {near}")

    def is_game_over(self, exact):
        return True if exact == self.length else False
