import unittest
import random
from gamelogic import Game
from gamelogic import Board
from gamelogic import Card


class TestGamelogic(unittest.TestCase):

    # board and game creation

    def setUp(self):
        random.seed(2)
        self.game = Game(8)

    def test_game_is_created(self):
        self.assertNotEqual(self.game, None)

    def test_game_starts_from_player1(self):
        self.assertEqual(self.game.turn, 1)

    def test_game_points_start_at_0(self):
        self.assertEqual(self.game.points, [0, 0])

    def test_board_is_created(self):
        self.assertNotEqual(self.game.board, None)

    def test_board_is_random(self):
        second_game = Game(8)
        self.assertNotEqual(self.game.board, second_game.board)

    # cards after creating

    def test_the_right_amount_of_cards_is_created(self):
        self.assertEqual(len(self.game.board.cards), 16)

    def test_created_cards_are_not_open(self):
        self.assertEqual(self.game.board.cards[3].open, False)

    def test_cards__are_created_in_pairs(self):
        threes = 0
        for i in self.game.board.cards:
            if i.value == 3:
                threes += 1
        self.assertEqual(threes, 2)

    # card functionality

    def test_cards_can_be_opened(self):
        self.game.board.open_card(2)
        self.assertEqual(self.game.board.cards[2].open, True)

    def test_cards_can_be_closed(self):
        self.game.board.open_card(2)
        self.game.board.close_card(2)
        self.assertEqual(self.game.board.cards[2].open, False)

    # game functionality.
    # 3 and 0 are a pair on the used seed and are used in these tests for pair functionality

    def test_opening_closed_card_returns_true(self):
        self.assertEqual(self.game.open_card(0, False), True)

    def test_opening_closed_card_still_opens_the_card(self):
        self.game.open_card(0, False)
        self.assertEqual(self.game.board.cards[0].open, True)

    def test_opening_open_card_returns_false(self):
        self.game.open_card(0, False)
        self.assertEqual(self.game.open_card(0, False), False)

    def test_opening_when_end_is_false_is_saved(self):
        self.game.open_card(0, False)
        self.assertEqual(self.game.saved, (0, 7))

    def test_opening_when_not_end_isnt_saved(self):
        self.game.open_card(0, True)
        self.assertEqual(self.game.saved, (-1, -1))

    def test_end_changes_player_turns(self):
        self.game.open_card(0, True)
        self.assertEqual(self.game.turn, 2)

    def test_comparing_nonpairs_closes_both_cards(self):
        self.game.open_card(0, False)
        self.game.open_card(1, True)
        values = []
        values.append(self.game.board.cards[0].open)
        values.append(self.game.board.cards[1].open)
        self.assertEqual(values, [False, False])

    def test_comparing_pairs_keeps_them_open(self):
        self.game.open_card(0, False)
        self.game.open_card(3, True)
        values = []
        values.append(self.game.board.cards[0].open)
        values.append(self.game.board.cards[3].open)
        self.assertEqual(values, [True, True])

    def test_comparing_pairs_awards_a_point(self):
        self.game.open_card(0, False)
        self.game.open_card(3, True)
        self.assertEqual(self.game.points[0], 1)

    def test_point_is_awarded_to_the_right_player(self):
        self.game.open_card(5, True)
        self.game.open_card(0, False)
        self.game.open_card(3, True)
        self.assertEqual(self.game.points[1], 1)
