
from game import TicTacToe, POS, Player, GameState, MoveState


def print_board(game):
    print(' 123')
    for y in TicTacToe.ypos:
        line = y
        for x in TicTacToe.xpos:
            pos = POS(x=x, y=y)
            line = line + game.board[pos].value
        print(line)


def get_pos(player):
    """
    Valiate player inputs, and return a POS instance if possible
    """
    pos = None
    move = input(f"Player {player.value} make your move!:").lower()
    x1, y1 = move[:1], move[1:2]
    y2, x2 = move[:1], move[1:2]

    try:
        pos = POS(x=int(x1), y=y1)
    except Exception as e:
        try:
            # try it backwards just in case the user reversed arguments
            pos = POS(x=int(x2), y=y2)
        except Exception as e:
            print(f"position input '{move}' is invalid, try again!")
    return pos


def make_move(game: TicTacToe, player: Player):
    pos = None
    while True:
        pos = get_pos(player) # keep trying this until we get a valid position
        if pos is not None:
            move_state = game.move(player=player, pos=pos)
            if move_state == MoveState.VALID:
                return move_state
            else:
                print(move_state.value)



def main():
    game = TicTacToe()
    print("valid inputs are XY coordinates, e.g. 1a, a1, b2, 2c.")
    while True:
        for player in [Player.X, Player.O]:
            print_board(game)
            make_move(game, player)
            if game.state == GameState.WIN:
                print(f"Player {game.current_player.name} has Won!")
                print_board(game)
            else:
                print(game.state.value)

            if game.state in [GameState.WIN, GameState.TIE]:
                return

if __name__ == '__main__':
    main()
