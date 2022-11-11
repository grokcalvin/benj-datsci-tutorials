from game import TicTacToe, POS, Player, GameState
import unittest


# Logic to define the possible wins
def possible_wins():
    possible_wins = []
    # won a row? 
    rows =[tuple(POS(x=x, y=y) for x in TicTacToe.xpos) for y in TicTacToe.ypos]
    possible_wins.extend(list(rows))
    # won a column? 
    columns =[tuple(POS(x=x, y=y) for y in TicTacToe.ypos) for x in TicTacToe.xpos]
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

    def test_all_possible_wins(self):
        expected_states = [GameState.NO_WIN, GameState.NO_WIN, GameState.WIN]

        for win in possible_wins():
            for player in Player:
                if player != Player.NA:
                    game = TicTacToe()
                    for pos, expected_state in zip(win, expected_states):
                        game.move(player, pos)
                        
                    self.assertEqual(expected_state, game.game_state)

if __name__ == '__main__':
    unittest.main()




