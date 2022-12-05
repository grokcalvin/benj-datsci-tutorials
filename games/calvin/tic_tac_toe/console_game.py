
from game import TicTacToe, POS, Player, GameState, MoveState


def print_board(game):
    print(' 123')
    #game.ypos = hard coded values or relative values from board?
    for y in game.ypos:
        line = y
        #game.ypos = hard coded values or relative values from board?
        #hard coded values, the same place that all the values are built from
        #this is an index system to print the board, using variables in POS class as indexes
        #make your down index system using a hard coded data set.
        #
        #it is a dictionary hard coded in from the modul
        for x in game.xpos:
            pos = POS(x=x, y=y)
            line = line + game.board[pos].value
            #make a engine with this ----------------------------------------------------------------------------------------
            #make it any size and render.
            #print(game.board)
        print(line)

#where does player come from?
def get_pos(player):
    """
    Valiate player inputs, and return a POS instance(specific object from class) if possible
    """
    pos = None
    move = input(f"Player {player.value} make your move!:").lower()
    #indexes the input and assigns values to 2 variables at once
    #be careful when programming and appeal to rules and conventions
    x1, y1 = move[:1], move[1:2]
    y2, x2 = move[:1], move[1:2]

    try:
        #needs a type conversion
        #assigns an index as POS to remember for later
        pos = POS(x=int(x1), y=y1)
    except Exception as e:
        #nested try, ---- try if exception IMPORTANT 
        try:
            # try it backwards just in case the user reversed arguments (IF FAIL try other way)
            pos = POS(x=int(x2), y=y2)
        except Exception as e:
            print(f"position input '{move}' is board invalid, try again!")
            #returns a POS index meant for board indexing
            #returns none if both tries fail
    return pos


#game with a TicTackToe output, what does this mean? or default values = TicTacToe
#classifing the type the game must be, it must be a TicTacToe
def make_move(game: TicTacToe, player: Player):
    pos = None
    #loop to ensure output
    #only stops when you have an output to return
    while True:
        pos = get_pos(player) # keep trying this until we get a valid position, seeking a user input
        if pos is not None:
            #seeks output of game.move using the input of user and player type moving from for loop
            #all based arround for board
            #game must be predefined in whatever scope you are using this function
            move_state = game.move(player=player, pos=pos)
            if move_state == MoveState.VALID:
                return move_state
            else:
                #move state.value whole class gets updated when running
                print(move_state.value)



def main():
    game = TicTacToe()
    print("valid inputs are XY coordinates, e.g. 1a, a1, b2, 2c.")
    while True:
        #this is where the player variable comes from
        for player in [Player.X, Player.O]:
            print_board(game)
            make_move(game, player)
            #validates, and then actually replaces the board value if validation is passed, accepts inputs converted to index of POS, which is used to reference and index the board dictionary. When you move it will also check for wins and this whole thing will loop over bother player types forever until Game state equals TIE or WIN, never equals lose, becuase its only concerned about someone winning not someone losing.
            #GameState is a list of tags.
            #TicTackToe class with all its functions = game. when and instance is initiated it generates a fresh board.
            if game.state == GameState.WIN:
                #current_player us defined in the move function in the game modul
                print(f"Player {game.current_player.name} has Won!")
                print_board(game)
            else:
                print(game.state.value)

            #if tag is either this or that
            #if either of these two are met then it will have already given output based on results.
            if game.state in [GameState.WIN, GameState.TIE]:
                #ends the while statement
                return

if __name__ == '__main__':
    main()
