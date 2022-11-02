
from game import START_BOARD, Player, POS, tictactoe
import unittest


class TestTicTacToe(unittest.TestCase):
    board = START_BOARD

    def test_row_win(self):
        win = ((1, 'a'), (1, 'b'), (1, 'c'))
        for player in Player:
            board = self.board.copy()
            for x, y in win:
                board, player_won = tictactoe(board, player=player, pos=POS(x=x, y=y))

            self.assertTrue(player_won)

    def test_column_win(self):
        win = ((1, 'a'), (2, 'a'), (3, 'a'))
        for player in Player:
            board = self.board.copy()
            for x, y in win:
                board, player_won = tictactoe(board, player=player, pos=POS(x=x, y=y))

            self.assertTrue(player_won)

    def test_down_diag_win(self):
        win = ((1, 'a'), (2, 'b'), (3, 'c'))
        for player in Player:
            board = self.board.copy()
            for x, y in win:
                board, player_won = tictactoe(board, player=player, pos=POS(x=x, y=y))

            self.assertTrue(player_won)

    def test_up_diag_win(self):
        win = ((3, 'c'), (2, 'b'), (1, 'a'))
        for player in Player:
            board = self.board.copy()
            for x, y in win:
                board, player_won = tictactoe(board, player=player, pos=POS(x=x, y=y))

            self.assertTrue(player_won)

if __name__ == '__main__':
    unittest.main()




