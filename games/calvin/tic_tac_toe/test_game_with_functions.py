from game_with_functions import START_BOARD, Player, POS, tictactoe, XPOS, YPOS
import unittest


def possible_wins():
    possible_wins = []
    # won a row? 
    rows =[tuple(POS(x=x, y=y) for x in XPOS) for y in YPOS]
    possible_wins.extend(list(rows))
    # won a column? 
    columns =[tuple(POS(x=x, y=y) for y in YPOS) for x in XPOS]
    possible_wins.extend(list(columns))
    # won down diagonal? 
    down_diag = [
        POS(x=1, y='a'),
        POS(x=2, y='b'),
        POS(x=3, y='c'),
    ]
    possible_wins.append(down_diag)
    # won up diagonal? 
    up_diag = [
        POS(x=1, y='c'),
        POS(x=2, y='b'),
        POS(x=3, y='a'),
    ]
    possible_wins.append(down_diag)
    return possible_wins


class TestTicTacToe(unittest.TestCase):
    board = START_BOARD

    def test_all_possible_wins(self):
        for win in possible_wins():
            for player in Player:
                if player != Player.NA:
                    board = self.board.copy()
                    for pos in win:
                        board, player_won = tictactoe(board, player=player, pos=pos)
                    self.assertTrue(player_won)

if __name__ == '__main__':
    unittest.main()




