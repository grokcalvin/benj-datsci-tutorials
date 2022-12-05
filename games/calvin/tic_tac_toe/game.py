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
        #a tag system from the class GameState
        self.state = GameState.START
        self.current_player = Player.NA

    def validate_move(self, player, pos: POS) -> MoveState:
        # make sure all move inputs are valid
        if player == Player.NA:
            state = GameState.INVALID_MOVE

        #this should never happen because output has already been filtered
        elif pos not in self.board:
            state = MoveState.INVALID_POSITION

        #self.board?
        elif not self.board[pos] == Player.NA:
            state = MoveState.TAKEN
        #same as
        #elif not dictionary[key] == "-"
        #   output = MoveState.TAKEN


        else: #this returns a string from the MoveState
            state = MoveState.VALID

        return state

    #this will test if a player can replace a "-" value and for test for wins
    def move(self, player: Player, pos: POS) -> MoveState:
        # validate move before making it
        #self refers to the object.method
        #move_state = tag after tests conditions
        move_state = self.validate_move(player, pos)
        #imagine a tag system

        #move_state = function_within_class(typical_value,typical_value)

        
        #uses same values acrross lots of functions

        # do an "early return" if the move state is not valid
        #this end the function before it can run the rest, IF ITS a invalid move
        #executes on no tag
        #validate move is blocks of code that have specific outputs
        if move_state != MoveState.VALID:
            return move_state

        # Since the move is valid, let's play the game
        self.state = GameState.NO_WIN  # assume no wins or ties before checking
        self.current_player = player #this comes from a for loop where X and O are in a list being iterated through via for loop
        #self.board is defined on init on the TicTackToe board
        #this index key's value now = the current player selected
        self.board[pos] = player

        #this scans though tuples containing 3 elements each, each element is a index of the board dictionary. You can break down "win" to access its elements as seen in the list comprehension
        for win in POSSIBLE_WINS:
            #breaks down and tests elements using min and True False values from "operators?"
            owns = [self.board[pos] == self.current_player for pos in win]
            player_wins = min(owns)
            #if 1 then go, if statements look for true or false values that you can just hand it directly
            if player_wins:
                self.state = GameState.WIN
                return move_state

            #changes more than the return value

        # are there any moves left?
        #values makes an iterable of just values of all the keys
        if Player.NA not in self.board.values():
            self.state = GameState.TIE

        return move_state