import random

win = False
board2 = ["---","---","---"]
print(f" 123\na{board2[0]}\nb{board2[1]}\nc{board2[2]}")
while win == False:
#display board
#  print(f" 123\na{board2[0]}\nb{board2[1]}\nc{board2[2]}")
#  print(board2[0][0])
#edit board
  continue1 = False
  while continue1 == False:
    Turn = "X"
    edit = input("input letter followed by a space and a number to select an empty space to place an {}:".format(Turn))
    y,x = tuple(edit.split(" "))
    x = int(x) - 1
#    print(str(x))
#    print(str(y))

    if y == "a":
      y = 0
    if y == "b":
      y = 1
    if y == "c":
      y = 2

  #feedback if location is taken
    if board2[y][x] != "-":
      print("\nthis slot is taken try again")
    else:
      if x == 0:
        print(board2[y][2])
        board2[y] = Turn+board2[y][1]+board2[y][2]
      if x == 1:
        board2[y] = board2[y][0]+Turn+board2[y][2]
      if x == 2:
        board2[y] = board2[y][0]+board2[y][1]+Turn
      continue1 = True
    print(f"\nYour Move\n 123\na{board2[0]}\nb{board2[1]}\nc{board2[2]}")






#win detection
  #cylces through up and down wins
  x,y= 0,0
  for i in range(3):
    comfirmed_win = 0


    for iii in range(3):
      if board2[y][x] == Turn:
        comfirmed_win +=1
        y +=1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True
    x += 1
    y = 0

  #cylces through left and right wins wins
  x,y= 0,0
  for i in range(3):
    comfirmed_win = 0

    for iii in range(3):
      if board2[y][x] == Turn:
        comfirmed_win +=1
        x +=1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True
    y += 1
    x = 0


  #cycles through diagonals
  x,y= 0,0
  comfirmed_win = 0
  for i in range(3):
    if board2[y][x] == Turn:
      comfirmed_win +=1
    x += 1
    y += 1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True

  x,y= 0,2
  comfirmed_win = 0
  for i in range(3):
    if board2[y][x] == Turn:
      comfirmed_win +=1
    x += 1
    y -= 1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True
  
  if win == True:
    break

#detects draw
  y = 0
  draw = True
  for i in range(3):
    if "-" in board2[y]:
      draw = False
    y += 1
  if draw == True:
    input1 = input("it's a draw! would you like to try again? y/n:")
    if input1 =="y":
      board2 = ["---","---","---"]
      print("Board reset!")
      print((f"\nNew Board\n 123\na{board2[0]}\nb{board2[1]}\nc{board2[2]}"))
    if input1 =="n":
      win = True
      print("Thanks for playing!")
      break

#enemy move
  Turn = "O"
  open_moves = []
  y = 0
  x = 0
  for i in board2:
    for iii in i:
      if iii == "-":
        open_moves.append((y,x))
      x += 1
    x = 0
    y += 1
#    print(open_moves)
  
  random_move = open_moves[random.randint(0,(len(open_moves)-1))]
#  print(random_move)
  y,x = random_move
  if x == 0:
    print(board2[y][2])
    board2[y] = Turn+board2[y][1]+board2[y][2]
  if x == 1:
    board2[y] = board2[y][0]+Turn+board2[y][2]
  if x == 2:
    board2[y] = board2[y][0]+board2[y][1]+Turn

  print(f"\nOpponent's Move\n 123\na{board2[0]}\nb{board2[1]}\nc{board2[2]}")

#win detection
  #cylces through up and down wins
  x,y= 0,0
  for i in range(3):
    comfirmed_win = 0


    for iii in range(3):
      if board2[y][x] == Turn:
        comfirmed_win +=1
        y +=1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True
    x += 1
    y = 0

  #cylces through left and right wins wins
  x,y= 0,0
  for i in range(3):
    comfirmed_win = 0

    for iii in range(3):
      if board2[y][x] == Turn:
        comfirmed_win +=1
        x +=1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True
    y += 1
    x = 0


  #cycles through diagonals
  x,y= 0,0
  comfirmed_win = 0
  for i in range(3):
    if board2[y][x] == Turn:
      comfirmed_win +=1
    x += 1
    y += 1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True

  x,y= 0,2
  comfirmed_win = 0
  for i in range(3):
    if board2[y][x] == Turn:
      comfirmed_win +=1
    x += 1
    y -= 1
    if comfirmed_win == 3:
      print("{} has Won!".format(Turn))
      win = True
  
  if win == True:
    break

  #a notifier saying your out of moves, its a draw
  y = 0
  draw = True
  for i in range(3):
    if "-" in board2[y]:
      draw = False
    y += 1
  if draw == True:
    input1 = input("it's a draw! would you like to try again? y/n:")
    if input1 =="y":
      board2 = ["---","---","---"]
      print("Board reset!")
      print((f"\nNew Board\n 123\na{board2[0]}\nb{board2[1]}\nc{board2[2]}"))
    if input1 =="n":
      win = True
      print("Thanks for playing!")
      break