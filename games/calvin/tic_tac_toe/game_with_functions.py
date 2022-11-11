from enum import Enum
from dataclasses import dataclass


class Player(Enum):
    X = 'X'
    O = 'O'
    NA = '-'

XPOS = (1, 2, 3)
YPOS = ('a', 'b', 'c')

@dataclass(frozen=True, eq=True)
class POS:
    x: int
    y: str


START_BOARD = {POS(x, y): Player.NA for y in YPOS for x in XPOS}


def possible_wins():
    ## Truth Table: See unit test for how this was generated
    return [
        (POS(x=1, y='a'), POS(x=2, y='a'), POS(x=3, y='a')),
        (POS(x=1, y='b'), POS(x=2, y='b'), POS(x=3, y='b')),
        (POS(x=1, y='c'), POS(x=2, y='c'), POS(x=3, y='c')),
        (POS(x=1, y='a'), POS(x=1, y='b'), POS(x=1, y='c')),
        (POS(x=2, y='a'), POS(x=2, y='b'), POS(x=2, y='c')),
        (POS(x=3, y='a'), POS(x=3, y='b'), POS(x=3, y='c')),
        [POS(x=1, y='a'), POS(x=2, y='b'), POS(x=3, y='c')],
        [POS(x=1, y='a'), POS(x=2, y='b'), POS(x=3, y='c')]
    ]


def tictactoe(board, player, pos):
    
    def move(board, player, pos: POS):
        assert pos.x in XPOS
        assert pos.y in YPOS
        assert board[pos] == Player.NA
        board[pos] = player
        return board

    def player_wins(board, player) -> bool:
        for possible_win in possible_wins():
            owns = [board[pos] == player for pos in possible_win]
            wins = min(owns)
            if wins:
                return wins

        return False

    board = move(board, player, pos)
    wins = player_wins(board, player)
    return board, wins
