from learning_enums import VALID_MOVES, Item, Move

"""
Example 1
"""

try:
    print(VALID_MOVES[Item.NULL])
except:
    print('bad move!')

print(VALID_MOVES.get(Item.NULL, 'bad move!'))


"""
Example 2
"""
try:
    if Move.ATTACK in VALID_MOVES[Item.NULL]:
        print('good move!')
except:
    print('bad move!')



# if Move.ATTACK in VALID_MOVES[Item.NULL]:
#     print('good move!')


if Move.ATTACK in VALID_MOVES.get(Item.NULL, []):
    print('good move!')
else:
    print('bad move!')
