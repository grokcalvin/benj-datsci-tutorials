from pprint import pprint
from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True,eq=True)
class POS:
    x : int
    y : int

object1 = POS(1,2)
pprint(object1.y)
board = {}

class player(Enum):
    background = "O"
    player = "P"

X_Range, Y_Range = int(input("X value:")), int(input("Y value:"))
for x in range(X_Range):
    for y in range(Y_Range):
        #how is data stored? is it as a player.background path, or is it the value of player.background.
        board[POS(x,y)] = player.background

top_line = ""
for x in range(X_Range):
    top_line = top_line + str(x)

side_line = ""
for y in range(Y_Range):
    side_line = side_line + str(y)

print(top_line)
for Y in range(len(side_line)):
    y_strip = ""
    for X in range(len(top_line)):
                            #cant concatanate player with string
        y_strip = y_strip + board[POS(int(x),int(y))].value
    print(y + y_strip)

#print(board)

#print(board[POS(1,3)])

#the consol game uses tags memory in the form of a class that has variables equalling strings.