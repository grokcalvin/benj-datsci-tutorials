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
    TIE = 'The game is tied!'



class TicTacToe:
    xpos = (1, 2, 3)
    ypos = ('a', 'b', 'c')

    def __init__(self) -> None:
        self.board = {POS(x, y): Player.NA for y in self.ypos for x in self.xpos}
        self.game_state = GameState.START
        self.current_player = Player.NA


    def update_game_state(self) -> None:
        self.game_state = GameState.NO_WIN # assume no wins or ties before checking
  
        for win in POSSIBLE_WINS:
            owns = [self.board[pos] == self.current_player for pos in win]
            player_wins = min(owns)
            if player_wins:
                self.game_state = GameState.WIN
                break

        # are there any moves left? 
        if Player.NA not in self.board.values():
            self.game_state = GameState.TIE


    def move(self, player: Player, pos: POS):
        assert pos in self.board # make sure position is valid
        assert player != Player.NA # make sure the player is valid 
        assert self.board[pos] == Player.NA  # make sure that position is not already taken
        self.current_player = player
        self.board[pos] = player
        self.update_game_state()
