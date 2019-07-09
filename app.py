# -*- coding: utf-8 -*-

import pyxel


class App:
    def __init__(self):
        pyxel.init(128,128,caption="テトリス")

        pyxel.load('tetris.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    def draw(self):
        pyxel.cls(0)
        self.tilemap_draw()

    def tilemap_draw(self):
        base_x = 0
        base_y = 0
        num = 0
        u = 0
        v = 0
        w = 16
        h = 16
        pyxel.bltm(base_x,base_y,num,u,v,w,h)

if __name__ == "__main__":
    App()
