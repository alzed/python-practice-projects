from hangman import Hangman

print("HANGMAN")

print("Enter the word length:", end="  ")
length = int(input())

hm = Hangman(length)
hm.random_word()

print("Try to guess the word:")

while not hm.is_gameover():
    print(' '.join(hm.guess_word))
    char = hm.ask_player()
    if hm.try_guess(char):
        hm.fill_indices(char, hm.get_matching_indices(char))

if hm.is_won():
    print("You won")
else:
    print(f"You failed to guess the word: {hm.secret_word}")
