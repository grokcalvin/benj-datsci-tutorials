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
    possible_wins = []
    # won a row? 
    rows =[tuple(POS(x=x, y=y) for x in XPOS) for y in YPOS]
    possible_wins.extend(list(rows))
    # won a column? 
    columns =[tuple(POS(x=x, y=y) for y in YPOS) for x in XPOS]
    possible_wins.extend(list(columns))
    # won down diagonal? 
    down_diag = [
        POS(x=1, y='a'),
        POS(x=2, y='b'),
        POS(x=3, y='c'),
    ]
    possible_wins.append(down_diag)
    # won up diagonal? 
    up_diag = [
        POS(x=1, y='c'),
        POS(x=2, y='b'),
        POS(x=3, y='a'),
    ]
    possible_wins.append(down_diag)
    return possible_wins


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
