import unittest
import mock

from tic_tac_toe_game import check_score, insert_player


class TestCheckScore(unittest.TestCase):

    def test_game_in_progress(self):
        boards = [
            [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            [[' ', 'O', ' '], [' ', ' ', 'O'], ['X', ' ', ' ']],
            [['X', 'X', ' '], ['X', 'O', 'O'], ['O', 'O', 'X']],
        ]

        for board in boards:
            is_winner, who_won = check_score(board)
            self.assertFalse(is_winner)
            self.assertIsNone(who_won)

    def test_weve_got_a_winner(self):
        boards_x = [
            [['X', ' ', ' '], [' ', 'X', 'O'], [' ', ' ', 'X']],
            [['O', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']],
            [[' ', 'X', ' '], [' ', 'X', ' '], ['O', 'X', ' ']],
            [[' ', 'O', ' '], ['X', 'X', 'X'], ['O', ' ', ' ']],
        ]

        boards_o = [
            [['O', ' ', ' '], [' ', 'O', 'X'], [' ', ' ', 'O']],
            [['X', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', ' ']],
            [[' ', 'O', ' '], [' ', 'O', ' '], ['X', 'O', ' ']],
            [[' ', 'X', ' '], ['O', 'O', 'O'], ['X', ' ', ' ']],
        ]

        for board in boards_x:
            is_winner, who_won = check_score(board)
            self.assertTrue(is_winner)
            print(board, who_won)
            self.assertEqual(who_won, "X")

        for board in boards_o:
            is_winner, who_won = check_score(board)
            self.assertTrue(is_winner)
            self.assertEqual(who_won, "O")

    def test_no_winner(self):
        boards = [
            [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']],
            [['O', 'X', 'X'], ['X', 'O', 'O'], ['O', 'O', 'X']]
        ]

        for board in boards:
            is_winner, who_won = check_score(board)
            self.assertFalse(is_winner)
            self.assertIsNone(who_won)



draw_a_board_game_mock = mock.Mock()


class TestInsertPlayer(unittest.TestCase):

    @mock.patch('tic_tac_toe_game.draw_a_board_game', draw_a_board_game_mock)
    def test_insert_ok(self):
        b1 = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        coords = '1,2'
        player = 'O'
        inserted = insert_player(b1, coords, player)
        self.assertTrue(inserted)
        self.assertEqual(b1[0][1], player)

        b2 = [[' ', 'O', 'X'], ['X', ' ', 'O'], ['O', ' ', ' ']]
        coords = '3, 3'
        player = 'X'
        inserted = insert_player(b2, coords, player)
        self.assertTrue(inserted)
        self.assertEqual(b2[2][2], player)

    def test_insert_not_ok(self):
        b1 = [[' ', 'X', ' '], ['O', 'X', ' '], [' ', 'O', ' ']]
        coords = '1,2'
        player = 'O'
        inserted = insert_player(b1, coords, player)
        self.assertFalse(inserted)
        self.assertEqual(b1[0][1], 'X')

        b2 = [[' ', 'O', 'X'], ['X', ' ', 'O'], ['O', ' ', 'X']]
        coords = '3, 3'
        player = 'X'
        inserted = insert_player(b2, coords, player)
        self.assertFalse(inserted)
        self.assertEqual(b2[2][2], "X")
