import unittest
from dataclasses import dataclass

from src.tiny_game.game import Player, SCREEN_WIDTH, SCREEN_HEIGHT


@dataclass
class SpriteMock:
    pass


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.sprite = SpriteMock()
        self.player = Player(0, 0, self.sprite)

    def test_move_within_screen(self):
        self.player.move(10, 10)
        self.assertEqual(self.player.x, 10)
        self.assertEqual(self.player.y, 10)

    def test_move_beyond_screen_width(self):
        self.player.move(SCREEN_WIDTH + 10, 10)
        self.assertEqual(self.player.x, 0)
        self.assertEqual(self.player.y, 10)

    def test_move_beyond_screen_height(self):
        self.player.move(10, SCREEN_HEIGHT + 10)
        self.assertEqual(self.player.x, 10)
        self.assertEqual(self.player.y, 0)

    def test_move_negative_x(self):
        self.player.move(-10, 10)
        self.assertEqual(self.player.x, 0)
        self.assertEqual(self.player.y, 10)

    def test_move_negative_y(self):
        self.player.move(10, -10)
        self.assertEqual(self.player.x, 10)
        self.assertEqual(self.player.y, 0)


if __name__ == "__main__":
    unittest.main()
