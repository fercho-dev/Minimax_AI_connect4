import unittest
import numpy as np
from ai import Minimax_AI


class TestAI(unittest.TestCase):

    def setUp(self):
        self.ai = Minimax_AI(4, 2, 6, 7)

    def tearDown(self):
        pass

    def test_depth(self):
        self.assertEqual(self.ai.depth, 4)

    def test_player(self):
        self.assertEqual(self.ai.player, 2)

    def test_board_rows(self):
        self.assertEqual(self.ai.board_rows, 6)

    def test_board_columns(self):
        self.assertEqual(self.ai.board_columns, 7)

    def test_is_endgame(self):
        winning_board_vertical1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0],
            [0, 2, 0, 1, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [0, 2, 1, 1, 2, 0, 0]
        ]
        winning_board_vertical2 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 2, 0, 0, 0],
            [0, 1, 0, 2, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [0, 1, 2, 2, 1, 0, 0]
        ]
        winning_board_horizontal1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 2, 0],
            [0, 2, 1, 1, 1, 1, 0],
            [0, 1, 2, 2, 1, 1, 0]
        ]
        winning_board_horizontal2 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0],
            [0, 1, 2, 2, 2, 2, 0],
            [0, 2, 1, 1, 2, 2, 0]
        ]
        winning_board_pslope1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 2, 1, 0],
            [0, 0, 1, 1, 2, 2, 0],
            [0, 0, 2, 1, 1, 2, 0]
        ]
        winning_board_pslope2 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 2, 2, 0],
            [0, 0, 0, 2, 1, 2, 0],
            [0, 0, 2, 2, 1, 1, 0],
            [0, 0, 1, 2, 2, 1, 0]
        ]
        winning_board_nslope1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [0, 2, 1, 2, 1, 1, 0]
        ]
        winning_board_nslope2 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [0, 1, 2, 1, 2, 2, 0]
        ]
        no_winning_board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [0, 2, 1, 1, 0, 0, 0],
            [2, 2, 1, 2, 1, 0, 0]
        ]
        self.assertTrue(self.ai._is_endgame(winning_board_horizontal1, 1))
        self.assertTrue(self.ai._is_endgame(winning_board_horizontal2, 2))
        self.assertTrue(self.ai._is_endgame(winning_board_vertical1, 1))
        self.assertTrue(self.ai._is_endgame(winning_board_vertical2, 2))
        self.assertTrue(self.ai._is_endgame(winning_board_pslope1, 1))
        self.assertTrue(self.ai._is_endgame(winning_board_pslope2, 2))
        self.assertTrue(self.ai._is_endgame(winning_board_nslope1, 1))
        self.assertTrue(self.ai._is_endgame(winning_board_nslope2, 2))
        self.assertIsNone(self.ai._is_endgame(no_winning_board, 1))
        self.assertIsNone(self.ai._is_endgame(no_winning_board, 2))

    def test_to_move(self):
        to_move_1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 2, 0, 0],
            [0, 2, 2, 1, 1, 0, 0]
        ]
        to_move_2 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 2, 0, 1],
            [0, 2, 2, 1, 1, 0, 2]
        ]
        self.assertEqual(self.ai._to_move(to_move_1), 1)
        self.assertEqual(self.ai._to_move(to_move_2), 2)

    def test_actions(self):
        actions7 = [
            [1, 1, 0, 2, 2, 0, 0],
            [0, 2, 0, 1, 2, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        actions5 = [
            [1, 1, 0, 2, 2, 0, 2],
            [2, 2, 0, 1, 2, 0, 2],
            [2, 0, 0, 0, 1, 0, 1],
            [2, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 2]
        ]
        actions1_col1 = [
            [1, 1, 2, 2, 2, 1, 1],
            [1, 2, 2, 1, 2, 1, 2],
            [1, 0, 1, 1, 1, 1, 1],
            [2, 0, 1, 1, 2, 1, 2],
            [2, 0, 1, 2, 2, 1, 1],
            [2, 0, 2, 2, 1, 1, 1]
        ]
        actions0 = [
            [1, 1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1, 2, 1],
            [2, 1, 2, 2, 1, 1, 2],
            [2, 2, 2, 1, 2, 1, 2],
            [1, 2, 2, 2, 1, 1, 1]
        ]
        self.assertEqual(7, len(self.ai._actions(actions7)))
        self.assertEqual(5, len(self.ai._actions(actions5)))
        self.assertEqual(1, len(self.ai._actions(actions1_col1)))
        self.assertIn(1, self.ai._actions(actions1_col1))
        self.assertEqual(0, len(self.ai._actions(actions0)))

    def test_result(self):
        board = [
            [1, 1, 2, 0, 2, 0, 0],
            [0, 2, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        action = 4
        piece = 2
        result_board = [
            [1, 1, 2, 0, 2, 0, 0],
            [0, 2, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(result_board, self.ai._result(board, action, piece))

    def test_is_tie(self):
        tie_board = [
            [1, 2, 1, 1, 1, 2, 2],
            [1, 2, 1, 2, 2, 1, 2],
            [1, 1, 2, 1, 2, 1, 1],
            [2, 1, 2, 1, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 1],
            [2, 2, 1, 2, 1, 1, 2]
        ]
        no_tie_board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [0, 1, 2, 1, 2, 2, 0]
        ]
        self.assertIsNone(self.ai._is_tie(no_tie_board))
        self.assertTrue(self.ai._is_tie(tie_board))

    def test_utility(self):
        tie_board = [
            [1, 2, 1, 1, 1, 2, 2],
            [1, 2, 1, 2, 2, 1, 2],
            [1, 1, 2, 1, 2, 1, 1],
            [2, 1, 2, 1, 1, 2, 1],
            [1, 2, 1, 2, 2, 2, 1],
            [2, 2, 1, 2, 1, 1, 2]
        ]
        opponent_win1 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 2, 1, 0],
            [0, 0, 1, 1, 2, 2, 0],
            [0, 0, 2, 1, 1, 2, 0]
        ]
        player_win2 = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0],
            [0, 1, 2, 2, 2, 2, 0],
            [0, 2, 1, 1, 2, 2, 0]
        ]
        center_column_test = np.array([
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        horizontal_test = np.array([
            [0, 0, 0, 0, 1, 1, 1],
            [0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        vertical_test = np.array([
            [2, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        slope_test = np.array([
            [2, 0, 0, 0, 0, 0, 1],
            [0, 2, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        self.assertEqual(self.ai._utility(tie_board), 0)
        self.assertEqual(self.ai._utility(opponent_win1), -100)
        self.assertEqual(self.ai._utility(player_win2), 100)
        self.assertEqual(self.ai._utility(center_column_test), 3)
        self.assertEqual(self.ai._utility(horizontal_test), -1)
        self.assertEqual(self.ai._utility(vertical_test), -2)
        self.assertEqual(self.ai._utility(slope_test), -3)


if __name__ == '__main__':
    unittest.main()
