import pyxel

class App:
    def __init__(self):
        pyxel.init(240, 180, display_scale=2)
        pyxel.mouse(True)
        pyxel.load("assets/tiny_adventure.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(2, 2, 0, 0, 0, 16, 16)
        pyxel.blt(18, 2, 0, 16, 0, 16, 16)
        pyxel.blt(32, 2, 0, 32, 0, 16, 16)

App()