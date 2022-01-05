from display import Display

grid = int(input("Enter the size of the minesweeper board: "))
game = Display(grid)
print('MINESWEEPER')
print('Press Ctrl+C to exit')
game.start_game()
game.show_game()

while not game.is_done():
    try:
        r, c = game.get_input()
        game.play(r, c)
    except ValueError as e:
        print(e)
