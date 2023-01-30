from enum import Enum

class Item(Enum):
    SWORD = 'sword'
    SHIELD = 'shield'
    APPLE = 'apple'
    NULL = 'Bad'

class Move(Enum):
    ATTACK = 'attacking'
    DEFEND = 'defending'
    EAT = 'eating'


VALID_MOVES = {
    Item.SWORD: [
        Move.ATTACK,
        Move.DEFEND
    ],
    Item.SHIELD: {
        Move.DEFEND
    },
    Item.APPLE: [
        Move.EAT
    ]
}


VERB_OVERRIDE = {
    Item.APPLE: {
        Move.EAT: 'an'
    }
}

def string_moves(move: str, item: str):
    print(f"{move} with {item}")


def moves(move: Move, item: Item):
    verb = VERB_OVERRIDE.get(item, {}).get(move, 'with')
    if move in VALID_MOVES[item]:
        print(f"{move.value} {verb} {item.value}")
    else:
        raise ValueError("Invalid Move")


def main():
    bad_move = string_moves(move="attack", item="apple")
    try:
        bad_move = moves(move=Move.ATTACK, item=Item.APPLE)
    except Exception:
        print('bad move!!')
    
    moves(Move.EAT, Item.APPLE)
    moves(Move.ATTACK, Item.SWORD)





if __name__ == '__main__':
    main()
