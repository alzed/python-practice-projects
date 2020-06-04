from mastermind import Mastermind

print("Enter the size of the game:", end="  ")
size = int(input())

mm = Mastermind(size)
mm.declare_pegs()

game = mm.game_over
while not game:
    guess = mm.ask_user()
    mm.print_matches(guess)
    game = mm.game_over
print("You won")
    