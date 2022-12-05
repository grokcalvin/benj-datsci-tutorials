import dataclasses

#pos, player
#generate dictionary board

@dataclass(frozen=true,eq=Tr)
class POS():
    x:int
    y:int

class Player():
    O ="O"
    X = "X"
    NA = "-"

class GameState():
    Win = "WinState"
    Tie = "TieState"
    Start = "StartState"


class MoveState():
    Valid = "Valid Position"
    InValid = "Invalid Position"


class tic_tac_toe():
    X_Lable = ["a","b","c"]
    Y_Lable = [1,2,3]

    def __init__(self):
        self.board = {POS(x,y):Player.NA for y in range(3) for x in range(3)}
        self.state = GameState.Start

    def validate_move(self,pos:POS,player:Player):
        state = "unknown"
        if self.board[pos] == Player.NA:
            state = GameState.Clear
            return state
        if pos not in self.board.keys:
            state = GameState.Taken
            return state
        #what other outcomes are there?
        #invalue position?
        #is this covered when you get a move which is in move while loop until valid move is found


        #see if there is a spot open
        #see other possiblities and return a state variable

#

    def move(self,pos:POS,player:Player) -> POS:
        #PRINT BOARD IS BEFORE THIS
        while True:
            input1 = input("Player {}, input X,Y, Example 13".format(player))
            x = input1[0:1]
            y = input1[1:2]
            state = self.validate_move(POS(x,y),player)
            if state == "Valid Position":
                return POS(x,y)
            if state != "Valid Position":
                print(state)

    def print_board():
        print(
        for y in Y_Lable:


#rename a class by putting it in a instance

#input and swap the two chacters to find the correct order

#within a for loop change the player variable



#what needs to happen?
#there needs to a board
#there needs to be a move based on the input of the player, this needs to alternate which will be in a for while that is in a while loop that is testing for the GameState of the class.
#every move needs to be comfirmed to be a good move and

#initiation need to set the State to start and create a blank board
#every time the game loops over to get a players move and inputs it, it generates a new board 
#INPUTS NEED TO BE VALIDATED