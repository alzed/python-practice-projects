from tictactoe import Gameboard

def player():
    print('Enter points: ', end=' ')
    r, c  = map(int, input().split())
    if game.check_pos(r-1, c-1):
        game.set_pos(xo, r-1, c-1)
    else:
        print('Invalid move. Try again.')
        game.display_board()
        player()
    game.display_board()

def computer():
    game.play()
    game.display_board()

game = Gameboard()
print('Choose x or o: ', end=' ')
xo = input()
x = game.choose_symbol(xo)
if x:
    game.display_board()
    player()
    for _ in range(4):
        computer()
        result = game.check_wins()
        if result in ['won', 'lost']:
            print(f'You {result}. Game over')
            break
        player()
        result = game.check_wins()
        if result in ['won', 'lost']:
            print(f'You {result}. Game over')
            break
    else:
        print('Game draw')
else:
    computer()
    for _ in range(4):
        player()
        result = game.check_wins()
        if result in ['won', 'lost']:
            print(f'You {result}. Game over')
            break
        computer()
        result = game.check_wins()
        if result in ['won', 'lost']:
            print(f'You {result}. Game over')
            break
    else:
        print('Game draw')
