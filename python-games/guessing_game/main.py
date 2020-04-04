from guessing_game import GuessingGame

print('GUESSING GAME')

print("Enter a minimum number:", end="  ")
min_num = int(input())
print("Enter a maximum number:", end="  ")
max_num = int(input())

gg = GuessingGame(min_num, max_num)

while not gg.gameover:
    gg.check_number(gg.ask_number())

print(f'Correct. You guessed in {gg.num_attempts} tries.')
