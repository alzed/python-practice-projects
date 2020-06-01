from random import choices

class Code:
    possible_pegs = ['R', 'G', 'B', 'Y', 'V', 'O', 'I']

    @classmethod
    def generate_secret_code(cls, length):
        return cls(Code.random(length), length)

    def __init__(self, code, number):
        if self.is_valid(code, number):   
            self.length = number
            self.code = code
            self.pegs = list(self.code)

    def is_valid(self, code, number):
        if len(code) == number:
            if all(map(lambda a: a in self.possible_pegs[:number], code)):
                return True
            else:
                print(f'Should contain self.possible')


    def get_matches(self, code):
        exact_matches = 0
        near_matches = 0
        for i,j in zip(self.code, code.code):
            if i == j:
                exact_matches += 1
            elif i in code.code:
                near_matches += 1
        return exact_matches, near_matches

    @staticmethod
    def random(number):
        return choices(Code.possible_pegs, k=number)  
