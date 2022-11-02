
from game import START_BOARD, Player, POS, tictactoe, YPOS, XPOS


def print_board(board):
    print(' 123')
    for y in YPOS:
        line = y
        for x in XPOS:
            pos = POS(x=x, y=y)
            line = line + board[pos].value
        print(line)


def get_move(board, player: Player):
    pos = None
    while True:
        move = input(f"Player {player.value} make your move!:").lower()
        try:
            x, y = move[:1], move[1:2]
            pos = POS(x=int(x), y=y)
        except Exception as e:
            print(f"move input '{move}' is invalid, try again!")
        if pos is not None:
            if board[pos] != Player.NA:
                print('position is taken, try again!')
            else:
                break

    return pos



def main():

    board = START_BOARD
    print("valid inputs are XY coordinates, e.g. 1a, 3b, 2c.")
    while True:
        for player in [Player.X, Player.O]:
            print_board(board)
            pos = get_move(board, player)
            board, win = tictactoe(board, player, pos)
            if win:
                print(f"Player {player.value} has Won!")
                return

1
if __name__ == '__main__':
    main()
