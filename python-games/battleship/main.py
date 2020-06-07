from battleship import Battleship

print("Welcome to Battleship")
print("Enter the size of grid:", end="  ")
size = int(input())

bs = Battleship(size)
bs.start_game()

while not bs.is_game_over():
    bs.turn()

if bs.is_won():
    print("You won")
else:
    print("You lost")
