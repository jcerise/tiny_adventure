from dataclasses import dataclass

import pyxel

GRID_SIZE: int = 16
SCREEN_WIDTH: int = 480
SCREEN_HEIGHT: int = 360

@dataclass
class Vector2:
    x: int
    y: int

@dataclass
class Sprite:
    name: str
    sheet_x: int
    sheet_y: int
    width: int
    height: int

    def render(self, x: int, y: int) -> None:
        pyxel.blt(x, y, 0, self.sheet_x, self.sheet_y, self.width, self.height)

@dataclass
class Player:
    x: int
    y: int
    sprite: Sprite

    def move(self, dx: int, dy: int) -> None:
        new_x: int = self.x + dx
        new_y: int = self.y + dy
        self.x = new_x if SCREEN_WIDTH >= new_x >= 0 else self.x
        self.y = new_y if SCREEN_HEIGHT >= new_y >= 0 else self.y


class App:

    player: Player

    def __init__(self):
        pyxel.init(480, 360, display_scale=2)
        pyxel.mouse(True)
        pyxel.load("assets/tiny_adventure.pyxres")

        # Create a player, with a sprite
        player_sprite: Sprite = Sprite("player", 0, 0, 16, 16)
        self.player = Player(2, 2, player_sprite)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        player_movement: Vector2 = self._handle_movement_input()
        self.player.move(player_movement.x, player_movement.y)

    def draw(self):
        pyxel.cls(0)
        self.player.sprite.render(self.player.x, self.player.y)

    @staticmethod
    def _handle_movement_input() -> Vector2:
        dx: int = 0
        dy: int = 0
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            dx = -16
        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            dx = 16
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            dy = -16
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            dy = 16

        return Vector2(dx, dy)


if __name__ == "__main__":
    App()
