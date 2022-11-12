from games.calvin.tic_tac_toe.game_with_functions import Player, XPOS, YPOS, POS, possible_wins, START_BOARD
from enum import Enum
from pprint import pprint
import random
from copy import deepcopy


A = {'board_state': [
                     [1, 4, 5], 
                     [-5, 8, 9]
                     ]}

# doesn't work
B = A.copy()
# does work
B = deepcopy(A)

B['board_state'].append(['foo', 'bar', 1])

pprint(A)


