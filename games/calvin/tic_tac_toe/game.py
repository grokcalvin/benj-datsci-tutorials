from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class POS:
    """
    Defines each board position.  See TicTacToe class for valid x and y positions. 
    """
    x: int
    y: str


# See unit test for how these were produced
POSSIBLE_WINS = [
    (POS(x=1, y='a'), POS(x=2, y='a'), POS(x=3, y='a')),
    (POS(x=1, y='b'), POS(x=2, y='b'), POS(x=3, y='b')),
    (POS(x=1, y='c'), POS(x=2, y='c'), POS(x=3, y='c')),
    (POS(x=1, y='a'), POS(x=1, y='b'), POS(x=1, y='c')),
    (POS(x=2, y='a'), POS(x=2, y='b'), POS(x=2, y='c')),
    (POS(x=3, y='a'), POS(x=3, y='b'), POS(x=3, y='c')),
    [POS(x=1, y='a'), POS(x=2, y='b'), POS(x=3, y='c')],
    [POS(x=1, y='a'), POS(x=2, y='b'), POS(x=3, y='c')]
]


class Player(Enum):
    X = 'X'
    O = 'O'
    NA = '-'


class GameState(Enum):
    START = 'The game is afoot!'
    WIN = 'The game has been won!'
    NO_WIN = 'No win yet, keep playing!'
    INVALID_MOVE = "Cannot make that move"
    TIE = 'The game is tied!'


class MoveState(Enum):
    VALID = 'valid move'
    TAKEN = 'That position is taken, try again'
    INVALID_POSITION = 'Invalid position, try again'
    INVALID_PLAYER = 'Invalid player, what are you doing?'



class TicTacToe:
    xpos = (1, 2, 3)
    ypos = ('a', 'b', 'c')

    def __init__(self) -> None:
        self.board = {POS(x, y): Player.NA for y in self.ypos for x in self.xpos}
        self.state = GameState.START
        self.current_player = Player.NA

    def validate_move(self, player, pos: POS) -> MoveState:
        # make sure all move inputs are valid
        if player == Player.NA:
            state = GameState.INVALID_MOVE
        elif pos not in self.board:
            state = MoveState.INVALID_POSITION
        elif not self.board[pos] == Player.NA:
            state = MoveState.TAKEN
        else:
            state = MoveState.VALID

        return state

    def move(self, player: Player, pos: POS) -> MoveState:
        # validate move before making it
        move_state = self.validate_move(player, pos)
        # do an "early return" if the move state is not valid
        if move_state != MoveState.VALID:
            return move_state

        # Since the move is valid, let's play the game
        self.state = GameState.NO_WIN  # assume no wins or ties before checking
        self.current_player = player
        self.board[pos] = player

        for win in POSSIBLE_WINS:
            owns = [self.board[pos] == self.current_player for pos in win]
            player_wins = min(owns)
            if player_wins:
                self.state = GameState.WIN
                return move_state

        # are there any moves left?
        if Player.NA not in self.board.values():
            self.state = GameState.TIE

        return move_state