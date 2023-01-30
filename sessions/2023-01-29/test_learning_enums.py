from learning_enums import moves, Move, Item


def test_learning_success():
    valid_moves = [
        (Move.ATTACK, Item.SWORD),
        (Move.DEFEND, Item.SWORD),
        (Move.DEFEND, Item.SHIELD),
    ]
    for move, item in valid_moves:
        moves(move=move, item=item)


def test_learning_enum_fail():
    invalid_moves = [
        (Move.ATTACK, Item.APPLE)
    ]
    for move, item in invalid_moves:
        
        try:
            moves(move=move, item=item)
            to_pass = False
        except ValueError:
            to_pass = True
        
        assert to_pass


def main():
    test_learning_success()
    test_learning_enum_fail()


if __name__ == '__main__':
    main()
