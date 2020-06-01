from mastermind import Mastermind

print("Enter the size of the game:", end="  ")
size = int(input())

mm = Mastermind(size)

game = True
while game:
    guess = mm.ask_user()
    mm.print_matches(guess)
    